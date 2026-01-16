input_file = 'input/students.txt'
output_file = 'Output/output16.txt'

name = input('name: ').strip()
with open(input_file) as input_file_obj:
   names = input_file_obj.read().upper()
if name in names:
    print("Bu ism faylda mavjud ")
else:
    print("Bu ism faylda yo\'q ")
       


with open(output_file, 'w') as output_file_obj:
    output_file_obj.write(names)