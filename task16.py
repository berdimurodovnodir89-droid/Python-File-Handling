input_file = 'input/students.txt'
with open(input_file) as input_file_obj:
    content = input_file_obj.read()
    students = content.split()

result = []
for student in students:
    if  len(student) >= 5:
        result.append(student)

output_file = 'Output/output16.txt'
with open(output_file, 'w') as output_file_obj:
    output_file_obj.write(str(result))