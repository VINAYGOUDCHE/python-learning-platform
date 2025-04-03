from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import hashlib
from flask_migrate import Migrate
from models import db, User, UserProgress, UserProject, UserNote, JobSkill, ResourceCategory, Resource
from learning_content import (
    learning_paths, 
    projects, 
    exercises, 
    resources, 
    job_skills
)

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure database
db_url = os.environ.get('DATABASE_URL')
if db_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
else:
    # Fallback for local development
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonlearning.db'
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Create all tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learning_path')
def learning_path():
    return render_template('learning_path.html', paths=learning_paths)

@app.route('/lesson')
def lesson():
    # Generic lesson template for teaching purposes
    # In a real app, this would load data from a database
    return render_template('lesson.html')

@app.route('/python_basics')
def python_basics():
    # This is a specific lesson with hardcoded content for teaching Python
    return render_template('python_basics.html')

@app.route('/object_oriented')
def object_oriented():
    # Lesson for object-oriented programming in Python
    return render_template('object_oriented.html')

@app.route('/error_handling')
def error_handling():
    # Lesson for error handling in Python
    return render_template('error_handling.html')

# Intermediate level lessons
@app.route('/advanced_python')
def advanced_python():
    # Lesson for advanced Python features
    return render_template('advanced_python.html')

@app.route('/data_analysis')
def data_analysis():
    # Lesson for data analysis with Python
    return render_template('data_analysis.html')

@app.route('/web_development')
def web_development():
    # Lesson for web development basics
    return render_template('web_development.html')

@app.route('/technical_interviews')
def technical_interviews():
    # Technical interview preparation page
    return render_template('technical_interviews.html')

@app.route('/projects')
def project_page():
    return render_template('projects.html', projects=projects)

@app.route('/exercises')
def exercise_page():
    return render_template('exercises.html', exercises=exercises)

@app.route('/resources')
def resource_page():
    # Get resources and categories from database
    db_resources = Resource.query.all()
    categories = ResourceCategory.query.all()
    
    # Organize resources by category
    resources_by_category = {}
    for category in categories:
        resources_by_category[category.name] = []
        
    for resource in db_resources:
        category_name = ResourceCategory.query.get(resource.category_id).name
        resources_by_category[category_name].append({
            'title': resource.title,
            'url': resource.url,
            'description': resource.description,
            'type': resource.resource_type,
            'is_free': resource.is_free
        })
    
    return render_template('resources.html', 
                          resources=resources_by_category, 
                          static_resources=resources,  # Keep original data as fallback
                          categories=categories)

@app.route('/job_skills')
def job_skills_page():
    # Get skills from database
    all_skills = JobSkill.query.all()
    
    # Group skills by category
    skills_by_category = {}
    categories = []
    
    for skill in all_skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
            categories.append(skill.category)
            
        skills_by_category[skill.category].append({
            'name': skill.name,
            'description': skill.description,
            'importance': skill.importance_level
        })
    
    return render_template('job_skills.html', 
                          job_skills=skills_by_category,
                          categories=categories,
                          static_job_skills=job_skills)  # Keep original data as fallback

# User Authentication Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Basic validation
        if not all([username, email, password, confirm_password]):
            flash('All fields are required', 'danger')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return render_template('register.html')
            
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return render_template('register.html')
            
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already registered', 'danger')
            return render_template('register.html')
        
        # Hash password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Basic validation
        if not all([username, password]):
            flash('Username and password are required', 'danger')
            return render_template('login.html')
        
        # Hash password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Check user credentials
        user = User.query.filter_by(username=username, password_hash=password_hash).first()
        
        if user:
            # Set session
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear session
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' not in session:
        flash('Please log in to access your dashboard', 'warning')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # Get user progress data
    user_progress = UserProgress.query.filter_by(user_id=user_id).all()
    user_projects = UserProject.query.filter_by(user_id=user_id).all()
    
    return render_template('dashboard.html', 
                          user=user, 
                          progress=user_progress, 
                          completed_projects=user_projects)

# Helper function to check if user is logged in
def is_logged_in():
    return 'user_id' in session

# Make is_logged_in function available to templates
@app.context_processor
def utility_processor():
    return {
        'is_logged_in': is_logged_in
    }

# Custom filter for slicing lists in templates
@app.template_filter('slice')
def slice_filter(iterable, start, end=None):
    if end is None:
        return iterable[start:]
    return iterable[start:end]

# CLI command to initialize database with sample data
@app.cli.command('init-db')
def init_db_command():
    """Initialize the database with sample data."""
    # Add job skills categories
    categories = [
        "Programming Fundamentals", 
        "Web Development", 
        "Data Analysis", 
        "Machine Learning",
        "DevOps",
        "Database"
    ]
    
    skills = [
        # Programming Fundamentals
        {"name": "Python Syntax", "category": "Programming Fundamentals", "importance_level": 5, 
         "description": "Core Python syntax including variables, data types, control flow, and functions."},
        {"name": "Object-Oriented Programming", "category": "Programming Fundamentals", "importance_level": 4, 
         "description": "Understanding classes, inheritance, encapsulation, and polymorphism in Python."},
        {"name": "Data Structures", "category": "Programming Fundamentals", "importance_level": 5, 
         "description": "Working with lists, dictionaries, sets, tuples and understanding their performance characteristics."},
        {"name": "Algorithms", "category": "Programming Fundamentals", "importance_level": 4, 
         "description": "Implementing and analyzing common algorithms for searching, sorting, and problem-solving."},
        
        # Web Development  
        {"name": "Flask", "category": "Web Development", "importance_level": 4, 
         "description": "Building web applications with Flask framework."},
        {"name": "Django", "category": "Web Development", "importance_level": 4, 
         "description": "Developing robust web applications with Django framework."},
        {"name": "REST APIs", "category": "Web Development", "importance_level": 5, 
         "description": "Designing and implementing RESTful APIs for web services."},
        {"name": "HTML/CSS/JavaScript", "category": "Web Development", "importance_level": 3, 
         "description": "Frontend web development basics to complement Python backend skills."},
        
        # Data Analysis
        {"name": "Pandas", "category": "Data Analysis", "importance_level": 5, 
         "description": "Data manipulation and analysis with Pandas library."},
        {"name": "NumPy", "category": "Data Analysis", "importance_level": 4, 
         "description": "Numerical computing with NumPy arrays and functions."},
        {"name": "Data Visualization", "category": "Data Analysis", "importance_level": 4, 
         "description": "Creating visualizations with Matplotlib, Seaborn, or Plotly."},
        {"name": "SQL", "category": "Data Analysis", "importance_level": 5, 
         "description": "Writing efficient SQL queries for data extraction and analysis."},
        
        # Machine Learning
        {"name": "Scikit-learn", "category": "Machine Learning", "importance_level": 4, 
         "description": "Implementing machine learning algorithms with Scikit-learn."},
        {"name": "TensorFlow/PyTorch", "category": "Machine Learning", "importance_level": 3, 
         "description": "Building and training deep learning models."},
        {"name": "Machine Learning Concepts", "category": "Machine Learning", "importance_level": 4, 
         "description": "Understanding classification, regression, clustering, and model evaluation."},
        
        # DevOps
        {"name": "Git Version Control", "category": "DevOps", "importance_level": 5, 
         "description": "Using Git for source code management and collaboration."},
        {"name": "Docker", "category": "DevOps", "importance_level": 3, 
         "description": "Containerizing applications for consistent deployment."},
        {"name": "CI/CD", "category": "DevOps", "importance_level": 3, 
         "description": "Setting up continuous integration and deployment pipelines."},
        
        # Database
        {"name": "PostgreSQL", "category": "Database", "importance_level": 4, 
         "description": "Working with PostgreSQL databases in Python applications."},
        {"name": "SQLAlchemy", "category": "Database", "importance_level": 4, 
         "description": "Using SQLAlchemy ORM for database operations in Python."},
        {"name": "Database Design", "category": "Database", "importance_level": 4, 
         "description": "Designing efficient database schemas and relationships."}
    ]
    
    # Create resource categories
    resource_categories = [
        {"name": "Tutorials", "description": "Step-by-step guides for learning Python concepts and tools."},
        {"name": "Documentation", "description": "Official documentation and reference materials."},
        {"name": "Online Courses", "description": "Structured learning experiences for developing Python skills."},
        {"name": "Books", "description": "In-depth resources for comprehensive learning."},
        {"name": "Community Resources", "description": "Forums, blogs, and discussion boards for Python developers."},
        {"name": "Practice Sites", "description": "Websites for practicing coding challenges and improving skills."}
    ]
    
    # Create resources
    resources_data = [
        {"title": "Python.org Official Documentation", "url": "https://docs.python.org/3/", 
         "description": "The official Python documentation with tutorials, library references and more.",
         "resource_type": "documentation", "category": "Documentation", "is_free": True},
        
        {"title": "Real Python", "url": "https://realpython.com/", 
         "description": "Tutorials, articles, and courses for all levels of Python developers.",
         "resource_type": "tutorial", "category": "Tutorials", "is_free": True},
        
        {"title": "Python Crash Course (Book)", "url": "https://nostarch.com/pythoncrashcourse2e", 
         "description": "A hands-on, project-based introduction to Python programming.",
         "resource_type": "book", "category": "Books", "is_free": False},
        
        {"title": "Automate the Boring Stuff with Python", "url": "https://automatetheboringstuff.com/", 
         "description": "Practical programming for total beginners, available both as a book and free online.",
         "resource_type": "book", "category": "Books", "is_free": True},
        
        {"title": "Codecademy Python Course", "url": "https://www.codecademy.com/learn/learn-python-3", 
         "description": "Interactive Python course with hands-on exercises.",
         "resource_type": "course", "category": "Online Courses", "is_free": False},
        
        {"title": "LeetCode", "url": "https://leetcode.com/", 
         "description": "Platform to practice coding problems often used in technical interviews.",
         "resource_type": "practice", "category": "Practice Sites", "is_free": True},
        
        {"title": "Flask Documentation", "url": "https://flask.palletsprojects.com/", 
         "description": "Official documentation for the Flask web framework.",
         "resource_type": "documentation", "category": "Documentation", "is_free": True},
        
        {"title": "PythonAnywhere", "url": "https://www.pythonanywhere.com/", 
         "description": "Hosting platform for Python web applications with free tier.",
         "resource_type": "tool", "category": "Community Resources", "is_free": True},
        
        {"title": "SQLAlchemy Documentation", "url": "https://docs.sqlalchemy.org/", 
         "description": "Comprehensive documentation for the SQLAlchemy ORM.",
         "resource_type": "documentation", "category": "Documentation", "is_free": True},
        
        {"title": "Stack Overflow Python Tag", "url": "https://stackoverflow.com/questions/tagged/python", 
         "description": "Community Q&A for Python programming problems.",
         "resource_type": "community", "category": "Community Resources", "is_free": True}
    ]
    
    print("Starting database initialization...")
    
    # Add resource categories
    for cat_data in resource_categories:
        category = ResourceCategory(
            name=cat_data["name"],
            description=cat_data["description"]
        )
        db.session.add(category)
    
    # Commit to get category IDs
    db.session.commit()
    print("Resource categories added.")
    
    # Add resources
    for res_data in resources_data:
        category = ResourceCategory.query.filter_by(name=res_data["category"]).first()
        if category:
            resource = Resource(
                title=res_data["title"],
                url=res_data["url"],
                description=res_data["description"],
                resource_type=res_data["resource_type"],
                category_id=category.id,
                is_free=res_data["is_free"]
            )
            db.session.add(resource)
    
    # Add job skills
    for skill_data in skills:
        skill = JobSkill(
            name=skill_data["name"],
            category=skill_data["category"],
            description=skill_data["description"],
            importance_level=skill_data["importance_level"]
        )
        db.session.add(skill)
    
    db.session.commit()
    print("Database initialized with sample data.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
