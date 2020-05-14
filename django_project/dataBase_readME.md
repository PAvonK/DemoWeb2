### Commands for database management through command line

ORM - object relational mapper = this allos us to access database in easy to use way which allows us to use different databased without chaning the code. (for instance we are going to use SQLite for testing and then PostGress database for production.)



models.py file contains the classes which set the attribues / fields for the database

#### python manage.py ## runserver = starts webserver

python manage.py makemigrations = create migrations which prepare for changes to the database

migrations will be found in app/migrations/0001_initial.py (app meaning the name of the app, in the case of this file 'blog')
** we can see the details in py file 0001_initial.py
** dont need to touch this.

python manage.py sqlmigrate blog 0001 = view SQLcode directly in the database
