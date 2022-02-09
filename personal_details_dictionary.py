import json

resume_details ={
    "primaryDetails": [
        {
            "Full Name": "Ma. Jensen Nicole C. Dela Rosa",
            "Sex / Gender": "Female (F)",
            "Age": "18 Years Old",
            "Home Address": "#563 Presidential St. Batasan Hills Quezon City",
            "Height": "158 cm",
            "Weight": "43 kg"
        }
    ],
    "contactInfo": [
        {
            "Email": "jendlrs333@gmail.com",
            "Cellphone number": "09748321023"
        }
    ],
    "academicBackground": [
        {
        "Elementary (2009-2015)": "Precious Learning Institute",
        "Junior High School (2015-1019": "Batasan Hills National High School",
        "Senior High School (2019-2021)": "Technological Institute of the Philippines",
        "College (PRESENT)": "Polytechnic University of the Philippines"
        }

    ],
    "achievements": [
        {
        "Achvmnts1": "Leadership awardee (2019)",
        "Achvmnts2": "Junior High School: Consistent With Honors (S. Y. 2015-2019)",
        "Achvmnts3": "Senior High School:", 
        "Achvmnts3_1": "Grade 11 (S. Y. 2019-2020): With High Honors",
        "Achvmnts3_2": "Grade 12 (S.Y. 2020-2021): With High Honors",
        "Achvmnts3_3": "2nd placer Physics Quiz Bee (2020)"
        }
    ],

    "characterReference": [
        {
        "Name":"Janeth A. Mendez",
        "Occupation": "Teacher",
        "WAddress":" University of Makati",
        "ContactN": "09273828031",
        "Email": "janeth16@gmail.com"
        "Janeth A. Mendez",
        }
    ],
    
    "coreCompetencies": [
        {
        "Competencies1": "Verbal and nonverbal communication skills",
        "Competencies2": "Fast Learner",
        "Competencies3": "Creative thinking"
        }
    ],

    "skills": [
        {
    "Skill1": "Clear communication and active learning skills",
    "Skill2": "Ability to meet deadlines",
    "Skill3": "Accuracy and skill in typing",
    "Skill4": "Capability to effort independently",
    "Skill 5": "Knowledge in computer operation"
        }
    ],

    "technicalQualification": [
        {
        "Microsoft Office": "Word, Excel, Powerpoint",
        "Programming Skills": "Python",
        "Graphic Editing": "Photoshop"
        }
    ]
}

file_json = json.dumps(resume_details, indent=2)
with open("personal_details.json", "w") as resume: 
    resume.write(file_json)