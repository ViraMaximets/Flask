# AutoRoll
This is aplication 'AutoRoll'. Here you can rent a car for your trip or a significant event.

To FIRST run this project, you need:
1. Install all packages from 'requirements.txt'
2. Activate virtual enviroment  >> (for Windows:) .venv\Scripts\activate 
3. Connect to a local datebase and run the server (if it isn\`t running)
4. Run command >> alembic init alembic
5. Customize the 'alembic/env.py' and 'alembic.ini' files (by adding your local route)
6. Run command >> alembic upgrate head (to add tables to your local db)
7. Run create_models to add notes in db

To run this project, you need:
1. Check if you connect to a datebase
2. Run create_models to add notes in db

Tips:
* You can also add notes in tables or create new tables by using SQL language
