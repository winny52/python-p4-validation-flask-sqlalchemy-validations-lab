from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 
      # Validation for author name
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError('Author name is required')
        return value

    # Validation for phone number
    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if value and (not value.isdigit() or len(value) != 10):
            raise ValueError('Author phone number must be exactly ten digits')
        return value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
  # Validation for post title
    @validates('title')
    def validate_title(self, key, value):
        if not value:
            raise ValueError('Post title is required')
        return value

    # Validation for post content length
    @validates('content')
    def validate_content_length(self, key, value):
        if len(value) < 250:
            raise ValueError('Post content must be at least 250 characters long')
        return value

    # Validation for post summary length
    @validates('summary')
    def validate_summary_length(self, key, value):
        if value and len(value) > 250:
            raise ValueError('Post summary must be a maximum of 250 characters')
        return value

    # Validation for post category
    @validates('category')
    def validate_category(self, key, value):
        if value not in ('Fiction', 'Non-Fiction'):
            raise ValueError('Post category must be either Fiction or Non-Fiction')
        return value

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title}, content={self.content}, summary={self.summary})'