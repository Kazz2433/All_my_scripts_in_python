import PyPDF2, os 

pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
pdf_files.sort(key=str.lower)
pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
    pdf_file_obj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file_obj)
    for page_num in range(1, pdfReader.numPages):
        page_obj = pdfReader.getPage(page_num)
        pdf_writer.addPage(page_obj)
pdfOutput = open('allminutes.pdf', 'wb')
pdf_writer.write(pdfOutput)
pdfOutput.close()
