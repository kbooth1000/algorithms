###   What is the smallest positive number 
###   that is evenly divisible by 
###   all of the numbers from 1 to 20?


def find_smallest_divisible(range_top):
    increment_num = range_top     
    for x in range(range_top, (range_top/2), -1):  
        print 'x = %d' % x 
        i = 1
        while True:
            
            if (i * increment_num) % (x - 1) != 0:
                i += 1
            else:
                increment_num = (i * increment_num)
                print 'increment num: %d' % increment_num
                break
    print i*increment_num

find_smallest_divisible(40)

### Thinking on this one: if the final number must be divisible by each
### number 1 thru 20, then it must be an even number (cause it needs to be 
### divisible by 2), and it needs to end in a 0 (aka, divisible by 10) 
### because it needs to also be divisible by 5 (by both 2 and 5). Then my logic
### jumped up to 'Well, it also needs to be divisible by 19 (for example), so 
### what's the first number divisible by both 10 and 19: 190. And it needs to be
### divisible by 20, so what's the first number divisible by both 190 and 20?:
### 380. So I saw a pattern: Each time a new higher number is found by which
### the final number must be divisible, there's no need to increment 
### through numbers between that new highest number and its next multiple -- 
### just skip straight to the next multiple of that number and test it 
### against your 1-20 (or better yet, 20-1) list until you find one that's
### not a factor of that new number. Then figure out the new first common
### product of those two numbers -- and that's your new increment. Start
### the loop over again until your 20-1 list gets to 1.

### (Then I realized, it probably doesn't need to go all the way to 1 -- it
### should be safe to stop incrementing at the half-point, cause
### anything after that should have been taken care of by going through the 
### higher half -- I'll still need to think about that to make sure that's
### true.)