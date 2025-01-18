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
]
