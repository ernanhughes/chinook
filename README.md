# chinook

This is a FastAPI project that uses Prisma to connect to a Postgres database.

## Getting Started

1. Install postgresql and create a database called `chinook`
2. Update the `DATABASE_URL` in `.env` to point to your postgresql database.
3. Create a virtual environment to work with
   `python -m venv venv` to create it
   `.\venv\Scripts\Activate.ps1` to activate it
4. Run `pip install -r .\requirements.txt` to install the dependencies.
5. Run `prisma db push --schema .\prisma\chinook.prisma` to create the database schema.
6. Run the script `python .\scripts\create_database.py` to populate the table data.
7. Run `uvicorn chinook.main:app --reload` to start the server.
8. You should then be able to browse the api using
   `http://localhost:8001/docs`.
9. The Jupyter notebook in notebooks/chinook_restapi.ipynb shows how to use the api.


## Testing

Run `pytest` to run the tests.
`pytest tests --cov=chinook --cov-report=html` to run the tests and generate a coverage report.

You will need these dependencies to run the tests:
`httpx~=0.25.0
starlette~=0.27.0
pytest~=7.4.2`
