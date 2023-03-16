from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str, default="", help="input PDF file")
parser.add_argument("-o", "--output", type=str, default="./", help="output PDF file")
args = parser.parse_args()

if __name__=='__main__':
    if args.file=="":
        print('No input pdf file')
        exit()
    if not os.path.exists(args.file) or not os.path.isfile(args.file):
        print('No input pdf file')
        exit()
    if not os.path.exists(args.output):
        print('No output dir')
        exit()
    with open(args.file, 'rb') as f:
        inputpdf = PdfFileReader(f)

        for i in range(len(inputpdf.pages)):
            output = PdfFileWriter()
            output.addPage(inputpdf.pages[i])
            with open(os.path.join(args.output, "{}.pdf".format(i)), "wb") as outputStream:
                output.write(outputStream)