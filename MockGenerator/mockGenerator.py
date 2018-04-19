import os, csv
import re

insert_base = ''
with open('insert_base.txt', 'r') as myfile:
    insert_base=myfile.read()
	
insert_beforefilename = ''
with open('insert_beforefilename.txt', 'r') as myfile:
    insert_beforefilename=myfile.read()
	
insert_afterfilename = ''
with open('insert_afterfilename.txt', 'r') as myfile:
    insert_afterfilename=myfile.read()
	
insert_aftertablename = ''
with open('insert_aftertablename.txt', 'r') as myfile:
    insert_aftertablename=myfile.read()
	
insert_column = ''
with open('insert_column.txt', 'r') as myfile:
    insert_column=myfile.read()
	
insert_end = ''
with open('insert_end.txt', 'r') as myfile:
    insert_end=myfile.read()
	
root = "P:/liquibaseSave/data/"
insert_root = "P:/LFM.OTPF/backend/src/main/resources/csv_mock/insert/"
directory = os.fsencode(root)

for file in os.listdir(directory):
	filename = root + os.fsdecode(file)
	print(filename)
	
	csvHeader = ''
	with open(filename, 'rt', encoding='ANSI') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		csvHeader = next(reader)		
	
	shortfilename = filename.split('/')[-1]
	tablename = shortfilename.split('.')[0]
	filename = 'insert_' + tablename + '.xml'

	# print( '########### TABLENAME ###############')
	
	# print (insert_root + filename)
	file = open(insert_root + filename, 'w') 
	file.write(insert_base)
	file.write(tablename)
	file.write(insert_beforefilename)
	file.write('../../csv_mock/' + shortfilename)
	file.write(insert_afterfilename)
	file.write(tablename)
	file.write(insert_aftertablename)
	
	
	for col in csvHeader:
		if col=='id' or col=='ID':
			assumed_type = 'NUMERIC'
		elif col=='VERSION' or  col=='version':
			assumed_type = 'NUMERIC'
		elif re.search('default', col, re.IGNORECASE):
			assumed_type = 'BOOLEAN'
		elif re.search('_id', col, re.IGNORECASE):
			assumed_type = 'NUMERIC'
		elif re.search('date', col, re.IGNORECASE):
			assumed_type = 'DATE'
		else:
			assumed_type = 'STRING'

		newCol = insert_column
		file.write(newCol.replace('colname',col).replace('coltype',assumed_type))
		
	file.write(insert_end)
	file.close()
	
		
	