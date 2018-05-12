import sys, re

def nonblank_lines(f):
	for l in f:
		line = l.rstrip()
		if line:
			yield line

def processHeader(header):
	header = header.rstrip()
	headerFields = header.split(';')
	#print((headerFields) )
	return headerFields
	
sourceFile = 'source.txt'


rows = []
with open(sourceFile) as f:
	header = processHeader(f.readline())
	#next(f)
	for line in nonblank_lines(f):
		li=line.strip()
		if (not li.startswith("#")):
			row = line.split(';')
			dictionary = {}
			for i in range(len(header)):
				dictionary[header[i]] = row[i]
			rows.append(dictionary)

templateString = ''

with open('template.xml', 'r') as myfile:
	templateString = myfile.read()
	#print(templateString)
	
	#print (rows);
	
i = 1
for row in rows:
	print(i)
	file = open('results/INK005_documentChanged_Request_' + str(i) + '.xml', 'w');     
	
	i += 1
	
	rowTemplate = templateString
	for key, value in row.items():
		#print ('<' + key + '>' + '?' + '</' + key + '>')
		#print( '<' + key + '>' + str(value) + '</' + key + '>')
		rowTemplate = re.sub('<' + key + '>' + '[?]' + '<\/' + key + '>' , '<' + key + '>' + str(value) + '</' + key + '>', rowTemplate, flags=re.I);        
		#print(templateString)
		#print()
	file.write(rowTemplate);
	file.close();
	
	