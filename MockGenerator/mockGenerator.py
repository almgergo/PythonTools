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
	
root = "P:/liquibaseSave/new/data/"
insert_root = "P:/liquibaseSave/new/insert/"
directory = os.fsencode(root)

for file in os.listdir(directory):
	filename = root + os.fsdecode(file)
	print(filename)
	
	csvHeader = ''
	with open(filename, 'rt', encoding='UTF-8') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')
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
		elif col=='CAPACITY' or col=='capacity':
			assumed_type = 'NUMERIC'
		elif col=='DEFAULT_ADDRESS' or  col=='default_address':
			assumed_type = 'BOOLEAN'
		elif col=='ACTIVE' or  col=='active':
			assumed_type = 'BOOLEAN'
		elif col=='MANDATORy' or  col=='mandatory':
			assumed_type = 'BOOLEAN'
		elif re.search('device_', col, re.IGNORECASE):
			assumed_type = 'STRING'
		elif re.search('interest_rate', col, re.IGNORECASE):
			assumed_type = 'NUMERIC'
		elif re.search('amount', col, re.IGNORECASE):
			assumed_type = 'NUMERIC'
		elif re.search('has', col, re.IGNORECASE):
			assumed_type = 'BOOLEAN'
		elif re.search('isdefault', col, re.IGNORECASE):
			assumed_type = 'BOOLEAN'
		elif re.search('string_id', col, re.IGNORECASE):
			assumed_type = 'STRING'
		elif re.search('_id', col, re.IGNORECASE):
			assumed_type = 'NUMERIC'
		elif re.search('createdat', col, re.IGNORECASE):
			assumed_type = 'DATE'			
		elif re.search('date', col, re.IGNORECASE):
			assumed_type = 'DATE'
		elif re.search('_at', col, re.IGNORECASE):
			assumed_type = 'DATE'

		else:
			assumed_type = 'STRING'

		newCol = insert_column
		file.write(newCol.replace('colname',col).replace('coltype',assumed_type))
		
	file.write(insert_end)
	file.close()
	
		
	