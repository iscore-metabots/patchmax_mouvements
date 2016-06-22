import get_coefficients # fonction entire_regression


def ask(source,degree):

    coefs = get_coefficients.entire_regression(source,degree)

    reponse = input("\nDo you want to change the initial coefficients of the regression ? (o/n) : ")
    print("Your answer : ", reponse)
    










    
ask("screenlog_interpolation.txt", 10)
    
