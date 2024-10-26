import re
fhandle = open('regex_sum_ex.txt')
numbers_list = []
for line in fhandle:
    re_result = re.findall('[0-9]+', line)
    
    if re_result:
        numbers_list = numbers_list + re_result

sum_values = 0
for value in numbers_list:
    number = int(value)
    sum_values = sum_values + number

print(sum_values)
