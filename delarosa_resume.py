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
import json
from fpdf import FPDF

#Global variables
dlrs_resume = ('DELAROSA_MA.JENSENNICOLE.pdf')
json_details = ('personal_details.json')


#Read json file
with open (json_details) as fh:
    resume_data = json.loads(fh.read()) 

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

    def primaryDetails(self):
        self.set_font("times", "B", 13)
        self.cell (0,35, "", ln=True)
        self.set_fill_color(152,245,255)
        self.cell(115,8,"PERSONAL INFORMATION", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(70,7, "Full Name: " + str(resume_data["primaryDetails"][0]["Full Name"]),ln =True)
        self.cell(70,7, "Sex/Gender: " + str(resume_data["primaryDetails"][0]["Sex / Gender"]),ln =True)
        self.cell(70,7, "Age: " + str(resume_data["primaryDetails"][0]["Age"]),ln =True)
        self.cell(70,7, "Home Address: " + str(resume_data["primaryDetails"][0]["Home Address"]),ln =True)
        self.cell(70,7, "Height: " + str(resume_data["primaryDetails"][0]["Height"]),ln =True)
        self.cell(70,7, "Weight: " + str(resume_data["primaryDetails"][0]["Weight"]),ln =True)
    
    def contactInfo (self):
        self.set_font ("times", 'B', 13)
        self.cell (0,4, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(115,8,"CONTACT INFORMATION", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(70,7, "Email: " + str(resume_data["contactInfo"][0]["Email"]),ln =True)
        self.cell(70,7, "Cellphone Number: " + str(resume_data["contactInfo"][0]["Cellphone number"]),ln =True)

    def academicBackground (self):
        self.set_font ("times", 'B', 13)
        self.cell (0,4, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(115,8,"ACADEMIC BACKGROUND", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(70,7, "Elementary (2009-2015): " + str(resume_data["academicBackground"][0]["Elementary (2009-2015)"]),ln =True)
        self.cell(70,7, "Junior High School (2015-1019): " + str(resume_data["academicBackground"][0]["Junior High School (2015-1019"]),ln =True)
        self.cell(70,7, "Senior High School (2019-2021): " + str(resume_data["academicBackground"][0]["Senior High School (2019-2021)"]),ln =True)
        self.cell(70,7, "College (PRESENT): " + str(resume_data["academicBackground"][0]["College (PRESENT)"]),ln =True)

    def achievements(self):
        self.set_font ("times", 'B', 13)
        self.cell (0,4, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(115,8,"ACHIEVEMENTS", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts1"]),ln =True)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts2"]),ln =True)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts3"]),ln =True)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts3_1"]),ln =True)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts3_2"]),ln =True)
        self.cell(70,7, str(resume_data["achievements"][0]["Achvmnts3_3"]),ln =True)

 
#Set size of the paper and add blank page on the file
DelaRosa_PDF = PDF('P', 'mm', 'Letter')
DelaRosa_PDF.set_auto_page_break (margin =0.5, auto =True)
DelaRosa_PDF.add_page() 

#calling the functions
DelaRosa_PDF.primaryDetails()
DelaRosa_PDF.contactInfo()
DelaRosa_PDF.academicBackground()
DelaRosa_PDF.achievements()
#Saving into PDF file
DelaRosa_PDF.output(dlrs_resume) 
os.startfile(dlrs_resume)