input_file = 'input/numbers.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

numbers = content.split()
numbers = list(map(
    lambda num :
    int(num),numbers
))
result = list(filter(
    lambda num:
    num % 5 == 0,
    numbers
))

output_file = 'Output/output08.txt'
output_file_obj = open(output_file,'w')
output_file_obj.write(str(result))



