#### Progression of the project

* __branch interpolation1.0__:
  * Nature: simple cubic interpolation between the values of a given motor.
  * Problems: curve too complex, impossible to get the polynom coefficients back.
  * Solution: smoothing the values before interpolation.


* __branch interpolation2.0__:
 * Nature: smoothing of motor values + cubic interpolation of these values
 * Problems: curve more simple but still impossible to get its coefficients back.
 * Solution: finding an average polynom between the values (polynomial regression).


* __branch regression
