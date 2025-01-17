# Training data for resume entity extraction
TRAIN_DATA = [
    # Full Name
    ("John Smith is a senior software engineer.", {"entities": [(0, 10, "FULL_NAME")]}),
    ("Alice Johnson, a skilled front-end developer.", {"entities": [(0, 13, "FULL_NAME")]}),
    
    # Tech Stacks
    ("Proficient in Python, Docker, and AWS.", {"entities": [(13, 19, "TECH_STACK"), (21, 27, "TECH_STACK"), (33, 36, "TECH_STACK")]}),
    ("Skilled in React, Kubernetes, and SQL.", {"entities": [(10, 15, "TECH_STACK"), (17, 27, "TECH_STACK"), (33, 36, "TECH_STACK")]}),
    
    # Experience
    ("Over 7 years of experience in full-stack development.", {"entities": [(5, 14, "EXPERIENCE")]}),
    ("Worked as a backend developer for 10 years.", {"entities": [(38, 46, "EXPERIENCE")]}),
    
    # Institute
    ("Graduated from Stanford University with a CS degree.", {"entities": [(14, 33, "INSTITUTE")]}),
    ("Earned a Bachelor's degree from MIT.", {"entities": [(32, 35, "INSTITUTE")]}),
    
    # Language
    ("Fluent in English and Spanish.", {"entities": [(10, 16, "LANGUAGE"), (21, 28, "LANGUAGE")]}),
    ("Speaks Mandarin, French, and German.", {"entities": [(7, 15, "LANGUAGE"), (17, 23, "LANGUAGE"), (29, 35, "LANGUAGE")]}),
    
    # Email and Phone
    ("Contact me at john.doe@example.com or 123-456-7890.", {"entities": [(13, 33, "EMAIL"), (37, 49, "PHONE")]}),
    ("Reach out to alice@gmail.com at +1-800-555-1212.", {"entities": [(12, 27, "EMAIL"), (31, 46, "PHONE")]}),
    
    # Mixed Examples
    ("Emily Davis, a software engineer, is proficient in Python and JavaScript.", 
     {"entities": [(0, 12, "FULL_NAME"), (47, 53, "TECH_STACK"), (58, 69, "TECH_STACK")]}),
    ("Michael Brown graduated from UC Berkeley with expertise in Kubernetes.", 
     {"entities": [(0, 14, "FULL_NAME"), (23, 34, "INSTITUTE"), (53, 63, "TECH_STACK")]}),
    ("David Wilson has 8 years of experience in Docker, React, and AWS.", 
     {"entities": [(0, 12, "FULL_NAME"), (13, 23, "EXPERIENCE"), (27, 33, "TECH_STACK"), (35, 40, "TECH_STACK"), (46, 49, "TECH_STACK")]}),
    ("Jane Miller earned her degree from Harvard University and is skilled in SQL and Python.", 
     {"entities": [(0, 11, "FULL_NAME"), (28, 47, "INSTITUTE"), (65, 68, "TECH_STACK"), (73, 79, "TECH_STACK")]}),
    ("Thomas Lee speaks English and Spanish, with experience in Docker.", 
     {"entities": [(0, 11, "FULL_NAME"), (18, 24, "LANGUAGE"), (29, 36, "LANGUAGE"), (57, 63, "TECH_STACK")]}),
    ("Sarah Brown, fluent in Mandarin and French, has worked with React.", 
     {"entities": [(0, 11, "FULL_NAME"), (21, 29, "LANGUAGE"), (34, 40, "LANGUAGE"), (57, 62, "TECH_STACK")]}),
    ("Contact Peter White at peter.white@example.com or call +1-123-456-7890.", 
     {"entities": [(8, 19, "FULL_NAME"), (23, 46, "EMAIL"), (51, 66, "PHONE")]}),
    ("Anna Lee graduated from MIT with a Master's in Computer Science.", 
     {"entities": [(0, 8, "FULL_NAME"), (20, 23, "INSTITUTE")]}),
]
