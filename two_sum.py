def two_sum(lis, target):
  first = None
  second = None 

  for num in lis:
    desired = target - num

    if desired in lis:
      second = lis.index(desired)

    if num + desired == target:
      first = lis.index(num)
      return [first, second]
      
  return 'None Found'

answer = two_sum([2, 11, 15], 9)
print(answer)