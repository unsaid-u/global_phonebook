## Global Phonebook

A backend application made using 
* Django
* Django-REST-framework
* sqlite (for maintiaing simplicty in the task)
* django-cache (for maintiaing simplicty in the task)
    

For running the application 

* Setup virtual environment
```python -m venv venv```

* Install the requirements
```pip install -r requirement.txt```

* Run the django application after migrating to the global Phonebook root directory
```python manage.py runserver ```

Make necessary DB migrations 
_Also Have added a script for adding dummy data i found online using a library called Faker. Although haven't tested it due to time constraint_



#### Endpoints

* `/user/` 
    * `/login/` - Authenticate users and provide a token for login.
    * `/register/` - Register a new user with provided details.
    * `/<str:user_id>/` - Retrieve or update details of a specific user by their ID.

* `/contacts/` 
    * `/` - Search for contacts based on query parameters.
    * `/ <int:contact_id>/spam` - Mark a specific contact as spam by its ID.
    * `/ <int:contact_id>/` - Retrieve or update details of a specific contact by its ID.


### Highlights
* Have used __JWT authentication__ for securing the APIs
* Have created __Paginated API__ for handling large data response
* Used __django-orm__ for manipulating database 
* Implemented __Caching__ for increasing efficiency of the APIs
* Added __Index__ in columns for speeding up query access to a column
* Followed proper module structure for better understanding and maintainability of the code base
* Moreover designed an overall scalable system
