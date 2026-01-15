import csv

input_file = 'Input/students.txt'

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file,fieldnames=('name','grade'))
    next(reader)
    data = list(reader)


output_file = 'output/output20.txt'
with open(output_file,'w') as csv_file:
    writter = csv.DictWriter(csv_file,fieldnames=('name','grade'))
    writter.writerows(data)