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

]
