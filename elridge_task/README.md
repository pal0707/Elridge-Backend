# Elridge-Backend

# Table of Contents
1. Getting Started
2. Endpoints
3. Authentication
4. Database
5. Built With

# Getting Started
To get started with this project, you'll need to clone the repository and set up a virtual environment:

# Clone the repository
git clone 
cd edridge_task

# Set up a virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
Once the server is running, you can access the API at http://localhost:8000/.

# Endpoints
The following endpoints are available:

# Blog Posts
GET /post/: Returns a list of all blog posts.
GET /post/:id/: Returns a specific blog post based on the id parameter.
POST /post/: Allows creating a new blog post. The request body should contain the title and content fields.
PUT /post/:id/: Allows updating an existing blog post. The request body should contain the title and content fields.
DELETE /post/:id/: Allows deleting an existing blog post.

# Authentication
POST /register/: Allows users to register for a new account. The request body should contain the username, email, and password fields.
POST /login/: Allows users to log in to their account. The request body should contain the username and password fields.

# Authentication
Some endpoints, such as creating or updating a blog post, require authentication. To authenticate, you should include an Authorization header in your request with a valid JWT token. To obtain a token, you should first register or log in a user, then include the token in subsequent requests.

# Database
This project uses a PostgreSQL database. You can modify the database settings in the settings.py file.

# Built With
This project was built with the following tools and libraries:

1. Django
2. Django Rest Framework
3. SQLite