#install PyPDF2 Library in terminal 
#PyPDF lib capable of splitting, merging, cropping, and transforming the pages of PDF files
import PyPDF2
import sys
#OS library provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc
import os

#code
merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")
