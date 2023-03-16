from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, default="./", help="input PDF dir")
parser.add_argument("-o", "--output", type=str, default="./", help="output PDF file")
args = parser.parse_args()

if __name__=='__main__':
    if not os.path.exists(args.input) or not os.path.isdir(args.input):
        print('No input dir')
        exit()
    if not os.path.exists(args.output) or not os.path.isdir(args.output):
        print('No output dir')
        exit()

    files = os.listdir(args.input)
    if len(files)<=0:
        exit()

    files = [[f, int(f.split('.', 1)[0])] for f in files]
    files = sorted(files, key=lambda x:x[1])
    output = PdfFileWriter()

    for content in files:
        filename = content[0]

        inputpdf = PdfFileReader(open(os.path.join(args.input, filename), 'rb'))
        for pageNum in range(inputpdf.numPages):
            output.addPage(inputpdf.getPage(pageNum))

    with open(os.path.join(args.output, "merged.pdf"), "wb") as outputStream:
        output.write(outputStream)