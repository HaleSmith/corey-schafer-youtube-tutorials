# References https://www.youtube.com/watch?v=k8asfUbWbI4

import datetime
import math

# Constants
goal_subs = 100000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / avg_subs_day)  # Rounds up

today = datetime.date.today()
print(today + datetime.timedelta(days=days_to_go))
