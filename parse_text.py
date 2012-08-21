from pyPdf import PdfFileReader
from subprocess import Popen
import os, commands, shlex

#Count Number of DOCS
response = os.popen("ls -1 *.pdf | wc -l")

for data in response:
	num_docs = data+""
	num_docs = num_docs.strip()



#Parse docs
i = 1
for filename in os.popen("ls *.pdf"):
	print "Processing file %s (%i of %s)" % (filename[:-1],i,num_docs)
	pdf_file = PdfFileReader(file(filename[:-1],"rb"))
	num_pages = pdf_file.getNumPages()
	
	#Each page goes into a separate TXT File
	for page in range(1,num_pages+1):
		command = "/usr/local/bin/pdf2txt.py -o %s_%i.txt -p %i %s" % (filename[:-5],page,page,filename[:-1])
		args = shlex.split(command)
		print "Page "+str(page)+" of "+str(num_pages)+"..."
		p = Popen(args)
		p.wait() # <--- blocks till done
	i = i + 1
	