input_file = 'input/students.txt'
input_file_obj = open(input_file)
content = input_file_obj.read()

students = content.split()

result = sorted(students)



output_file = 'Output/output13.txt'
output_file_obj = open(output_file,'w')
output_file_obj.write(str(result))



