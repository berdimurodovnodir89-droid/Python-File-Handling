input_file = 'input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

numbers = content.split()
numbers = list(map(
    lambda num :
    int(num),numbers
))
count = 0

for num in numbers:
    if num in numbers :
        count += 1

avg = num / count

output_file = 'Output/output05.txt'
output_file_obj = open(output_file,'w')
output_file_obj.write(str(avg))



