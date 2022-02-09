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
        self.image ('2x2_picture.png',160,10,40,0)
        self.image ('divider.png',0,8,500,2)
        self.image ('divider.png',0,50,500,2)

    def primaryDetails(self):
        self.set_font("times", "B", 13)
        self.cell (0,25, "", ln=True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"PERSONAL INFORMATION", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(90,7, "Full Name: " + str(resume_data["primaryDetails"][0]["Full Name"]),ln =False, align = 'R')
        self.cell(80,7, "Sex/Gender: " + str(resume_data["primaryDetails"][0]["Sex / Gender"]),ln =True, align = 'R')
        self.cell(121,7, "Home Address: " + str(resume_data["primaryDetails"][0]["Home Address"]),ln =False, align ='R')
        self.cell(40,7, "Age: " + str(resume_data["primaryDetails"][0]["Age"]),ln =True, align= 'R')
        self.cell(45,7, "Height: " + str(resume_data["primaryDetails"][0]["Height"]),ln =False, align = 'R')
        self.cell(109,7, "Weight: " + str(resume_data["primaryDetails"][0]["Weight"]),ln =True, align= 'R')
    
    def contactInfo (self):
        self.set_font("times", "B",13)
        self.cell (0,1,"",ln =True)
        self.set_fill_color(152,245,255)
        self.cell (195, 8, "CONTACT INFORMATION", border=1, fill=True, align = 'C', ln=1)
        self.set_font ("times",'', 11)
        self.cell(69,7, "Email: " + str(resume_data["contactInfo"][0]["Email"]),ln =False, align = 'R')
        self.cell(116,7, "Cellphone Number: " + str(resume_data["contactInfo"][0]["Cellphone number"]),ln =True, align = 'R')

    def academicBackground (self):
        self.set_font ("times", 'B', 13)
        self.cell (0,1, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"ACADEMIC BACKGROUND", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(0,7, "Elementary (2009-2015): " + str(resume_data["academicBackground"][0]["Elementary (2009-2015)"]),ln =True, align = 'C')
        self.cell(0,7, "Junior High School (2015-1019): " + str(resume_data["academicBackground"][0]["Junior High School (2015-1019"]),ln =True, align = 'C')
        self.cell(0,7, "Senior High School (2019-2021): " + str(resume_data["academicBackground"][0]["Senior High School (2019-2021)"]),ln =True, align = 'C')
        self.cell(0,7, "College (PRESENT): " + str(resume_data["academicBackground"][0]["College (PRESENT)"]),ln =True, align = 'C')

    def achievements(self):
        self.set_font ("times", 'B', 13)
        self.cell (0,1, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"ACHIEVEMENTS", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(0,7, str(resume_data["achievements"][0]["Achvmnts2"]),ln =True, align = 'C')
        self.cell(0,7, str(resume_data["achievements"][0]["Achvmnts1"]),ln =True,  align = 'C')
        self.cell(0,7, str(resume_data["achievements"][0]["Achvmnts3"]),ln =True, align = 'C')
        self.cell(0,7, str(resume_data["achievements"][0]["Achvmnts3_1"]),ln =True, align = 'C')
        self.cell(100,7, str(resume_data["achievements"][0]["Achvmnts3_2"]),ln =False, align = 'R')
        self.cell(75,7, str(resume_data["achievements"][0]["Achvmnts3_3"]),ln =True, align = 'R')

    def skills (self):
        self.set_font ("times", 'B', 13)
        self.cell (0,1, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"SKILLS", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(90,7, str(resume_data["skills"][0]["Skill1"]),ln =False, align = 'R')
        self.cell(80,7, str(resume_data["skills"][0]["Skill2"]),ln =True, align = 'R')
        self.cell(70,7, str(resume_data["skills"][0]["Skill3"]),ln =False, align = 'R')
        self.cell(105,7, str(resume_data["skills"][0]["Skill4"]),ln =True, align = 'R')
        self.cell(0,7, str(resume_data["skills"][0]["Skill5"]),ln =True, align = 'C')

    def technicalQualification (self):
        self.set_font ("times", 'B', 13)
        self.cell (0,1, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"TECHNICAL QUALIFICATION", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(90,7, "Microsoft Office: " + str(resume_data["technicalQualification"][0]["Microsoft Office"]),ln =True, align = 'R')
        self.cell(90,7, "Programming Skill: " + str(resume_data["technicalQualification"][0]["Programming Skills"]),ln =True, align = 'R')
        self.cell(90,7, "Graphic Editing: "+str(resume_data["technicalQualification"][0]["Graphic Editing"]),ln=True, align = 'R')


    def characterReference(self):
        self.set_font ("times", 'B', 13)
        self.cell (0,1, "", ln =True)
        self.set_fill_color(152,245,255)
        self.cell(195,8,"CHARACTER REFERENCE", ln =1, border= 1, fill= True, align= 'C')
        self.set_font ("times",'', 11)
        self.cell(0,7, "Name: " + str(resume_data["characterReference"][0]["Name"]),ln =True, align = 'C')
        self.cell(90,7, "Occupation: " + str(resume_data["characterReference"][0]["Occupation"]),ln =False, align = 'R')
        self.cell(50,7, str(resume_data["characterReference"][0]["WAddress"]),ln =True, align = 'R')
        self.cell(97,7, "Contact Number: " + str(resume_data["characterReference"][0]["ContactN"]),ln =False, align = 'R')
        self.cell(50,7, "Email: " + str(resume_data["characterReference"][0]["Email"]),ln =False, align = 'R')

#Set size of the paper and add blank page on the file
DelaRosa_PDF = PDF('P', 'mm', 'Letter')
DelaRosa_PDF.set_auto_page_break (margin =0.5, auto =True)
DelaRosa_PDF.add_page() 

#calling the functions
DelaRosa_PDF.primaryDetails()
DelaRosa_PDF.contactInfo()
DelaRosa_PDF.academicBackground()
DelaRosa_PDF.achievements()
DelaRosa_PDF.skills()
DelaRosa_PDF.technicalQualification()
DelaRosa_PDF.characterReference()

#Saving into PDF file
DelaRosa_PDF.output(dlrs_resume) 
os.startfile(dlrs_resume)