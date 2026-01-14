input_file = 'input/students.txt'
output_file = 'Output/output16.txt'

pattern = input('Pattern: ')

with open(input_file) as input_file_obj:
   names = input_file_obj.readlines()

result = filter(
    lambda name :
    name.startswith(pattern),
    names
)

with open(output_file, 'w') as output_file_obj:
    output_file_obj.writelines(result)