TRAIN_DATA = [
    # Full Names
    ("John Doe is a software developer.", {"entities": [(0, 8, "FULL_NAME")]}),
    ("Jane Smith is a full-stack developer.", {"entities": [(0, 10, "FULL_NAME")]}),
    ("Michael Johnson is a backend developer.", {"entities": [(0, 15, "FULL_NAME")]}),
    ("Abebe Tadesse is a full-stack developer.", {"entities": [(0, 13, "FULL_NAME")]}),
    ("Hana Mekonnen is a data scientist.", {"entities": [(0, 13, "FULL_NAME")]}),

    # Emails and Phones
    ("Email: john.doe@example.com | Phone: +1-123-456-7890", 
     {"entities": [(7, 27, "EMAIL"), (37, 52, "PHONE")]}),
    ("Email: jane.smith@example.com | Phone: +1-987-654-3210", 
     {"entities": [(7, 29, "EMAIL"), (39, 54, "PHONE")]}),
    ("Email: michael.johnson@example.com | Phone: +1-555-789-1234", 
     {"entities": [(7, 34, "EMAIL"), (44, 59, "PHONE")]}),
    ("Email: abebe.tadesse@example.com | Phone: +251-911-654-321", 
     {"entities": [(7, 32, "EMAIL"), (42, 58, "PHONE")]}),
    ("Email: hana.mekonnen@example.com | Phone: +251-922-987-654", 
     {"entities": [(7, 32, "EMAIL"), (42, 58, "PHONE")]}),

    # Technical Skills
    ("Skilled in Python, JavaScript, React, and Kubernetes.", 
     {"entities": [(11, 17, "TECH_STACK"), (19, 29, "TECH_STACK"), (31, 36, "TECH_STACK"), (42, 52, "TECH_STACK")]}),
    ("Proficient in TensorFlow, Scikit-learn, and PyTorch.", 
     {"entities": [(14, 24, "TECH_STACK"), (26, 38, "TECH_STACK"), (44, 51, "TECH_STACK")]}),
    ("Experienced with Tableau, Power BI, and PostgreSQL.", 
     {"entities": [(17, 24, "TECH_STACK"), (26, 34, "TECH_STACK"), (40, 50, "TECH_STACK")]}),

    # Experience
    ("Built a healthcare web application for rural clinics.", 
     {"entities": [(8, 52, "EXPERIENCE")]}),
    ("Built machine learning models to forecast agricultural yields in rural Ethiopia.", 
     {"entities": [(6, 79, "EXPERIENCE")]}),
    ("Created dashboards using Tableau for government agencies.", 
     {"entities": [(8, 57, "EXPERIENCE")]}),

    # Education
    ("Graduated with a Bachelor's in Software Engineering from Addis Ababa University.", 
     {"entities": [(57, 79, "INSTITUTE")]}),
    ("Earned a Master's degree in Data Science from Haramaya University.", 
     {"entities": [(46, 65, "INSTITUTE")]}),

    # Languages
    ("Fluent in Amharic and English.", 
     {"entities": [(10, 17, "LANGUAGE"), (22, 29, "LANGUAGE")]}),
    ("Speaks Amharic and Afaan Oromoo.", 
     {"entities": [(7, 14, "LANGUAGE"), (19, 32, "LANGUAGE")]}),

    # Projects
    ("Developed a scalable e-learning platform using Angular and Firebase.", 
     {"entities": [(47, 54, "TECH_STACK"), (59, 67, "TECH_STACK")]}),
    ("Developed a machine learning pipeline in TensorFlow and Scikit-learn.", 
     {"entities": [(41, 51, "TECH_STACK"), (56, 68, "TECH_STACK")]}),
    ("Created a business trend visualization tool using Tableau.", 
     {"entities": [(50, 57, "TECH_STACK")]}),

     # Resume 6
    ("Kebede Alemu is a skilled software engineer with 5 years of experience.", {"entities": [(0, 12, "FULL_NAME"), (26,70,"EXPERIENCE")]}),
    ("Contact: kebede.alemu@example.com | +251-933-456-789", {"entities": [(9, 33, "EMAIL"), (36, 52, "PHONE")]}),
    ("Earned a Bachelor’s degree in Computer Engineering from Jimma University.", {"entities": [(56, 72, "INSTITUTE")]}),
    ("Proficient in Java, Spring Boot, and Kubernetes.", {"entities": [(14, 18, "TECH_STACK"), (20, 31, "TECH_STACK"), (37, 47, "TECH_STACK")]}),
    ("Fluent in Amharic, English, and French.", {"entities": [(10, 17, "LANGUAGE"), (19, 26, "LANGUAGE"), (32, 38, "LANGUAGE")]}),

    # Resume 7
    ("Sara Mohammed is a project manager with 8 years of experience in Agile methodologies, Scrum, and Jira.", {"entities": [(0, 13, "FULL_NAME"), (19, 61, "EXPERIENCE"), (65, 84, "TECH_STACK"), (86, 91, "TECH_STACK"), (97, 101, "TECH_STACK")]}),
    ("Completed her MBA at Addis Ababa University and speaks Amharic, Arabic, and English.", {"entities": [(21, 43, "INSTITUTE"), (55, 62, "LANGUAGE"), (64, 70, "LANGUAGE"), (76, 83, "LANGUAGE")]}),
    ("You can reach her at sara.mohammed@projectmail.com or call her at +251911112233.", {"entities": [(21, 50, "EMAIL"), (66, 79, "PHONE")]}),

    # Resume 8
    ("Mekonnen Tesfaye is an IT consultant with expertise in cloud computing, AWS, and Docker.", {"entities": [(0, 16, "FULL_NAME"), (23, 36, "EXPERIENCE"), (55, 70, "TECH_STACK"), (72, 75, "TECH_STACK"), (81, 87, "TECH_STACK")]}),
    ("He studied at Addis Ababa Institute of Technology and is fluent in Amharic and English.", {"entities": [(14, 49, "INSTITUTE"), (67, 74, "LANGUAGE"), (79, 86, "LANGUAGE")]}),
    ("His contact is mekonnen.tesfaye@consultant.com and phone number is +251912345678.", {"entities": [(15, 46, "EMAIL"), (67, 80, "PHONE")]}),

    # Resume 9
    ("Liya Fekadu is a full-stack developer with expertise in React, Node.js, and MongoDB.", {"entities": [(0, 11, "FULL_NAME"), (17, 37, "EXPERIENCE"), (56, 61, "TECH_STACK"), (63, 70, "TECH_STACK"), (76, 83, "TECH_STACK")]}),
    ("She graduated from Jimma University and speaks Afaan Oromo and English.", {"entities": [(19, 35, "INSTITUTE"), (47, 58, "LANGUAGE"), (63, 70, "LANGUAGE")]}),
    ("Contact her at liya.fekadu@jimma.edu or call +251933334455.", {"entities": [(15,36 , "EMAIL"), (45, 58, "PHONE")]}),

    # Resume 10
    ("Hanna Tadesse is a data scientist with 6 years of experience in machine learning and AI.", {"entities": [(0, 13, "FULL_NAME"), (19, 60, "EXPERIENCE"), (64, 80, "TECH_STACK"), (85, 87, "TECH_STACK")]}),
    ("She earned her MSc in Data Science from Addis Ababa University and is fluent in English and Amharic.", {"entities": [(40, 62, "INSTITUTE"), (80, 87, "LANGUAGE"), (92, 99, "LANGUAGE")]}),
    ("You can reach her at hanna.tadesse@datascience.com or call +251923456789.", {"entities": [(21, 50, "EMAIL"), (59, 72, "PHONE")]}),

    # Resume 11
    ("I am Abebe Birhanu, a senior software developer with 10 years of experience in backend development and microservices.", {"entities": [(5, 18, "FULL_NAME"), (22, 75, "EXPERIENCE"), (79, 98, "TECH_STACK"), (103, 116, "TECH_STACK")]}),
    ("I hold a Bachelor’s degree in Computer Science from Addis Ababa University and am fluent in Amharic and English.", {"entities": [(52, 74, "INSTITUTE"), (92, 99, "LANGUAGE"), (104, 111, "LANGUAGE")]}),
    ("You can contact me at abebe.birhanu@devmail.com or reach me by phone at +251922233344.", {"entities": [(22, 47, "EMAIL"), (72, 85, "PHONE")]}),

    # Resume 12
    ("I am Fikirte Alemu, a data analyst with 4 years of experience specializing in data visualization and SQL.", {"entities": [(5, 18, "FULL_NAME"), (22, 61, "EXPERIENCE"), (78, 96, "TECH_STACK"), (101, 104, "TECH_STACK")]}),
    ("I graduated with a degree in Statistics from Bahir Dar University and am proficient in Amharic and English.", {"entities": [(45, 65, "INSTITUTE"), (87, 94, "LANGUAGE"), (99, 106, "LANGUAGE")]}),
    ("You can reach me at fikirte.alemu@data.com or call me at +251920998877.", {"entities": [(20, 42, "EMAIL"), (57, 70, "PHONE")]}),

    # Resume 13
    ("I am Tesfaye Zewde, an experienced web developer with 7 years of experience in developing web applications using JavaScript, React, and Node.js.", {"entities": [(5, 18, "FULL_NAME"), (23, 75, "EXPERIENCE"), (113, 123, "TECH_STACK"), (125, 130, "TECH_STACK"), (136, 143, "TECH_STACK")]}),
    ("I graduated with a Bachelor’s degree in Information Technology from Mekelle University and speak Amharic, Tigrinya, and Arabic.", {"entities": [(68, 86, "INSTITUTE"), (97, 104, "LANGUAGE"), (106, 114, "LANGUAGE"), (120, 126, "LANGUAGE")]}),
    ("You can contact me at tesfaye.zewde@techmail.com or reach me by phone at +251912344567.", {"entities": [(22,48 , "EMAIL"), (73, 86, "PHONE")]}),

    # Resume 14
    ("I am Mulugeta Hailu, a skilled machine learning engineer with 6 years of experience specializing in deep learning and natural language processing using TensorFlow, Keras, and Python.", {"entities": [(5, 19, "FULL_NAME"), (23, 145, "EXPERIENCE"), (152, 162, "TECH_STACK"), (164, 169, "TECH_STACK"), (175, 181, "TECH_STACK")]}),
    ("I hold a Master’s degree in Artificial Intelligence from Addis Ababa Institute of Technology and am fluent in English and Amharic.", {"entities": [(57, 92, "INSTITUTE"), (110, 117, "LANGUAGE"), (122, 129, "LANGUAGE")]}),
    ("You can email me at mulugeta.hailu@ai.com or call me at +251911223344.", {"entities": [(20, 41, "EMAIL"), (56, 69, "PHONE")]}),

    # Resume 15
    ("I am Samuel Gebremedhin, a passionate junior software developer with 2 years of experience in web development and programming using HTML, CSS, JavaScript, and Python.", {"entities": [(5, 23, "FULL_NAME"), (38, 90, "EXPERIENCE"), (132, 136, "TECH_STACK"), (138, 141, "TECH_STACK"), (143, 153, "TECH_STACK"), (159, 165, "TECH_STACK")]}),
    ("I graduated with a Bachelor’s degree in Computer Science from Addis Ababa University and am fluent in English and Amharic.", {"entities": [(62, 84, "INSTITUTE"), (102, 109, "LANGUAGE"), (114, 121, "LANGUAGE")]}),
    ("You can contact me at samuel.gebremedhin@devmail.com or call me at +251912334455.", {"entities": [(22, 52, "EMAIL"), (67, 80, "PHONE")]}),

    # Resume 16
    ("My name is Lemlem Assefa, a motivated entry-level data analyst with a strong background in Excel, SQL, and Power BI.", 
     {"entities": [(11, 24, "FULL_NAME"), (38, 62, "EXPERIENCE"), (91, 96, "TECH_STACK"), (98, 101, "TECH_STACK"), (107, 115, "TECH_STACK")]}),
    ("I earned a Bachelor’s degree in Statistics from Mekelle University and am proficient in Tigrinya and English.", 
     {"entities": [(48, 66, "INSTITUTE"), (88, 96, "LANGUAGE"), (101, 108, "LANGUAGE")]}),
    ("Feel free to reach out at lemlem.assefa@datamail.com or call me at +251922334455.", 
     {"entities": [(26, 52, "EMAIL"), (67, 80, "PHONE")]}),

    # Resume 17
    ("I am Bekele Tadesse, a junior cybersecurity professional with 1 year of experience in network security and threat analysis.", 
     {"entities": [(5, 19, "FULL_NAME"), (23, 82, "EXPERIENCE"), (86, 102, "TECH_STACK"), (107, 122, "TECH_STACK")]}),
    ("I graduated with a Bachelor’s degree in Computer Science from Bahir Dar University and am fluent in Amharic and English.", 
     {"entities": [(62, 82, "INSTITUTE"), (100, 107, "LANGUAGE"), (112, 119, "LANGUAGE")]}),
    ("You can contact me via email at bekele.tadesse@securemail.com or by phone at +251933445566.", 
     {"entities": [(32, 61, "EMAIL"), (77, 90, "PHONE")]}),

    # Resume 18
    ("My name is Fikirte Alemayehu, and I am a passionate junior mobile app developer with 3 years of experience in React Native, Flutter, and Kotlin.", 
     {"entities": [(11, 28, "FULL_NAME"), (52, 106, "EXPERIENCE"), (110, 122, "TECH_STACK"), (124, 131, "TECH_STACK"), (137, 143, "TECH_STACK")]}),
    ("I hold a Bachelor’s degree in Software Engineering from Adama Science and Technology University and am proficient in Afaan Oromo and English.", 
     {"entities": [(56, 95, "INSTITUTE"), (117, 128, "LANGUAGE"), (133, 140, "LANGUAGE")]}),
    ("Feel free to email me at fikirte.alemayehu@mobiledev.com or reach me on my phone at +251944556677.", 
     {"entities": [(25, 56, "EMAIL"), (84, 97, "PHONE")]}), 

     # Resume 19
     ("I am Dawit Tesfaye, a skilled backend developer with 4 years of experience in Node.js, MongoDB, and Express.js.", 
     {"entities": [(5, 18, "FULL_NAME"), (30, 74, "EXPERIENCE"), (78, 85, "TECH_STACK"), (87, 94, "TECH_STACK"), (100, 110, "TECH_STACK")]}),
    ("I graduated with a Bachelor’s degree in Information Technology from Haramaya University and am fluent in Oromiffa and Amharic.", 
     {"entities": [(68, 87, "INSTITUTE"), (105, 113, "LANGUAGE"), (118, 125, "LANGUAGE")]}),
    ("Contact me via email at dawit.tesfaye@backendpro.com or by phone at +251955667788.", 
     {"entities": [(24, 52, "EMAIL"), (68, 81, "PHONE")]}),

     # Resume 20
     ("My name is Selam Yohannes, and I am an experienced project manager with 7 years of expertise in Agile, Scrum, and Kanban methodologies.", 
     {"entities": [(11, 25, "FULL_NAME"), (51, 92, "EXPERIENCE"), (96, 101, "TECH_STACK"), (103, 108, "TECH_STACK"), (114, 120, "TECH_STACK")]}),
    ("I earned a Master’s degree in Project Management from St. Mary’s University and speak fluent Tigrinya and English.", 
     {"entities": [(54, 75, "INSTITUTE"), (93, 101, "LANGUAGE"), (106, 103, "LANGUAGE")]}),
    ("You can email me at selam.yohannes@pmail.com or reach me on my phone at +251966778899.", 
     {"entities": [(20, 44, "EMAIL"), (72, 85, "PHONE")]}),

]
