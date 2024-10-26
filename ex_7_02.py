# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
total_value = 0
line_count = 0
for lines in fh:
    if lines.startswith("X-DSPAM-Confidence:"):
        num1 = lines.find(':')
        found = lines[num1+1:]
        value = float(found.strip())
        total_value = total_value + value
        line_count = line_count + 1
        average = total_value / line_count
        
print('Average spam confidence: ', average)