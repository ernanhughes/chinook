# chinook

This is a FastAPI project that uses Prisma to connect to a Postgres database.

## Getting Started

1. Install postgresql and create a database called `chinook`
2. Update the `DATABASE_URL` in `.env` to point to your postgresql database.
3. Create a virtua environemtn to work with 
     `python -m venv venv` to create it 
     `.\venv\Scripts\Activate.ps1` to activate it 
3. Run `pip install -r .\requirements.txt` to install the dependencies.
4. Run `prisma db push --schema .\prisma\chinook.prisma` to create the database schema.
5. Run the script `python .\scripts\create_database.py` to populate the table data.
6. Run `uvicorn main:app --reload` to start the server.
7. You sahouls then be able to brows the api using
    `http:\\localhost:8001\docs`.


