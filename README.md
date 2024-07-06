# RESTO SERVICE

This is a microservice that implements a crud operation on a restaurant service

# Status

Working

# File Structure

    resto-coreservice/
    │
    ├── api/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   ├── middleware.py
    │   ├── home.py
    │   ├── proxy_view.py
    │   └── proxy_views.py
    │
    ├── apps/
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   │
    │   └── contact_service/
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── models.py
    │       ├── serializers.py
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    │
    ├── README.md
    ├── .gitignore
    ├── db.sqlite3
    ├── requirements.txt
    └── manage.py

# Explanations
1. api/:
    The api/ directory serves as the main configuration and entry point for your Django project.
    
    It typically contains:
    - settings.py: This file holds all the configuration settings for your Django project, including database settings, installed apps, middleware, and other project-wide configurations.
    - urls.py: This is the main URL configuration file that defines the top-level URL patterns for your entire project.
    - wsgi.py and asgi.py: These files are used for deploying your application with WSGI or ASGI servers.
    - middleware.py: Contains custom middleware for processing requests and responses.
    - proxy_view.py and proxy_views.py: These files likely contain views that act as proxies, possibly for forwarding requests to other services or handling them in a specific way.

    The api/ directory essentially sets up the overall structure and configuration of your Django project.

2. apps/core/:
    The core/ directory typically contains functionality that is central to your application and might be used across multiple other apps.
    
    It often includes:
    - Models for core data structures.
    - Views for basic functionality like health checks.
    - Utility functions or classes that are used throughout the project.
    - Custom management commands.
    - Handles things like API logging, health checks, and other foundational features of your microservice.

3. apps/contact_service/:
    This directory represents a specific feature or domain of your application, in this case, probably handling menu-related operations.
    
    It typically includes:
    - models.py: Defines the data models for this specific feature (e.g., MenuItem).
    - views.py: Contains the view logic for handling requests related to menu items (CRUD operations).
    - serializers.py: Defines how complex data types, like your models, should be converted to native Python datatypes that can then be easily rendered into JSON, XML, or other content types.
    - urls.py: Defines URL patterns specific to this app's functionality.

    The contact_service app encapsulates all the logic and data structures needed for managing menu items in your restaurant service.

4. Summary
    - api/ sets up the project and its configuration
    - apps/core/ provides central, shared functionality
    - apps/contact_service/ handles specific feature implementation (in this case, menu item management)


# How To Run It?

1. Set up database
We use postgresql for the database, and here is the SQL Query to setup the database:

    CREATE TABLE core_menu (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            description TEXT NOT NULL,
            stocks INTEGER NOT NULL CHECK (stocks >= 0),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );

Then make sure to add your postgresql connection credentials in the api/settings.py

2. Django installments
After cloning up the files and setting up the database connection, make sure you have all of the packages, modules, libraries, etc.

3. Migrate
before running it, you make sure to migrate them, in this case we just migrate the apps/core and apps/contact_service
To migrate, you can just run:

    python manage.py makemigrations core contact_service
    python manage.py migrate

Migrations in Django are necessary to synchronize your database schema with your model definitions. By running migrations, you ensure that your database structure matches your current models, allowing Django to interact correctly with the database and maintaining consistency across different environments and team members.

4. Run it
Finally you can just run it by doing the command:

    python manage.py runserver

5. Test on Postman
Then you can test the server in postman, since this is a CRUD Operations, therefore there are about 4-5 requests to be made:

- To Create:
        - set the request to POST
        - add the Endpoint:  http://127.0.0.1:8000/contact/menu-items
        - go to the body section and add the json format:
        {
            "name": "Kimbab",
            "price": 1.99,
            "description": "Delicious Wrapped Rice With Veggies",
            "stocks": 20
        }
        - click send

- To Get ALL:
        - set the request to GET
        - add the Endpoint:  http://127.0.0.1:8000/contact/menu-items
        - click send

- To Get By ID:
        - set the request to GET
        - add the Endpoint:  http://127.0.0.1:8000/contact/menu-items/(enter ID)
        - click send

- To Update:
        - set the request to PUT
        - add the Endpoint: http://127.0.0.1:8000/contact/menu-items/(enter ID)
        - - go to the body section and add the json format:
        {
            "name": "Kebab",
            "price": 4.99,
            "description": "Delicious Wrapped Donner With Veggies",
            "stocks": 45
        }
        - click send

- To Delete:
        - set the request to DELETE
        - add the Endpoint: http://127.0.0.1:8000/contact/menu-items/(enter ID)
        - click send


# Summary

A restaurant microservice demonstration with the implementation of CRUD Operations.
