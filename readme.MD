# Overview
This Python script loops through a YAML file and updates Prisma Access Decryption Exclusions


## Creating a service account in Prisma Access

You will need to create a service account in Prisma Access to generate the access token.

The Client ID, Secret ID, and TSG ID will be saved in the .env file.

To create a service account: https://pan.dev/sase/docs/service-accounts/


## Installing and running

Clone down this repo and cd into the directory.

Create a Python virtual environment: python -m venv venv

Activate the virtual environment: \
Windows: .\venv\Scripts\activate \
OSX: source venv/bin/activate \

Install the dependencies using `pip install -r requirements.txt`

Rename `.env.example` to `.env` and populate your variables in this file generated while creating the service account. The .env is included in the .gitignore to ensure it does not accidentally get checked into a git repo.

Run: `python main.py`

The output will be displayed to the screen.
