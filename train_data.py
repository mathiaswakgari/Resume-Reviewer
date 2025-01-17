TRAIN_DATA = [
    # Technical skills
    ("Proficient in Python, SQL, and JavaScript.", {"entities": [(13, 19, "SKILL"), (21, 24, "SKILL"), (30, 40, "SKILL")]}),
    ("Skilled in Docker, Kubernetes, and Jenkins.", {"entities": [(10, 16, "SKILL"), (18, 28, "SKILL"), (34, 41, "SKILL")]}),
    ("Experienced with TensorFlow, PyTorch, and Scikit-learn.", {"entities": [(18, 28, "SKILL"), (30, 37, "SKILL"), (43, 56, "SKILL")]}),
    ("Knowledge of AWS, Azure, and Google Cloud Platform.", {"entities": [(12, 15, "SKILL"), (17, 22, "SKILL"), (28, 50, "SKILL")]}),
    ("Worked with databases like MySQL, MongoDB, and PostgreSQL.", {"entities": [(23, 28, "SKILL"), (30, 37, "SKILL"), (43, 53, "SKILL")]}),

    # Soft skills
    ("Strong communication and leadership skills.", {"entities": [(7, 20, "SKILL"), (25, 35, "SKILL")]}),
    ("Excellent problem-solving and time management abilities.", {"entities": [(10, 26, "SKILL"), (31, 47, "SKILL")]}),
    ("Teamwork, adaptability, and conflict resolution are my strengths.", {"entities": [(0, 8, "SKILL"), (10, 21, "SKILL"), (27, 46, "SKILL")]}),

    # Domain-specific skills
    ("Financial modeling and data analysis are key competencies.", {"entities": [(0, 18, "SKILL"), (23, 36, "SKILL")]}),
    ("Experienced in digital marketing and search engine optimization (SEO).", {"entities": [(15, 32, "SKILL"), (37, 63, "SKILL")]}),
    ("Expertise in supply chain management and inventory optimization.", {"entities": [(12, 34, "SKILL"), (39, 61, "SKILL")]}),

    # Tools and platforms
    ("Proficient in Tableau, Power BI, and Looker.", {"entities": [(13, 20, "SKILL"), (22, 30, "SKILL"), (36, 42, "SKILL")]}),
    ("Skilled in Adobe Photoshop, Illustrator, and Premiere Pro.", {"entities": [(10, 25, "SKILL"), (27, 38, "SKILL"), (44, 56, "SKILL")]}),
    ("Hands-on experience with Jenkins, Ansible, and Terraform.", {"entities": [(25, 32, "SKILL"), (34, 41, "SKILL"), (47, 56, "SKILL")]}),

    # Negative examples
    ("Graduated from the University of California.", {"entities": []}),
    ("Worked at the University of Technology.", {"entities": []}),
    ("The project was developed for the Department of Defense.", {"entities": []}),
    ("I studied at the Massachusetts Institute of Technology.", {"entities": []}),

    # Mixed sentences
    ("I am proficient in Python and have experience with Docker.", {"entities": [(17, 23, "SKILL"), (46, 52, "SKILL")]}),
    ("My skills include JavaScript, AWS, and leadership.", {"entities": [(17, 27, "SKILL"), (29, 32, "SKILL"), (38, 48, "SKILL")]}),
    ("Worked on financial modeling using Python and Excel.", {"entities": [(9, 27, "SKILL"), (34, 40, "SKILL"), (45, 50, "SKILL")]}),
    ("Familiar with agile methodologies like Scrum and Kanban.", {"entities": [(14, 21, "SKILL"), (43, 48, "SKILL"), (53, 59, "SKILL")]}),
    ("I used tools like Git, GitHub, and JIRA for project management.", {"entities": [(15, 18, "SKILL"), (20, 26, "SKILL"), (32, 36, "SKILL")]}),

    # Generic sentences with no entities
    ("The team worked together to complete the project.", {"entities": []}),
    ("This document was written using Microsoft Word.", {"entities": []}),
    ("Attended a workshop on improving leadership.", {"entities": [(33, 43, "SKILL")]}),
]
