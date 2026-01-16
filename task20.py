import csv

input_file = 'Input/students.txt'

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file,fieldnames=['name','grade'])
    next(reader)
    
    total_grade = sum(map(lambda item :int(item['grade']),reader))
    n = reader.line_num - 1
    avg_grade = total_grade / n


output_file = 'output/output20.txt'
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['average_grade'])
    writer.writeheader()
    writer.writerow({'average_grade': avg_grade})