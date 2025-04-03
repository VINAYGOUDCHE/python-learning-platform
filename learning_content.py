# This file contains all the learning content for the Python learning path application

# Learning paths structured by difficulty level
learning_paths = [
    {
        "level": "Beginner",
        "description": "Start your Python journey with the fundamentals",
        "topics": [
            {
                "title": "Python Basics",
                "description": "Learn the core syntax and concepts of Python",
                "subtopics": [
                    "Installing Python and setting up your environment",
                    "Variables, data types, and basic operations",
                    "Control flow: if statements, loops",
                    "Functions and modules",
                    "Basic data structures: lists, dictionaries, tuples, sets",
                    "File I/O operations"
                ],
                "time_estimate": "2-3 weeks",
                "route": "python_basics"
            },
            {
                "title": "Object-Oriented Programming",
                "description": "Master the principles of OOP in Python",
                "subtopics": [
                    "Classes and objects",
                    "Inheritance and polymorphism",
                    "Encapsulation and abstraction",
                    "Magic methods and operator overloading",
                    "Properties and descriptors"
                ],
                "time_estimate": "2 weeks",
                "route": "object_oriented"
            },
            {
                "title": "Error Handling",
                "description": "Learn to handle exceptions and write robust code",
                "subtopics": [
                    "Understanding exceptions",
                    "Try-except blocks",
                    "Raising exceptions",
                    "Custom exception classes",
                    "Context managers (with statement)"
                ],
                "time_estimate": "1 week",
                "route": "error_handling"
            }
        ]
    },
    {
        "level": "Intermediate",
        "description": "Enhance your Python skills with advanced concepts",
        "topics": [
            {
                "title": "Advanced Python Features",
                "description": "Explore Python's powerful features for efficient coding",
                "subtopics": [
                    "Decorators and closures",
                    "Generators and iterators",
                    "Context managers",
                    "Lambda functions and functional programming",
                    "Type hinting and annotations",
                    "Advanced OOP patterns"
                ],
                "time_estimate": "2-3 weeks",
                "route": "advanced_python"
            },
            {
                "title": "Data Analysis with Python",
                "description": "Learn to analyze and visualize data using Python libraries",
                "subtopics": [
                    "Introduction to NumPy",
                    "Data manipulation with Pandas",
                    "Data visualization with Matplotlib and Seaborn",
                    "Basic statistical analysis",
                    "Working with CSV, JSON, and Excel files",
                    "Web scraping for data collection"
                ],
                "time_estimate": "3-4 weeks",
                "route": "data_analysis"
            },
            {
                "title": "Web Development Basics",
                "description": "Build web applications using Python frameworks",
                "subtopics": [
                    "Introduction to web development concepts",
                    "Flask framework basics",
                    "Building RESTful APIs",
                    "Database integration with SQLAlchemy",
                    "Authentication and authorization",
                    "Deployment basics"
                ],
                "time_estimate": "4 weeks",
                "route": "web_development"
            }
        ]
    }
]

# Sample projects for different skill levels
projects = [
    {
        "id": "beginner-1",
        "title": "Command Line To-Do List Application",
        "description": "Build a simple command line application to manage to-do items with basic CRUD operations.",
        "difficulty": "Beginner",
        "estimated_hours": 4,
        "skills_practiced": ["Basic Python syntax", "File I/O", "Data structures"],
        "instructions": [
            "Create a command line interface that allows users to add, view, update, and delete tasks",
            "Store tasks in a text or JSON file",
            "Implement basic error handling",
            "Add the ability to mark tasks as complete",
            "Include a help command to show available options"
        ],
        "extension_ideas": [
            "Add due dates for tasks",
            "Implement task categories or priorities",
            "Add a search function",
            "Create a simple statistics feature (e.g., percentage of completed tasks)"
        ]
    },
