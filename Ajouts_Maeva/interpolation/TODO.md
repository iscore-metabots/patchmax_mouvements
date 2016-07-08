#### Progression of the project

* __branch interpolation1.0__:
  * Nature: simple cubic interpolation between the values of a given motor.
  * Problems: curve too complex, impossible to get the polynom coefficients back.
  * Solution: smoothing the values before interpolation.


* __branch interpolation2.0__:
 * Nature: smoothing of motor values + cubic interpolation of these values
 * Problems: curve more simple but still impossible to get its coefficients back.
 * Solution: finding an average polynom between the values (polynomial regression).


* __branch polynomial_regression__:
 * Nature: smoothing of motor values + polynomial regression of these values (returns an average polynom of degree chosen by user)
 * Problems: the movement generated is not recognisable (the extreme values of the movement are not reached because the polynom is an average).
 * Solution: keeping the extreme values of the movement and make a linear regression between these values (thus, the movement will be divided into several parts, each part will be interpolated).

* __branch master__:
  * Contents: contains the polynomial regression API + the beginning of the division of movement according to its extreme values.


#### TODO

* The decomposition of movement hasn't already been tested on a Metabot.
* Because this method hasn't been tested it maybe needs to be rearranged.

#### Conclusion:

* Simple cubic interpolation and smoothing + cubic interpolation are inefficient methods.
* Polynomial regression is a method that works (the user can replenish a movement and modify the coefficients of the curve), but the movement obtained is not the awaited movement.
* The extreme values method still needs to be worked on and maybe perfected.
* Maybe other interpolation methods could be found and performed.