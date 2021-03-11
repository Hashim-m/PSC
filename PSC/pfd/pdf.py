import PyPDF2
pdfobj=open("aaa.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(pdfobj)
with open("aa2.txt",'w') as hs:
    print(pdfReader.numPages)
    for i in range(pdfReader.numPages):
        pageobj=pdfReader.getPage(i)
        print(pageobj.extractText())
        #hs.write(str(pageobj.extractText()))
pdfobj.close()
