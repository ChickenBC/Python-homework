filename = 'pi_digits.txt'

with open(filename) as file_object:
  lines = file_object.readlines()
  #readline()只读取第一行

pi_string = ' '
for line in lines:
  pi_string += line.strip()
  #strip()用于删除空格
  
print(pi_string)
print(len(pi_string))
