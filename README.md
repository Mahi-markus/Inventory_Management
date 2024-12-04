# Property Management System

This repository contains the **Property Management System**, a Django-based application designed to manage property information using geospatial data with PostgreSQL and PostGIS. The project includes a robust backend with an admin interface for managing properties, user permissions, and a public-facing sign-up page for property owners.

## Features

- **Geospatial Data Handling**: Utilizes PostGIS for location management.
- **Django Admin Interface**: User-friendly admin dashboard for property management.
- **Role-Based Access Control**: Permissions for property owners to manage their properties.
- **Localization Support**: Multilingual descriptions and policies for properties.
- **Sitemap Generator**: Command-line tool to generate a sitemap for all locations.
- **Public Sign-Up**: A dedicated page for property owner registration.

## Installation

### Prerequisites

Ensure the following software is installed:

- **Python 3.8+**
- **PostgreSQL** with the **PostGIS extension**
- **Node.js** (optional, for additional frontend setup)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mahi-markus/Inventory_Management.git
   ```
   ```bash
cd Inventory_Management
    ```
Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Dependencies
```bash
pip install -r requirements.txt
```
Set Up PostgreSQL and PostGIS
Install PostgreSQL and PostGIS.
Create a database:



Enable the PostGIS extension:



Configure Django Settings

Update the DATABASES configuration in settings.py:
```bash
   DATABASES = {
    'default': {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        'NAME': 'inventory_manage',         # The name of the database you created
        'USER': 'dummy',             # The username you defined
        'PASSWORD': 'dummy123',     # The password you defined
        'HOST': 'db',                 # Use the container name (db) as the hostname
        'PORT': '5432',               # The default PostgreSQL port
    }
}

```
Apply Migrations
```bash
docker exec -it inventory_manage-web-1 python manage.py makemigrations
```
```bash
docker exec -it inventory_manage-web-1 python manage.py migrate
```
Create a Superuser

docker exec -it inventory_manage-web-1 python manage.py createsuperuser

Run the Server
```bash
docker compose up --build
 ```

  ```bash
docker compose up
```
To stop 
```bash
docker compose down

```
Access the application at  http://localhost:8000.