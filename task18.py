input_file = 'input/students.txt'
output_file = 'Output/output18.txt'

name = input('name: ')
with open(input_file) as input_file_obj:
   names = input_file_obj.read().split()
result = []
if  name in names :
    result.append(f"{name} faylda mavjud\n")
else :
    result.append(f"{name} faylda mavjud emas\n")


with open(output_file, 'w') as output_file_obj:
    output_file_obj.writelines(result)