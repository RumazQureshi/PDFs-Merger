import PyPDF2 #importing pypdf2 library for merging pdfs

pdf_files = ["1st PDF.pdf","2nd PDF.pdf","3rd PDF.pdf"] #list of pdf files to be merged
merger = PyPDF2.PdfMerger() #pdf merger object
for pdfs in pdf_files: #for loop for merging all the pdfs in the list
    merger.append(pdfs) #append will pend the pdf size 
merger.write("Merged.pdf") #it will create a new pdf named as merged.pdf
merger.close()
print('''PDFs MERGED SUCCESSFULLY INTO NEW PDF FILE "Merged.pdf" ''')