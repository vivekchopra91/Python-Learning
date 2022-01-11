import PyPDF2
a = PyPDF2.PdfFileReader('pdf-reader/sample.pdf')
print(a.documentInfo)
# print(a.getDestinationPageNumber)
print(a.getNumPages())
print(a.getPageLayout())
print(a.getPage(0).extractText())