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
    {
        "id": "beginner-2",
        "title": "Simple Calculator",
        "description": "Build a calculator program that performs basic arithmetic operations.",
        "difficulty": "Beginner",
        "estimated_hours": 3,
        "skills_practiced": ["Functions", "User input", "Basic operations", "Error handling"],
        "instructions": [
            "Create functions for addition, subtraction, multiplication, and division",
            "Implement a user interface (command line) to get input from users",
            "Handle division by zero and invalid inputs",
            "Allow users to perform multiple calculations in a session",
            "Display results with appropriate formatting"
        ],
        "extension_ideas": [
            "Add support for more complex operations (power, square root, etc.)",
            "Implement memory functions (store/recall results)",
            "Add support for parentheses in expressions",
            "Create a simple GUI using a library like Tkinter"
        ]
    },
    {
        "id": "intermediate-1",
        "title": "Data Analysis Dashboard",
        "description": "Create a program that analyzes a dataset and presents key insights.",
        "difficulty": "Intermediate",
        "estimated_hours": 8,
        "skills_practiced": ["Pandas", "Matplotlib/Seaborn", "Data analysis"],
        "instructions": [
            "Import and clean a dataset (CSV, Excel, or JSON)",
            "Perform basic statistics (mean, median, etc.) on the data",
            "Create at least three different types of visualizations",
            "Allow users to filter data based on criteria",
            "Export analysis results to a file"
        ],
        "extension_ideas": [
            "Add interactive elements to visualizations",
            "Implement more advanced statistical analysis",
            "Create a web dashboard using Flask",
            "Add predictive components using basic machine learning"
        ]
    }
]

# Practice exercises by topic
exercises = [
    {
        "id": "ex-basics-1",
        "title": "Number Guessing Game",
        "difficulty": "Beginner",
        "topic": "Python Basics",
        "description": "Create a simple number guessing game where the computer randomly selects a number and the user tries to guess it."
    },
    {
        "id": "ex-basics-2",
        "title": "List Manipulation",
        "difficulty": "Beginner",
        "topic": "Python Basics",
        "description": "Write functions to perform various operations on lists: finding max/min values, filtering even/odd numbers, etc."
    },
    {
        "id": "ex-oop-1",
        "title": "Bank Account System",
        "difficulty": "Beginner-Intermediate",
        "topic": "Object-Oriented Programming",
        "description": "Design a class hierarchy for different types of bank accounts with methods for deposit, withdrawal, and interest calculation."
    },
    {
        "id": "ex-oop-2",
        "title": "Library Management System",
        "difficulty": "Intermediate",
        "topic": "Object-Oriented Programming",
        "description": "Create classes for a library system with books, members, and borrowing functionality."
    },
    {
        "id": "ex-errors-1",
        "title": "Robust Input Handling",
        "difficulty": "Beginner",
        "topic": "Error Handling",
        "description": "Create a program that handles various types of user input errors using exception handling."
    },
    {
        "id": "ex-adv-1",
        "title": "Custom Iterator",
        "difficulty": "Intermediate",
        "topic": "Advanced Python",
        "description": "Design a custom iterator class that generates a Fibonacci sequence."
    },
    {
        "id": "ex-adv-2",
        "title": "Function Decorator",
        "difficulty": "Intermediate",
        "topic": "Advanced Python",
        "description": "Create a decorator that measures and logs the execution time of functions."
    }
]

# External resources organized by type
resources = {
    "Tutorials": [
        {
            "title": "Real Python",
            "url": "https://realpython.com/",
            "description": "Tutorials, articles, and courses for all levels of Python developers.",
            "type": "tutorial",
            "is_free": True
        },
        {
            "title": "Corey Schafer YouTube Channel",
            "url": "https://www.youtube.com/user/schafer5",
            "description": "In-depth video tutorials on Python programming and various libraries.",
            "type": "video",
            "is_free": True
        }
    ],
    "Documentation": [
        {
            "title": "Python Official Documentation",
            "url": "https://docs.python.org/3/",
            "description": "The official Python documentation with tutorials, library references and more.",
            "type": "documentation",
            "is_free": True
        },
        {
            "title": "Flask Documentation",
            "url": "https://flask.palletsprojects.com/",
            "description": "Official documentation for the Flask web framework.",
            "type": "documentation",
            "is_free": True
        }
    ],
    "Books": [
        {
            "title": "Python Crash Course",
            "url": "https://nostarch.com/pythoncrashcourse2e",
            "description": "A hands-on, project-based introduction to Python programming.",
            "type": "book",
            "is_free": False
        },
        {
            "title": "Automate the Boring Stuff with Python",
            "url": "https://automatetheboringstuff.com/",
            "description": "Practical programming for total beginners, available both as a book and free online.",
            "type": "book",
            "is_free": True
        }
    ],
    "Practice Sites": [
        {
            "title": "LeetCode",
            "url": "https://leetcode.com/",
            "description": "Platform to practice coding problems often used in technical interviews.",
            "type": "practice",
            "is_free": True
        },
        {
            "title": "HackerRank",
            "url": "https://www.hackerrank.com/domains/python",
            "description": "Practice Python skills with interactive challenges and competitions.",
            "type": "practice",
            "is_free": True
        }
    ]
}

# Job skills required for Python developers
job_skills = {
    "Programming Fundamentals": [
        {
            "name": "Python Syntax",
            "description": "Core Python syntax including variables, data types, control flow, and functions.",
            "importance": 5
        },
        {
            "name": "Object-Oriented Programming",
            "description": "Understanding classes, inheritance, encapsulation, and polymorphism in Python.",
            "importance": 4
        },
        {
            "name": "Data Structures",
            "description": "Working with lists, dictionaries, sets, tuples and understanding their performance characteristics.",
            "importance": 5
        },
        {
            "name": "Algorithms",
            "description": "Implementing and analyzing common algorithms for searching, sorting, and problem-solving.",
            "importance": 4
        }
    ],
    "Web Development": [
        {
            "name": "Flask",
            "description": "Building web applications with Flask framework.",
            "importance": 4
        },
        {
            "name": "Django",
            "description": "Developing robust web applications with Django framework.",
            "importance": 4
        },
        {
            "name": "REST APIs",
            "description": "Designing and implementing RESTful APIs for web services.",
            "importance": 5
        },
        {
            "name": "HTML/CSS/JavaScript",
            "description": "Frontend web development basics to complement Python backend skills.",
            "importance": 3
        }
    ],
    "Data Analysis": [
        {
            "name": "Pandas",
            "description": "Data manipulation and analysis with Pandas library.",
            "importance": 5
        },
        {
            "name": "NumPy",
            "description": "Numerical computing with NumPy arrays and functions.",
            "importance": 4
        },
        {
            "name": "Data Visualization",
            "description": "Creating visualizations with Matplotlib, Seaborn, or Plotly.",
            "importance": 4
        },
        {
            "name": "SQL",
            "description": "Writing efficient SQL queries for data extraction and analysis.",
            "importance": 5
        }
    ],
    "DevOps": [
        {
            "name": "Git Version Control",
            "description": "Using Git for source code management and collaboration.",
            "importance": 5
        },
        {
            "name": "Docker",
            "description": "Containerizing applications for consistent deployment.",
            "importance": 3
        },
        {
            "name": "CI/CD",
            "description": "Setting up continuous integration and deployment pipelines.",
            "importance": 3
        }
    ],
    "Database": [
        {
            "name": "PostgreSQL",
            "description": "Working with PostgreSQL databases in Python applications.",
            "importance": 4
        },
        {
            "name": "SQLAlchemy",
            "description": "Using SQLAlchemy ORM for database operations in Python.",
            "importance": 4
        },
        {
            "name": "Database Design",
            "description": "Designing efficient database schemas and relationships.",
            "importance": 4
        }
    ]
}
