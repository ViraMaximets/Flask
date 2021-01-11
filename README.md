# AutoRoll
This is application 'AutoRoll'. Here you can rent a car for your trip or a significant event.

## Tools and Technologies
#### Core
Python
Flask
MySQL
#### Extensions
Flask-SQLAlchemy
Swagger/OpenAPI 3.0
#### Testing and Linting
pytest
Coverage.py
#### Services
GitHub

## FIRST run
1. Install all packages from 'requirements.txt'
2. Activate virtual environment:
 - (for Windows:) .venv\Scripts\activate 
3. Connect to a local database and run the server (if it isn\`t running)
4. Run command:
- alembic init alembic
5. Customize the '\_\_init__.py', 'alembic/env.py' and 'alembic.ini' files (by adding your local route)
6. Run commands: 
- alembic revision -m "add models" --autogenerate
- alembic upgrade head


## START
1. Check if you are connected to a database
2. If you don`t have tables run commands:
- alembic revision --autogenerate
- alembic upgrade head
3. Visit http://127.0.0.1:5000/
