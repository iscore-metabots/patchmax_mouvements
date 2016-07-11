### Progression of the MAX interface part

It enables the user to send a textfile (corresponding to the movement orders, aka: the values of each motor through time).  
It hasn't been fully tested with the Metabot (only tested with "print"), but uses the same sending method as used by Robin in other efficient Maxpatchs. In order to work, the bluetooth connection needs to be maintained. It can be maintained by two methods: opening a "screen" on a terminal or using an external application to keep the connection.  
__Problem: A way the maintain the bluetooth connection on Mac and Windows needs to be found!__ 


### Progression of the interpolation part

* __branch interpolation1.0__:
  * Nature: simple cubic interpolation between the values of a given motor.
  * Problems: curve too complex, impossible to get the polynom coefficients back.
  * Solution: smoothing the values before interpolation.
  * See repertories "img" and "img_points" to observe the interpolated curve on an example.


* __branch interpolation2.0__:
 * Nature: smoothing of motor values + cubic interpolation of these values
 * Problems: curve more simple but still impossible to get its coefficients back.
 * Solution: finding an average polynom between the values (polynomial regression).
 * See repertories "img" and "img_points" to observe the interpolated curve on an example.


* __branch polynomial_regression__:
 * Nature: smoothing of motor values + polynomial regression of these values (returns an average polynom of degree chosen by user)
 * Problems: the movement generated is not recognisable when sent to the Metabot (the extreme values of the movement are not reached because the polynom is an average).
 * Solution: keeping the extreme values of the movement and make a linear regression between these values (thus, the movement will be divided into several parts and each part will be interpolated).


* __branch master__:
  * Contents: contains the polynomial regression API + the beginning of the division of movement according to its extreme values.


### TODO

* The decomposition of movement hasn't already been tested on a Metabot.
* Because this method hasn't been tested it maybe needs to be rearranged, and there may be better solutions.
* Find a way to maintain the bluetooth connection with Mac and Windows in order to use the Maxpatchs.


### Conclusion:

* "Simple cubic interpolation" and "smoothing + cubic interpolation" are inefficient methods.
* Polynomial regression is a method that works (the user can replenish a movement and modify the coefficients of the curve), but the movement obtained is not the expected movement.
* The extreme values method still needs to be worked on and maybe perfected.
* Maybe other interpolation methods could be found and performed.
* The bluetooth connection can be maintained easily on Linux with the application "Blueman", but a way to maintain it still needs to be found on Mac and Windows. Otherwise, an option could be to write in a terminal/shell from the Max interface to open a screen and send the movement there.