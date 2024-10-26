# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
position1 = text.find(':')
last = len(text)
position2 = last
found = text[position1+1 : position2]
output = found.strip()
final_output = float(output)
print(output)