# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 12:20:09 2020

@author: Tuli
"""

def exp_sum(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  for num in range(1,n+1):
    for i in range(num,n+1):
      dp[i] += dp[i-num]
  print(dp)
  return dp[-1]
    
print(exp_sum(7))
