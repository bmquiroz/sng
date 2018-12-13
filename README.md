# Server Name Generator Tool

The Server Name Generator (SNG) Tool creates a 15 character hostname based on the Aon standard naming convention (e.g. NL4DWDPCMS1234). The tool stores hostnames, region ID, and service owner ID for traceability. 

For a complete list of values and functional mappings, please visit this page.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Block Diagram

<p align="center"> 
<img src="https://github.com/bmquiroz/sng/raw/master/sng_arch.png">
</p>

### Prerequisites

The following dependencies must be installed on the Ansible workstation that will be used to deploy swarm clusters. 

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

Ensure all prerequisites are met. Update playbook parameters. Navigate to `/aws-provision` and execute play:

```
mkdir sng_v11
git clone ssh://git@bitbucket.gxicloud.com:7999/foun/foundry_automations.git
cd /home/sng/sng_v11
python3.7 -m venv venv
source bin/activate
pip install -r requirements.txt
```
Parameters passed to playbooks are `lifecycle` which represents the environment you are deploying to and `cluster` which represents the cluster.

## TODO

* Dockerize services and automate build through Compose or Puppet
* Redesign to fit Flask blueprint model
* Move SQLite to MySQL
* Enable OAuth for SSO integration

## Contributing

WIP

## Versioning

WIP

## Authors

* **Boris Quiroz** - *Initial work*
