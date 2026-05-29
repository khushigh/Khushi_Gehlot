# pip install langchain (chunking)
# pip install langchain-community (chromadb vector store wrapper)
# pip install chromadb (vector database)
# pip install sentence-transformers (embedding model)
# pip install pypdf2 (pdf parsing)

import PyPDF2

a = PyPDF2.PdfReader('Course.pdf') #a is a PdfReader object that represents the PDF file "course.pdf". 
print(len(a.pages)) 

# print(a.pages[0].extract_text())
str = ""
for page in range(1, len(a.pages) ): 
    str += a.pages[page].extract_text() 

with open('course.txt', 'w', encoding='utf-8') as f: 
    f.write(str) 
