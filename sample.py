'''
Created on 02-Jan-2020

@author: elango
'''
import html2text
with open("sample.html") as text_file:
    contents = text_file.read()
#print(contents)
openFile = open("sample.md", "a")
print(html2text1.html2text(contents))
appendFile = openFile.write(html2text1.html2text(contents))
openFile.close()
