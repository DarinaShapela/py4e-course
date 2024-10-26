import re

fhandle = open("regex_sum_test.txt")


numbers_list = []
for line in fhandle:
    re_result = re.findall("[0-9]+", line)
    #    print(re_result)

    if re_result:
        numbers_list = numbers_list + re_result

overall_values = 0
for value in numbers_list:
    nice_value = int(value)
    overall_values = overall_values + nice_value
print(overall_values)
