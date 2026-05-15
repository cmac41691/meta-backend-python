# Access Python system paths
import sys

locations = sys.path
print(locations)

for i in locations:
  print(i)

import calendar

leapdays = calendar.leapdays(2000, 2077)
print(leapdays)
isthatleap = calendar.isleap(2040)
print(isthatleap)
