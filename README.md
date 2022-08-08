#### RETAILER_APP REST API WITH JWT AUTH

### Terminal commands
Note: make sure you have `docker` installed.

To build: 

    docker image build -t anakin-assignment .

To run application: 

    docker compose up


Make sure to run the initial migration commands to update the database.
    
    > export FLASK_APP=manage.py    # required to use flask cli
    
    > flask db init

    > flask db migrate --message 'initial database migration'

    > flask db upgrade


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:3000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.

