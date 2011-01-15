#!/usr/bin/env python
"""
Format tests
-------------------

>>> inPeriod ("yr{2007}", datetime (2007, 1, 1))
1

>>> inPeriod ("yr {2007}", datetime (2007, 1, 1))
1

>>> inPeriod ("yr{ 2007 }", datetime (2007, 1, 1))
1

>>> inPeriod ("yr { 2007 }", datetime (2007, 1, 1))
1

>>> inPeriod ("yr { 2007 - 2008 }", datetime (2007, 1, 1))
1

>>> inPeriod ("yr{ 2007-2008 }", datetime (2007, 1, 1))
1

>>> inPeriod ("yr{2007-2008}", datetime (2007, 1, 1))
1

>>> inPeriod ("yr {2007 2008}", datetime (2007, 1, 1))
1

Two options
>>> inPeriod ("yr {2007} wd {mon}", datetime (2007, 1, 1))
1

Two options with a comma
>>> inPeriod ("yr {2007}, min {5}", datetime (2007, 6, 12, 12, 5))
1

One option from each scale has to be true
>>> inPeriod ("yr {2007} wd {mon}", datetime (2007, 1, 2))
0

>>> inPeriod ("yr {2007} wd {tue-mon}", datetime (2007, 1, 1))
1

Options seperated by a comma are ORed together
>>> inPeriod ("min {5}, yr {2007}", datetime (2007, 6, 12))
1

Constants
>>> inPeriod ("always")
1

>>> inPeriod ("")
1

>>> inPeriod ("never")
0

>>> inPeriod ("min {5} min {10} min {15}", datetime (2007, 6, 12, 12, 15))
1

>>> inPeriod ("nv {2007} wd {tue-mon}", datetime (2007, 1, 1))
Traceback (most recent call last):
InvalidFormat: nv is not a valid scale.

>>> inPeriod ("x {2007}", datetime (2007, 1, 1))
Traceback (most recent call last):
InvalidFormat: x is not a valid scale.

>>> inPeriod ("none", datetime (2007, 1, 1))
0

Year tests
-------------------

>>> inPeriod ("yr {2007}", datetime (2007, 6, 1))
1

>>> inPeriod ("yr {2007-2009}", datetime (2009, 6, 1))
1

>>> inPeriod ("yr {2007 2009}", datetime (2007, 6, 1))
1

>>> inPeriod ("yr {2007 2009}", datetime (2008, 6, 1))
0

Numbers less than 100 assume the century of the datetime
>>> inPeriod ("yr {7}", datetime (2007, 6, 1))
1

>>> inPeriod ("yr {99}", datetime (1999, 6, 1))
1

>>> inPeriod ("yr {99}", datetime (2099, 6, 1))
1

>>> inPeriod ("yr {fred}", datetime (2099, 6, 1))
Traceback (most recent call last):
InvalidFormat: An integer value is required for year.

Long name
>>> inPeriod ("year {2009}", datetime (2009, 6, 12))
1

>>> inPeriod('yr {2015-2010}', datetime(2011, 1, 1))
1

>>> inPeriod('yr {1960}', datetime(1960, 1, 1))
1

Month tests
-------------------

>>> inPeriod ("mo {jun}", datetime (2099, 6, 1))
1

>>> inPeriod ("mo {jun-jul}", datetime (2099, 7, 1))
1

>>> inPeriod ("mo {nov-feb}", datetime (2099, 1, 1))
1

>>> inPeriod ("mo {jan mar jun}", datetime (2099, 3, 1))
1

>>> inPeriod ("mo {1-3}", datetime (2099, 2, 1))
1

Case insensitive and only the first three letters matter
>>> inPeriod ("mo {JUN-julio}", datetime (2099, 7, 1))
1

>>> inPeriod ("mo {13}", datetime (2099, 7, 1))
Traceback (most recent call last):
InvalidFormat: 13 is not valid for month. Valid options are between 1 and 12.

>>> inPeriod ("mo {0}", datetime (2099, 7, 1))
Traceback (most recent call last):
InvalidFormat: 0 is not valid for month. Valid options are between 1 and 12.

>>> inPeriod ("mo {garbledygook}", datetime (2099, 7, 1))
Traceback (most recent call last):
InvalidFormat: An integer value is required for month.

>>> inPeriod ("month {june}", datetime (2007, 6, 12))
1

Week tests
-------------------

>>> inPeriod ("wk {3}", datetime (2007, 6, 15))
1

>>> inPeriod ("wk {1 3 5}", datetime (2007, 6, 30))
1

>>> inPeriod ("wk {3-5}", datetime (2007, 6, 23))
1

>>> inPeriod ("wk {3-5}", datetime (2007, 6, 2))
0

>>> inPeriod ("wk {7}", datetime (2007, 6, 15))
Traceback (most recent call last):
InvalidFormat: 7 is not valid for week. Valid options are between 1 and 6.

>>> inPeriod ("wk {0}", datetime (2007, 6, 15))
Traceback (most recent call last):
InvalidFormat: 0 is not valid for week. Valid options are between 1 and 6.

>>> inPeriod ("wk {xxx}", datetime (2007, 6, 15))
Traceback (most recent call last):
InvalidFormat: An integer value is required for week.

>>> inPeriod ("week {3}", datetime (2007, 6, 12))
1

>>> inPeriod('wk {5-1}', datetime(2010, 12, 20))
0

>>> inPeriod('wk {6}', datetime(2011, 1, 31))
1

>>> inPeriod('wk {2}', datetime(2011, 1, 2))
1

>>> inPeriod('wk {1}', datetime(2011, 5, 1))
1

Year day tests
-------------------

>>> inPeriod ("yd {162}", datetime (2007, 6, 11))
1

>>> inPeriod ("yd {162}", datetime (2007, 6, 12))
0

>>> inPeriod ("yd {160-165}", datetime (2007, 6, 11))
1

>>> inPeriod ("yd {160 162 164}", datetime (2007, 6, 11))
1

Leap years have 366 days
>>> inPeriod ("yd {366}", datetime (2008, 12, 31))
1

>>> inPeriod ("yd {367}", datetime (2007, 6, 11))
Traceback (most recent call last):
InvalidFormat: 367 is not valid for year day. Valid options are between 1 and 366.

>>> inPeriod ("yd {0}", datetime (2007, 6, 11))
Traceback (most recent call last):
InvalidFormat: 0 is not valid for year day. Valid options are between 1 and 366.

>>> inPeriod ("yd {george}", datetime (2007, 6, 11))
Traceback (most recent call last):
InvalidFormat: An integer value is required for year day.

>>> inPeriod ("yday {163}", datetime (2007, 6, 12))
1

Month day tests
-------------------

>>> inPeriod ("md {12}", datetime (2007, 6, 12))
1

>>> inPeriod ("md {13}", datetime (2007, 6, 12))
0

>>> inPeriod ("md {10-15}", datetime (2007, 6, 12))
1

>>> inPeriod ("md {10 12 14}", datetime (2007, 6, 12))
1

>>> inPeriod ("md {29-14}", datetime (2007, 6, 12))
1

>>> inPeriod ("md {32}", datetime (2007, 6, 12))
Traceback (most recent call last):
InvalidFormat: 32 is not valid for day. Valid options are between 1 and 31.

>>> inPeriod ("md {0}", datetime (2007, 6, 12))
Traceback (most recent call last):
InvalidFormat: 0 is not valid for day. Valid options are between 1 and 31.

>>> inPeriod ("md {tom}", datetime (2007, 6, 12))
Traceback (most recent call last):
InvalidFormat: An integer value is required for day.

>>> inPeriod ("mday {12}", datetime (2007, 6, 12))
1

Weekday tests
-------------------

Match Mondays
>>> inPeriod ("wd {mon}", datetime (2007, 06, 11))
1

Match monday through friday, inclusively
>>> inPeriod ("wd {mon-fri}", datetime (2007, 06, 15))
1

Friday through tuesday
>>> inPeriod ("wd {fri-tue}", datetime (2007, 06, 11))
1

False test
>>> inPeriod ("wd {mon}", datetime (2007, 06, 12))
0

>>> inPeriod ("wd {mon-fri}", datetime (2007, 06, 16))
0

>>> inPeriod ("wd {fri-mon}", datetime (2007, 06, 12))
0

Only the first two characters matter in string names
>>> inPeriod ("wd {tuednesday}", datetime (2007, 06, 12))
1

>>> inPeriod ("wd {june}", datetime (2007, 06, 12))
Traceback (most recent call last):
InvalidFormat: An integer value is required for weekday.

>>> inPeriod ("wday {tue}", datetime (2007, 6, 12))
1

Hour tests
-------------------

>>> inPeriod ("hr {12}", datetime (2007, 6, 12, 12, 05))
1

>>> inPeriod ("hour {12}", datetime (2007, 6, 12, 12))
1

>>> inPeriod ("hr {10-14}", datetime (2007, 6, 12, 12, 05))
1

>>> inPeriod ("hr {10 12 13}", datetime (2007, 6, 12, 12, 05))
1

>>> inPeriod ("hr {12noon}", datetime (2007, 6, 12, 12, 05))
1

>>> inPeriod ("hr {noon}", datetime (2007, 6, 12, 12, 05))
1

>>> inPeriod("hr {12pm}", datetime(2007, 6, 12, 12, 05))
1

>>> inPeriod ("hr {12midnight}", datetime (2007, 6, 12, 0, 05))
1

>>> inPeriod ("hr {midnight}", datetime (2007, 6, 12, 0, 05))
1

>>> inPeriod ("hr {12am}", datetime (2007, 6, 12, 0, 05))
1

>>> inPeriod ("hr {10am-1pm}", datetime (2007, 6, 12, 13, 05))
1

>>> inPeriod ("hr {9pm-5am}", datetime (2007, 6, 12, 9))
0

>>> inPeriod ("hr {13am}", datetime (2007, 6, 12, 12, 05))
Traceback (most recent call last):
InvalidFormat: 13am is an invalid value for hour.

>>> inPeriod ("hr {24}", datetime (2007, 6, 12, 12, 05))
Traceback (most recent call last):
InvalidFormat: 24 is not valid for hour. Valid options are between 0 and 23.

>>> inPeriod ("hr {-1}", datetime (2007, 6, 12, 12, 05))
Traceback (most recent call last):
InvalidFormat: An integer value is required for hour.

>>> inPeriod ("hr {13pm}", datetime (2007, 6, 12, 12, 05))
Traceback (most recent call last):
InvalidFormat: 25 is not valid for hour. Valid options are between 0 and 23.

>>> inPeriod ("hr {fred-george}", datetime (2007, 6, 12, 12, 05))
Traceback (most recent call last):
InvalidFormat: An integer value is required for hour.

Minute Tests
-------------------

>>> inPeriod ("min {5}", datetime (2007, 6, 12, 12, 5))
1

>>> inPeriod ("min {2 4 6}", datetime (2007, 6, 12, 12, 6))
1

>>> inPeriod ("min {0-5}", datetime (2007, 6, 12, 12, 5))
1

>>> inPeriod ("min {0-5}", datetime (2007, 6, 12, 12, 45))
0

>>> inPeriod ("minute {5}", datetime (2007, 6, 12, 12, 5))
1

>>> inPeriod ("min {-1}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: An integer value is required for minute.

>>> inPeriod ("min {60}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: 60 is not valid for minute. Valid options are between 0 and 59.

>>> inPeriod ("min {harry}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: An integer value is required for minute.

Second Tests
-------------------

>>> inPeriod ("sec {5}", datetime (2007, 6, 12, 12, 5, 5))
1

>>> inPeriod ("sec {2 4 6}", datetime (2007, 6, 12, 12, 6, 6))
1

>>> inPeriod ("sec {0-5}", datetime (2007, 6, 12, 12, 5, 5))
1

>>> inPeriod ("sec {0-5}", datetime (2007, 6, 12, 12, 45, 45))
0

>>> inPeriod ("second {5}", datetime (2007, 6, 12, 12, 5, 5))
1

>>> inPeriod ("sec {-1}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: An integer value is required for second.

>>> inPeriod ("sec {60}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: 60 is not valid for second. Valid options are between 0 and 59.

>>> inPeriod ("sec {tom}", datetime (2007, 6, 12, 12, 5))
Traceback (most recent call last):
InvalidFormat: An integer value is required for second.

Time::Period's Examples
-------------------

>>> inPeriod ("wd {Mon-Fri} hr {9am-4pm}", datetime (2007, 8, 1, 12))
1

>>> inPeriod ("wd {Mon Wed Fri} hr {9am-4pm}, wd{Tue Thu} hr {9am-2pm}", datetime (2007, 7, 3, 15))
0

>>> inPeriod ("wk {1 3 5} wd {Mon Wed Fri} hr {9am-4pm}", datetime (2007, 8, 1, 12))
1

>>> inPeriod ("mo {Nov-Feb}", datetime (2007, 1, 1, 12))
1

>>> inPeriod ("mo {Jan-Feb Nov-Dec}", datetime (2007, 8, 1, 12))
0

>>> inPeriod ("mo {jan feb nov dec}", datetime (2007, 11, 1, 12))
1

>>> inPeriod ("mo {Jan Feb}, mo {Nov Dec}", datetime (2007, 12, 1, 12))
1

>>> inPeriod ("mo {Jan Feb} mo {Nov Dec}", datetime (2007, 1, 1, 12))
1

>>> inPeriod ("minute { 0-29 }", datetime (2007, 8, 1, 12, 15))
1

>>> inPeriod ("hour { 12am-11am }", datetime (2007, 8, 1, 1))
1

>>> inPeriod ("sec {0-4 10-14 20-24 30-34 40-44 50-54}", datetime (2007, 8, 1, 12, 15, 22))
1

>>> inPeriod ("wd {1 3 5 7} min {0-29}, wd {2 4 6} min {30-59}", datetime (2007, 6, 10, 12, 45))
0

Empty Ranges
------------

>>> inPeriod('yr {}', datetime(2011, 1, 1))
0

>>> inPeriod('mo {}', datetime(2011, 1, 1))
0

>>> inPeriod('wk {}', datetime(2011, 1, 1))
0

>>> inPeriod('yd {}', datetime(2011, 1, 1))
0

>>> inPeriod('md {}', datetime(2011, 1, 1))
0

>>> inPeriod('wd {}', datetime(2011, 1, 1))
0

>>> inPeriod('hr {}', datetime(2011, 1, 1))
0

>>> inPeriod('min {}', datetime(2011, 1, 1))
0

>>> inPeriod('sec {}', datetime(2011, 1, 1))
0

"""

from TimePeriod import inPeriod
from datetime import datetime

if __name__ == "__main__":
	import doctest
	doctest.testmod ()
