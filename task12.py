input_file = 'input/students.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

students = content.split()
result = 0
for student in students :
    if student in students :
        result += 1



output_file = 'Output/output12.txt'
output_file_obj = open(output_file,'w')
output_file_obj.write(str(result))



