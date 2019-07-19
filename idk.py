def to_camel_case(text):
  lis = list(text)
  for index, letter in enumerate(lis): 
    if letter == '-':
      lis[index + 1] = lis[index + 1].upper()
    return ''.join(lis).replace('-', '')
    
    if letter == '_':
      lis[index + 1] = lis[index + 1].upper()
    return ''.join(lis).replace('_', '')

hello = to_camel_case('the_stealth_warrior')
print(hello)