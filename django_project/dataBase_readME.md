## Commands for database management through command line

ORM - object relational mapper = this allos us to access database in easy to use way which allows us to use different databased without chaning the code. (for instance we are going to use SQLite for testing and then PostGress database for production.)

models.py file contains the classes which set the attribues / fields for the database

#### python manage.py runserver
    **starts webserver

#### python manage.py makemigrations 
    **create migrations which prepare for changes to the database

migrations will be found in app/migrations/0001_initial.py (app meaning the name of the app, in the case of this file 'blog')
** we can see the details in py file 0001_initial.py
** dont need to touch this.

#### python manage.py sqlmigrate blog 0001
    **view SQLcode directly in the database, it does it in the database that we are using which right now is sqlite

#### python manage.py migrate
    ** this make the changes to the database that is staged in the 0001 file.  
    ** Migrations also allow for the making changes to the database that is already running

### python manage.py shell
    ** this allows us to work in the python shell and work with our objects

#### >>> from blog.models import Post
#### >>> from djange.contrib.auth.models import User
    ** These import the models so we can work directly in those databases

#### >>> User.objects.all()
    ** queries all of the users

#### >>> User.objects.first()
    ** only the first user

#### >>> User.objects.filter(username='pvonkaenel')
    ** queries by the user

#### >>> User.objects.filter(username='pvonkaenel').first()
    ** by the user but only the first result in case there are more than one.

#### >>> user = User.objects.filter(username='pvonkaenel').first()
    ** captures in user variable

#### >>> user.id or user.pk
    ** shows id number or primary key number both equal 1 in this case

#### >>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
    ** creates a post for user 1 in shell

#### >>> post_1.save()
    ** saves that post to the database

#### >>> user.post_set.all()
    ** runs query on all user posts etc...

#### >>> user.post_set.create(title='Blog 3', content='Third Post Content!')
    ** adds post to that author with special 'set' - don't need to add author again since it already knows and it does not need saved like example above, this saves automatically.
