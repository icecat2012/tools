Split PDF:
1. The code will split the input pdf to multiple pdf (0.pdf, 1.pdf, 2.pdf ...). Each output pdf corresponds to each page of the input pdf.
splitPDF.py -f [pdf file path] -o [output dir]
Merge PDF: 
1. The name of the pdf files in input dir need to be i.pdf, where i is an integer number
2. The output merged.pdf contains the input pdfs, which are sorted by the integer (0.pdf, 1.pdf, 2.pdf ...)
mergePDF.py -i [dir with pdfs] -o [output dir]
