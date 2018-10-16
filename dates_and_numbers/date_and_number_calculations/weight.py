# References https://www.youtube.com/watch?v=k8asfUbWbI4

import datetime

# Constants
current_weight = 220
goal_weight = 180
avg_lbs_week = 2

# Init dates
start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(end_date)
# // Is floor division
print(f"Reached goal in {(end_date - start_date).days // 7} weeks")