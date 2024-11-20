# Project Name  (Task Manager)


- Python Version: Python 3.12.0
- Bootstrap 5
- DJango default database sqlite3
- for API django rest framework

## Features

- Feature 1: User can Signup, Login, logout
- Feature 2: User can Add task into project
- Feature 3: User can POST, get, delete, task from api 


## Demo


## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/suyogbhere/Company_Count_Application/tree/master
    cd https://github.com/suyogbhere/Company_Count_Application/tree/master
    ```
## Usage
- for runing the project first go to project directory 
    - run following command python manage.py runserver
- Access the portal at http://127.0.0.1:8000
- Log in using default admin credentials (set in the admin panel).
- You can view tasks in the Admin dashboard.  http://127.0.0.1:8000/admin
- admin credentials  (usrname: admin,  pwd : admin)


## project Urls

1. http://127.0.0.1:8000/login/
2. http://127.0.0.1:8000/signup/


## API Urls
- for all data view, POST
1. http://127.0.0.1:8000/api/       
- for get, put 
1. http://127.0.0.1:8000/api/<int:id>    