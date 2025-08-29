### Create python virtual environment###
python -m venv  env_name
### Install Packages ###
pip dagster dagster-embdedded-elt 
### Create an Empty Dagster Project ###
cd Dagster_ETL_Rest
dagster project scaffold --name rest_api_postgres

### Run the Flask App ###
In one terminal run the App
flask --app app run
http://localhost:5000
###  APIs can be found at this link ###
http://localhost:5000/getcustomerdata
### Run Dagster Server ###
cd rest_api_postgres
dagster dev
This runs dagster on dev environment
Hit http://localhost:3000 to have a look at the Assets and Run them to orchestrate the process of loading data into postgres.

