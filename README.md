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

### Set Up a Virtual Environment

```bash
python -m venv .venv
.venv/Scripts/activate    #On windows
deactivate
```

```bash
python3 -m venv .venv
source .venv/bin/activate    #On linux
deactivate
```

### Run the Server

```bash
docker compose up --build
```

```bash
docker compose up
```

### To stop

```bash
docker compose down

```

Install Dependencies(onptional if Dependemcies do any unusual problem)

```bash
pip install -r requirements.txt
```

### Enable the PostGIS extension using the docker-compose.yml and Dockerfile.

### Configure Django Settings

Already Updated the DATABASES configuration in settings.py:

```bash

DATABASES = {
    'default': {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        'NAME': 'inventory_manage',         # The name of the database you created
        'USER': 'mahi',             # The username you defined
        'PASSWORD': 'mahi123',     # The password you defined
        'HOST': 'db',                 # Use the container name (db) as the hostname
        'PORT': '5432',               # The default PostgreSQL port
    }
}


```

### Apply Migrations

```bash
docker exec -it inventory_manage-web-1 python manage.py makemigrations
```

```bash
docker exec -it inventory_manage-web-1 python manage.py migrate
```

### Create a Superuser

```bash

docker exec -it inventory_manage-web-1 python manage.py createsuperuser
```

then put Username,Email and Password in order to create a super user.

```bash
for example:
Username: admin
email: admin@admin.com
Password:admin
and then type y to avoid Bypass password validation

```

### Property owner group creation

1. login accessing http://localhost:8000/admin as admin
2. click groups and give a name for example: property_owners
3. In permissions segment: select all the accomodation related permissions and then save.

## Create a normal user(steps):

1.  Access the application at http://localhost:8000
2.  Fill all the necessary fields in order to create property owner user.
3.  Then Click on the signup and then go to login or
4.  Access the login page by this url: http://localhost:8000/admin and then login as normal user.

## Giving persimision(as a admin) to normal usr to their see their own property and update

1. login as admin.
2. click on a normal user and Acitve,Staff Status both.
3. In groups select the property owners group
4. In user permission select all accomodation related permissions and save.

## normal user

1. After getting permission by admin a normal user can see his own accomomation and update,delete also.

### Importing location data

### Dummy Data example to for tables or models

### Sitemap generations nstruction

### Testing Instructions
