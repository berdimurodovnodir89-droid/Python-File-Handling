import csv

input_file = 'Input/students.txt'

with open(input_file) as csv_file:
    reader = csv.DictReader(csv_file,fieldnames=('name','grade'))
    next(reader)

    rows = []
    for row in reader:
        rows.append(row)

output_file = 'output/output19.txt'
with open(output_file,'w') as csv_file:
     writer = csv.DictWriter(csv_file, fieldnames=['name', 'grade'])
     writer.writerows(rows) 
