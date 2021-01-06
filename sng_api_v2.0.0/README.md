# Server Name Generator Tool

The Server Name Generator (SNG) Tool creates 15 character hostnames based on a standard naming convention (e.g. NL4DWDPCMS1234). The tool stores hostnames, region ID, and service owner ID for traceability. 

For a complete list of values and functional mappings, please visit this page.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Block Diagram

<p align="center"> 
<img src="https://github.com/bmquiroz/sng/raw/master/sng_arch.png">
</p>

### Prerequisites

The following dependencies must be installed on the web server. 

```
- Python 3.7.0
- Gunicorn
- Nginx
- Python 2.7
- Supervisor
- Click 7.0
- Flask 1.0.2
- Flask-SQLAlchemy 2.3.2
- itsdangerous 1.1.0
- Jinja2 2.10
- MarkupSafe 1.1.0
- SQLAlchemy 1.2.14
- Werkzeug 0.14.1
```

### Directory Structure
```
/home/sng/sng_12
├── app
│   ├── hostnames.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── routes.py
│   ├── static
│   ├── templates
│   └── data.db
├── __pycache__
│   └── run.cpython-37.pyc
├── README.md
├── requirements.txt
├── run.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    ├── pip-selfcheck.json
    └── pyvenv.cfg
```

### Installation

Ensure all prerequisites are met before creating the directory structure. 

```
mkdir sng_v11
git clone repo
python3.7 -m venv venv
source bin/activate
pip install -r requirements.txt
...
```

## TODO

* Dockerize services and automate build through Compose or Puppet
* Redesign to fit Flask blueprint model
* Move SQLite to MySQL
* Enable OAuth for SSO integration
* Improve database table output, add ModelView for CRUD operations
* Add Flask-API

## Contributing

WIP

## Versioning

WIP

## Authors

* **Boris Quiroz** - *Initial work*
