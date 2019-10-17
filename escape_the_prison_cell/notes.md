# solving the locks

## facts
1. worst case scenario is 100 spins, too slow for second lock

2. spinning by one each time is too slow, can reach 100 spins, most likely will not, but it can
 
## failed plans
1. spinning the lock by 2 each time, this misses even or odd numbers

## ENDING
so it really was as simple as just going one-by-one... spent like  5 hours trying to make a optimized
solution, when the challenge literally expected a for loop that spins it by one and check each
until it finds the right pin...