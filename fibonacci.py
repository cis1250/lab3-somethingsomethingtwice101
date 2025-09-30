#!/usr/bin/env python3

# Fibonacci Sequence Exercise
nums = [0, 1]
terms = -1
while True:
    try:
        terms = int(input("Number of terms in the fibonacci sequence: "))
    except ValueError:
        print("Input is not a positive integer.")
        continue
        
    if (terms > 0):
        break
    print("Please enter a positive integer.")

for i in range(terms):
    if (i < len(nums)):
        print(nums[i])
        continue
    
    s = sum(nums)
    nums[0] = nums[1]
    nums[1] = s
    print(s)
