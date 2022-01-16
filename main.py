# Given n as input. Print sum of 4th power of all numbers from 1 to n. Check your output against following set of inputs.

n = 2
quad = 0
sum = 0
for i in range(1,n+1):
  quad = i*i*i*i
  sum = sum + quad
print(sum)