# SQLAlchemy, Pydantic and Linkml Testbed

If you want to use this testbed, you can set up your own by creating an app in our Dash Enterprise development server (dash-temp)

Once the app is created you need to go to the service tab and turn on Postgres
You will also need to turn on the persistent storage, and put a copy of the [ROR CSV database](https://zenodo.org/records/16950727) ../mount/ror/

Then you should install psql so you can easily look at the database table that get created.

```
sudo apt update && sudo apt upgrade
sudo apt install postgresql-client postgresql-client-common libpq-dev
```

 After installing psql, you can update your workspace with the required modules with:

```
pip install -r requirements.txt
```

Once psql is installed you can start it from a terminal with:

```
psql $DATABASE_URL
```

To create all of the database tables and the collection of example metadata using the hand-coded SQLAlchey model classes, run the following commands:

```
python ror_and_roles.py
python test.py
python test2.py
```

You can look at the relations created using psql on the command line as above and you can dump the resulting schema to a file with:

```
pg_dump --schema-only $DATABASE_URL
```

If you want to nuke all of the tables and data that was created from that scenario, you can run the following to SQL commands in psql

```
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```

To create all of the relations and fill them with the example data using the models produced by the linkml model classes, you can run the following commands.

```
python ror_and_roles_linkml.py
python test_linkml.py
python test2_linkml.py
```
The linkml model I used is in models/linkml/model.yaml

Linkml is installed so you can change the yaml and regenerate the SQLAlchemy classes if you want.

```
gen-sqla models/linkml/model.yaml
```