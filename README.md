# FastAPI Scraper Tool

This project is a Python FastAPI backend for for scraping websites. 
The project is scraping https://dentalstall.com/shop/ at the moment but can easily be tweaked to scrape any website just by adding a parser for the same.

## Requirements

- Python ^3.12 (Recommended: use pyenv or virtualenv to manage your Python environment)
- FastAPI
- Uvicorn (ASGI server)
- Poetry (Package Management)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BipinKalra/scraper-tool-fastapi.git
   cd scraper-tool-fastapi
   ```

2. Set up a virtual environment (optional but recommended):

   ```bash
   poetry shell
   ```

3. Install the dependencies:

   ```bash
   poetry install
   ```

## Running the Server

To start the FastAPI application, run the following command:

```bash
python app/app.py
```

This will start the server locally at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the API documentation (Swagger UI) at:

```
http://localhost:8000/docs
```

or the alternative ReDoc documentation at:

```
http://localhost:8000/redoc
```

## Authentication

The endpoints are authenticated using a simple JWT Token. No Secret has been used at the moment. Please generate a valid JWT token from https://jwt.io/ and use it to authenticate requests.

You can also use the following token to test.
```
JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.he0ErCNloe4J7Id0Ry2SEDg09lKkZkfsRiGsdX_vgEg
```

## Project Structure

```
.
├── poetry.lock                             # Package Lock file auto generated by poetry
├── pyproject.toml                          # Contains all project specs and dependencies
├── README.md                               # README file
└── app
    ├── app.py                              # FastAPI application instantiation
    ├── db             
          ├── data            
                └── products.json           # Local Products Database (JSON)
          ├── repos             
                └── products.py             # Products Repo to help communicate with the database
    ├── deps          
          └── authentication.py             # Authentication using JWT token
    ├── routes          
          ├── products.py                   # Route definition to list all products and search by ID
          └── scrape.py                     # Route definition to scrape from the target site
    └── services          
          ├── authentication
                └── scrape.py               # Authentication service
          └── scraper
                ├── parser
                      └── dental_stall.py   # Parsing logic for Dental Stall website
                ├── __init__.py             # Scraper Service with retry mechanism
                ├── interfaces.py           # Base Interface to be used to create different parsers
                └── models.py               # Data Model for products
```
