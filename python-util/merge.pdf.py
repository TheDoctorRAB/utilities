#!/usr/bin/env python
# importing required modules
import PyPDF2
###
def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

def main():
    # pdf files to merge
    pdfs = ['2018 CFA ENV UI 18-15211.pdf', '2018 CFA ENV PU 18-15211.pdf']

    # output pdf file name
    output  = '2018 CFA ENV 18-15211.pdf'

    # calling pdf merge function
    PDFmerge(pdfs = pdfs, output = output)

if __name__ == "__main__":
    # calling the main function
    main()
# EOF
