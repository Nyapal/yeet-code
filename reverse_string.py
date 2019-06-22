def reverse_string(string):
  output = ''
  for letter in string[::-1]: 
    output += letter
  return output 
  # return string[::-1] # same ish but in one line 

answer = reverse_string('hello')
print(answer)