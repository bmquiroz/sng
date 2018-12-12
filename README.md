# Server Name Generator Tool

The Server Name Generator (SNG) Tool allows you to create 15 character host names based on the Aon standard naming convention (e.g. NL4DWDPCMS1234). 

For a complete list of values and functional mappings, please visit this page.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Block Diagram



### Prerequisites

The following dependencies must be installed on the Ansible workstation that will be used to deploy swarm clusters. 

```
- Python 3.7.0
- Gunicorn
- Nginx
- Python 2.7
- Supervisor
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
│   └── test.db
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
git clone ssh://git@bitbucket.gxicloud.com:7999/foun/foundry_automations.git
ansible-playbook site.yml -e "lifecycle=qa cluster=02"
```
Parameters passed to playbooks are `lifecycle` which represents the environment you are deploying to and `cluster` which represents the cluster.

## Contributing

WIP

## Versioning

WIP

## Authors

* **Boris Quiroz** - *Initial work*
