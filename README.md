This repository contains Iqbal Fadhil's assignment for Katekima Backend Developer using Python Django.
Before running the code, please create a new virtual environment using the following command.

python3 -m venv virtualenvironment

Then, install the requirements in this directory using the following command.

pip3 install -r requirements.txt

------

The Assignment 1 contains LSFR code.
This assignment has 2 solutions.
First solution is lsfr_with_package.py. This file is the solution of creating LSFR using common package of LSFR on python named pylsfr.
Second solution is lsfr_without_package.py. This file is the solution of creating LSFR using python function only from scratch.
Both solution can be run by using this command on terminal.

python3 {filename}

for example

python3 lsfr_with_package.py

------

The Assignment 2 contains the REST API code using Django.
For testing purpose using Postman, collection Postman v2 and Postman v2.1 are provided on the Assignment 2 directory.
The database is provided using sqlite3. 
The project can be run right away using the following command

python3 manage.py runserver