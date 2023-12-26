# ElectroMarketHub

Brief project description goes here.

## Getting Started

These instructions will guide you through setting up and running the project on your local machine.


1. Clone the project repository:

```bash
git clone https://github.com/rusanov8/ElectroMarketHub.git
```

2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
  - On Windows:
    ```bash
    .\env\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source env/bin/activate
    ```


4. Install project dependencies:

  Use the package manager [pip](https://pip.pypa.io/en/stable/) to install project dependencies.
```bash
pip install -r requirements.txt
 ```


5. Create a Database:
- Ensure PostgreSQL is installed on your system.
- Create a new PostgreSQL database for the project.


6. Configure Environment Variables:
- Create a copy of `.env.example` and rename it to `.env`.
- Set the database credentials and other necessary variables in the .env file.


7. Apply migrations to set up the database:
```bash
python manage.py migrate
 ```

8. Create a Superuser:
```bash
python manage.py csu
 ```


### Running the Development Server

- Start the development server with:
```bash
python manage.py runserver
 ```

The project will be accessible at http://127.0.0.1:8000/.


### API Documentation

Explore the API documentation to understand available endpoints and data models. The documentation is generated using Swagger UI and ReDoc.

- **Swagger UI:** Visit [Swagger UI](http://127.0.0.1:8000/docs/) to interactively explore and test the API.

- **ReDoc:** For a more structured and readable view, check [ReDoc](http://127.0.0.1:8000/redoc/).

Note: Make sure the development server is running (`python manage.py runserver`) before accessing the API documentation.


### License
This project is licensed under the MIT License - see the LICENSE.md file for details.