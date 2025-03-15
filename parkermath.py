# Parker Math!
# would it truly be Parker Math without Terrible Python Code?
# This code is licensed under Creative Commons Zero. No rights reserved. https://creativecommons.org/public-domain/cc0/

from math import * # Everything except for pi is the same as the math library
import datetime

# Matt Parker's values of pi, based on the system date. New values of pi become effective on Pi Day each year.
if datetime.date(2025, 3, 14) <= datetime.date.today():
    pi = 3.9
elif datetime.date(2024, 3, 14) <= datetime.date.today():
    pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223176
elif datetime.date(2023, 3, 14) <= datetime.date.today():
    pi = 3.11712
elif datetime.date(2022, 3, 14) <= datetime.date.today():
    pi = 3.14159265358
elif datetime.date(2021, 3, 14) <= datetime.date.today():
    pi = 3.875
elif datetime.date(2020, 3, 14) <= datetime.date.today():
    pi = 3.141591678589793935225
elif datetime.date(2019, 3, 14) <= datetime.date.today():
    pi = 3.11791
elif datetime.date(2018, 3, 14) <= datetime.date.today():
    pi = 3.141592751
elif datetime.date(2017, 3, 14) <= datetime.date.today():
    pi = 3.052338478336799
elif datetime.date(2016, 3, 14) <= datetime.date.today():
    pi = 3.04183997892940221112
elif datetime.date(2015, 3, 14) <= datetime.date.today():
    # Matt Parker used two methods of calculating pi in 2015. Thus, the rational thing to do is to randomly pick one, using the current microsecond as a seed.
    pi = 3.1512 if (datetime.now().microsecond % 2 == 0) else 3.128
else:
    pi = math.pi # This is the value of pi if this code is being used before March 14, 2015

# Fine, I'll add tau...
tau = 2 * pi
