import numpy as np;
import re; # regexp
import matplotlib.pyplot as plt;


def splint(xi, yi, y2i, x):
    kmin = 0;
    kmax = len(xi)-1;
    while(kmax-kmin > 1):
        k = (kmax+kmin)/2;
        if(xi[k]>x):
            kmax = k;
        else:
            kmin = k;
    h = xi[kmax]-xi[kmin];
    if(h == 0.0):
        print("Erreur");
    else:
        a = (xi[kmax]-x)/h;
        b = (x-xi[kmin])/h;
        c = (1/6)*(a**3-a)*((xi[kmax]-xi[kmin])**2)
        d = (1/6)*(b**3-b)*((xi[kmax]-xi[kmin])**2)
        return a*yi[kmin]+b*yi[kmax]+c*y2i[kmin]+d*y2i[kmax];


def spline(x, y, yp1, ypn):
    n = len(x);
    y2 = np.zeros([n]);
    u = range(0,n-1);
    if(yp1 > 0.99*(10**30)):
        y2[0] = 0.0;
        u[0] = 0.0;
    else:
        y2[0] = -0.5;
        u[0] = (3.0/(x[1]-x[0])) * ((y[1]-y[0])/(x[1]-x[0])-yp1);
    for i in range(1,n-1):
        sig = (x[i]-x[i-1])/(x[i+1]-x[i-1]);
        p = sig * y2[i-1] + 2.0;
        y2[i] = (sig-1.0)/p;
        u[i] = (y[i+1]-y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1]);
        u[i] = (6.0*u[i]/(x[i+1]-x[i-1]) - sig*u[i-1])/p;
    if(ypn > 0.99*(10**30)):
        qn = 0.0;
        un = 0.0;
    else:
        qn = 0.5;
        un = (3.0/(x[n-1]-x[n-2])) * (ypn-(y[n-1]-y[n-2])/(x[n-1]-x[n-2]));
    y2[n-1]=(un-qn*u[n-2])/(qn*y2[n-2]+1.0);
    for k in np.arange(n-2,-1,-1):
        y2[k]=y2[k]*y2[k+1]+u[k];

    return y2;


def interpolation(x,y):
    yp1 = (y[1]-y[0])/(x[1]-x[0]);
    ypn = (y[len(x)-1]-y[len(x)-2])/(x[len(x)-1]-x[len(x)-2]);
    y2 = spline(x,y,yp1,ypn);
    d = splint(x,y,y2,0);
    a = np.array([[0.25**3,0.25**2,0.25],[0.75**3,0.75**2,0.75],[1,1,1]]);
    b = np.array([splint(x,y,y2,0.25)-d,splint(x,y,y2,0.75)-d,splint(x,y,y2,1)-d]);
    p = np.linalg.solve(a,b);
    p = np.append(p,d);
    return p;

def f(p):
    return lambda x : p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3];

pe = interpolation(ex,ey);
pi = interpolation(ix,iy);
x = np.arange(0,1,0.001);
plt.plot(x,f(pe)(x));
plt.plot(x,f(pi)(x));
plt.show();
