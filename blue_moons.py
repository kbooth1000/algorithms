import math

month_change_days = [
    31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
]

top_yr = 2999
start_yr = 2000
day_nums = []
days_to_add = 0
blue_moons = 0

for yr in xrange(start_yr, top_yr+1):    
    for i in xrange(0, len(month_change_days)): 
        day_nums.append(int( month_change_days[i] + days_to_add ) ) #gives list of all days in century when the month changes over
    if yr % 4 == 0:
        days_to_add += 366
    else:
        days_to_add += 365

cycle_day = 0
moons_per_month = 0

day_nums.insert(0,0)

for j in xrange( 0, len(day_nums) ):
    moons_per_month = 0
    if j+1 < len(day_nums):
        while cycle_day >= day_nums[j] and cycle_day <= day_nums[j+1]:
            moons_per_month += 1
            if moons_per_month == 2:
                blue_moons += 1
                print 'bluemoons: %d' % blue_moons

            cycle_day += 29.5
        
        


    
print 'Blue Moons: %d' % blue_moons