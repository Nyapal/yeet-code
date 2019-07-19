import math

# math.exp( x )
# class Solution:

def reverse(x):
  string = str(x)
  lis = list(string)
  lis.reverse()
  string2 = ''.join(lis)
  whatever = int(string2)

  [−231,  231 − 1].

  #reverse the string.. 
  #if the string is not in range [−231,  231 − 1] return 0, 
  #if the last digit is -, move it to the front 
  
  # if lis[0] == '-':
  #   del lis[0]
  #   string1 = ''.join(lis)
  #   negative = '-' + string1
  #   return int(negative)
  # else: 
  #   lis.reverse()
  #   return ''.join(lis)

print(reverse(-123))