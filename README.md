# AutoRoll
This is aplication 'AutoRoll'. Here you can rent a car for your trip or a significant event.

To FIRST run this project, you need:
1. Install all packages from 'requirements.txt'
2. Activate virtual environment  >> (for Windows:) .venv\Scripts\activate 
3. Connect to a local database and run the server (if it isn\`t running)
4. Run command >> alembic init alembic
5. Customize the 'alembic/env.py' and 'alembic.ini' files (by adding your local route)
6. Run command >> alembic upgrade head (to add tables to your local db)
7. Run command >> alembic revision -m "add models" --autogenerate


To run this project, you need:
1. Check if you are connected to a database
2. (If you don`t have tables) Run command >> alembic upgrade head
3. Run create_models to add notes in db


Tips:
* You can also add notes in tables or create new tables by using SQL language
