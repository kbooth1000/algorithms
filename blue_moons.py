# The moon goes through phases because it orbits the earth
# and the sun hits it differently at different places
# in its orbit. This means that, depending on where it is
# in its orbit, you might see a full moon, right quarter
# moon, or even "no" moon (new moon) at all. It takes 27.3
# days for the moon to orbit the Earth, but the actual 
# phase difference from one full moon to the next is 29.5 
# days because the earth cruises a cool 45 million miles
# around the sun in that 27.3 days. It takes 2.2 days for 
# the the moon to make up for that distance and get all 
# the way back to where you last saw a full moon.

# Whenever the moon is full twice in one month, the second 
# one is called a "blue moon." This happened in July of 
# 2015 on the 1st and 31st. The next time was January 
# of 2018 (same days). You can research the timing, 
# otherwise you can assume midnight. Write a program that 
# determines how many "blue moons" there will be in third 
# millenium (2000-2999).



import math

month_change_days = [
    31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
]

start_yr = 2001
top_yr = 2999

# calculate first lunar cycle in Jan of start_year
yrs_diff = 2018 - start_yr
days_diff = 0
days_in_year = 365
leap_years = 0
if yrs_diff >= 1:
    for i in range(2018, start_yr, -1):
        if i % 4 == 0:
            days_in_year = 366
            leap_years += 1
        else: 
            days_in_year = 365
        days_diff += i * days_in_year

days_til_first_cycle = days_diff % 29.5
print 'First cycle on Jan %d, %d' % (days_til_first_cycle, start_yr)


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

cycle_day = days_til_first_cycle
moons_per_month = 0

day_nums.insert(0,0)

month = 0
for j in xrange( 0, len(day_nums) ):
    moons_per_month = 0
    if j+1 < len(day_nums):
        while cycle_day >= day_nums[j] and cycle_day <= day_nums[j+1]:
            moons_per_month += 1
            if moons_per_month == 2:
                blue_moons += 1
                month = j - (12* math.floor(j/12))
                year = start_yr + math.floor(j/12) - 1
                print 'bluemoons: %d' % blue_moons
                print '%d / %d' % (month, year)

            cycle_day += 29.5
    
print 'Blue Moons: %d' % blue_moons