import PyPDF2
import sys

# with open('./dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)


#COMBINE all PDF
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
        merger.write('super.pdf')

pdf_combiner(inputs)