TRAIN_DATA = [
    # Tools
    ("Experienced with Git, GitHub, JIRA, and Trello.", {"entities": [(18, 21, "TOOL"), (23, 29, "TOOL"), (31, 35, "TOOL"), (40, 46, "TOOL")]}),
    ("Proficient in Tableau, Power BI, and Looker for data analysis.", {"entities": [(13, 19, "TOOL"), (22, 30, "TOOL"), (36, 42, "TOOL")]}),
    ("Skilled in Adobe Photoshop, Illustrator, and Premiere Pro for design.", {"entities": [(10, 25, "TOOL"), (27, 38, "TOOL"), (44, 56, "TOOL")]}),
    ("Worked with Jira, Slack, and Confluence for project management.", {"entities": [(18, 22, "TOOL"), (24, 29, "TOOL"), (34, 45, "TOOL")]}),
    ("Familiar with Docker, Kubernetes, and Jenkins for CI/CD pipelines.", {"entities": [(16, 22, "TOOL"), (24, 34, "TOOL"), (40, 47, "TOOL")]}),

    # Technologies
    ("Experienced with AWS, Azure, and Google Cloud for cloud computing.", {"entities": [(16, 19, "TECHNOLOGY"), (21, 26, "TECHNOLOGY"), (32, 50, "TECHNOLOGY")]}),
    ("Familiar with TensorFlow, PyTorch, and Scikit-learn for machine learning.", {"entities": [(18, 28, "TECHNOLOGY"), (30, 37, "TECHNOLOGY"), (43, 56, "TECHNOLOGY")]}),
    ("Knowledge of Hadoop, Spark, and Flink for big data processing.", {"entities": [(12, 18, "TECHNOLOGY"), (20, 25, "TECHNOLOGY"), (31, 36, "TECHNOLOGY")]}),
    ("Skilled in PostgreSQL, MongoDB, and MySQL for database management.", {"entities": [(13, 22, "TECHNOLOGY"), (24, 32, "TECHNOLOGY"), (38, 44, "TECHNOLOGY")]}),
    ("Experienced with Kubernetes, Docker, and Ansible for automation.", {"entities": [(16, 25, "TECHNOLOGY"), (27, 33, "TECHNOLOGY"), (39, 46, "TECHNOLOGY")]}),

    # Programming Languages
    ("Proficient in Python, JavaScript, Java, and C++.", {"entities": [(13, 19, "PROGRAMMING_LANGUAGE"), (21, 32, "PROGRAMMING_LANGUAGE"), (34, 38, "PROGRAMMING_LANGUAGE"), (43, 46, "PROGRAMMING_LANGUAGE")]}),
    ("Familiar with Ruby, PHP, and Swift for web development.", {"entities": [(16, 20, "PROGRAMMING_LANGUAGE"), (22, 25, "PROGRAMMING_LANGUAGE"), (30, 35, "PROGRAMMING_LANGUAGE")]}),
    ("Skilled in C#, Kotlin, and Go for backend development.", {"entities": [(13, 16, "PROGRAMMING_LANGUAGE"), (18, 23, "PROGRAMMING_LANGUAGE"), (28, 30, "PROGRAMMING_LANGUAGE")]}),
    ("Experienced in Rust, Python, and Java for performance-critical applications.", {"entities": [(17, 21, "PROGRAMMING_LANGUAGE"), (23, 29, "PROGRAMMING_LANGUAGE"), (34, 38, "PROGRAMMING_LANGUAGE")]}),
    ("Knowledge of Scala, TypeScript, and Dart for modern web applications.", {"entities": [(12, 17, "PROGRAMMING_LANGUAGE"), (19, 30, "PROGRAMMING_LANGUAGE"), (35, 39, "PROGRAMMING_LANGUAGE")]}),

    # Languages Spoken
    ("Fluent in English, Spanish, and French.", {"entities": [(10, 16, "LANGUAGE"), (18, 25, "LANGUAGE"), (30, 35, "LANGUAGE")]}),
    ("Speaks Mandarin, Cantonese, and basic Japanese.", {"entities": [(7, 15, "LANGUAGE"), (17, 26, "LANGUAGE"), (31, 38, "LANGUAGE")]}),
    ("Native speaker of German and Italian.", {"entities": [(19, 25, "LANGUAGE"), (30, 37, "LANGUAGE")]}),
    ("Fluent in Portuguese and Italian, basic knowledge of Russian.", {"entities": [(10, 19, "LANGUAGE"), (24, 30, "LANGUAGE"), (35, 42, "LANGUAGE")]}),
    ("Speaks Dutch, English, and some Arabic.", {"entities": [(7, 12, "LANGUAGE"), (14, 20, "LANGUAGE"), (25, 31, "LANGUAGE")]}),

    # Mixed examples
    ("Proficient in Python, Java, JavaScript, and AWS.", {"entities": [(13, 19, "PROGRAMMING_LANGUAGE"), (21, 25, "PROGRAMMING_LANGUAGE"), (31, 43, "PROGRAMMING_LANGUAGE"), (49, 52, "TECHNOLOGY")]}),
    ("Skilled in Docker, Kubernetes, and Python programming.", {"entities": [(13, 19, "TOOL"), (21, 31, "TOOL"), (36, 42, "PROGRAMMING_LANGUAGE")]}),
    ("Fluent in English and Spanish, experienced with SQL and AWS.", {"entities": [(10, 16, "LANGUAGE"), (21, 28, "LANGUAGE"), (36, 39, "TECHNOLOGY"), (44, 47, "TECHNOLOGY")]}),
    ("Experienced in Java, Swift, and Git for software development.", {"entities": [(16, 20, "PROGRAMMING_LANGUAGE"), (22, 27, "PROGRAMMING_LANGUAGE"), (32, 35, "TOOL")]}),
    ("Fluent in Mandarin, proficient in Python and Docker.", {"entities": [(10, 18, "LANGUAGE"), (28, 34, "PROGRAMMING_LANGUAGE"), (39, 45, "TOOL")]}),

    # Negative examples
    ("Graduated from the University of California.", {"entities": []}),
    ("Worked at the University of Technology.", {"entities": []}),
    ("The project was developed for the Department of Defense.", {"entities": []}),
    ("I studied at the Massachusetts Institute of Technology.", {"entities": []}),

    # Soft Skills (Bonus)
    ("Strong leadership, communication, and problem-solving skills.", {"entities": []}),
    ("Excellent teamwork, adaptability, and conflict resolution abilities.", {"entities": []}),
    ("Proven track record in managing teams, project planning, and customer service.", {"entities": []}),
]
