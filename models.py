from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# User model for authentication and tracking progress
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    progress = db.relationship('UserProgress', back_populates='user', cascade='all, delete-orphan')
    completed_projects = db.relationship('UserProject', back_populates='user', cascade='all, delete-orphan')
    notes = db.relationship('UserNote', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'

# Track user progress through learning paths
class UserProgress(db.Model):
    __tablename__ = 'user_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    path_id = db.Column(db.String(50), nullable=False)  # Identifier for the learning path
    topic_id = db.Column(db.String(50), nullable=False)  # Identifier for the specific topic
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    
    # Relationship
    user = db.relationship('User', back_populates='progress')
    
    def __repr__(self):
        return f'<UserProgress {self.user_id} - {self.path_id} - {self.topic_id}>'

# Track user completed projects
class UserProject(db.Model):
    __tablename__ = 'user_projects'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.String(50), nullable=False)  # Identifier for the project
    github_url = db.Column(db.String(255), nullable=True)  # Optional link to user's GitHub repo
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', back_populates='completed_projects')
    
    def __repr__(self):
        return f'<UserProject {self.user_id} - {self.project_id}>'

# User notes for learning material
class UserNote(db.Model):
    __tablename__ = 'user_notes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # 'learning_path', 'project', 'exercise', etc.
    content_id = db.Column(db.String(50), nullable=False)  # Identifier for the content
    notes = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    user = db.relationship('User', back_populates='notes')
    
    def __repr__(self):
        return f'<UserNote {self.user_id} - {self.content_type} - {self.content_id}>'

# Job skills tracking
class JobSkill(db.Model):
    __tablename__ = 'job_skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'programming', 'database', 'framework'
    description = db.Column(db.Text, nullable=True)
    importance_level = db.Column(db.Integer, nullable=False, default=1)  # 1-5 rating of importance
    
    def __repr__(self):
        return f'<JobSkill {self.name} - {self.category}>'

# Resource categories and tags
class ResourceCategory(db.Model):
    __tablename__ = 'resource_categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    # Relationships
    resources = db.relationship('Resource', back_populates='category')
    
    def __repr__(self):
        return f'<ResourceCategory {self.name}>'

# External resource links
class Resource(db.Model):
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    resource_type = db.Column(db.String(20), nullable=False)  # 'video', 'article', 'tutorial', etc.
    category_id = db.Column(db.Integer, db.ForeignKey('resource_categories.id'), nullable=False)
    is_free = db.Column(db.Boolean, default=True)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    category = db.relationship('ResourceCategory', back_populates='resources')
    
    def __repr__(self):
        return f'<Resource {self.title}>'
