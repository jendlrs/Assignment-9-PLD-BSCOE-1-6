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
import os
from fpdf import FPDF

#Global variables
dlrs_resume = ('DELAROSA_MA.JENSENNICOLE.pdf')
json_details = ('personal_details.json')

#Header
Name = 'DELA ROSA, MA. JENSEN NICOLE C.'
position = 'Computer Engineering Student'

class PDF (FPDF):
    def header (self):
        #Font size and font style and format of the string for header
        self.set_font('times','B', 20)
        self.cell (205,30, Name)
        self.ln(20)
        self.set_font ('times','', 15)
        self.cell (-137, 5, position)
        #for images
        self.image ('2x2_picture.png',150,10,50,0)
        self.image ('divider.png',0,8,500,2)
        self.image ('divider.png',0,60,500,2)

    def body (self, name):
        #Read json file
        with open (json_details) as fh:
            resume_data = fh.read() 
        self.set_font ('times', "", 12)
        self.multi_cell (0, 7,resume_data, border=0, align ="R")
        self.ln(2)

    def output_ (self, name):
        self.body(name)
    
#Set size of the paper and add blank page on the file
DelaRosa_PDF = PDF('P', 'mm', 'Letter')
DelaRosa_PDF.set_auto_page_break (margin =0.5, auto =True)
DelaRosa_PDF.add_page() 
DelaRosa_PDF.body(json_details)

#Saving into PDF file
DelaRosa_PDF.output(dlrs_resume) 
os.startfile(dlrs_resume)