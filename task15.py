input_file = 'input/students.txt'
with open(input_file) as input_file_obj:
    content = input_file_obj.read()
    students = content.split()

result = {}
for num in students:
    uzunlik = len(num)
    if uzunlik in result:
        result[uzunlik] += 1  
    else:
        result[uzunlik] = 1 

output_file = 'Output/output15.txt'
with open(output_file, 'w') as output_file_obj:
    output_file_obj.write(str(result))