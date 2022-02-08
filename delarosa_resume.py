#PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually
#	- Your code should be in github before Feb12

#Import needed modules
from fpdf import FPDF

#Global variables
dlrs_resume = ('DELAROSA_MA.JENSENNICOLE.pdf')

#Header
Name = 'DELA ROSA, MA. JENSEN NICOLE C.'
position = 'Computer Engineering Student'

#Set size of the paper and add blank page on the file
DelaRosa_PDF = FPDF('P', 'mm', 'Letter'); 
DelaRosa_PDF.add_page() 

#Font size and font style and format of the string for header
DelaRosa_PDF.set_font('times', 'B', 20) 
DelaRosa_PDF.cell(205, 15, Name) 
DelaRosa_PDF.set_font ('times','',15)
DelaRosa_PDF.cell (-137, 28, position, border=0,align="R", ln=2)

#For images
DelaRosa_PDF.image ('2x2_picture.png',150,10,50,0) #2x2 picture on the top right of the document
DelaRosa_PDF.image ('divider.png',0,8,500,2) #Left, Up Length, Width
DelaRosa_PDF.image ('divider.png',0,60,500,2) #Left, Up Length, Width

#Saving into PDF file
DelaRosa_PDF.output(dlrs_resume) 