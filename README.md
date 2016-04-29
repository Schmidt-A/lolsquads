LoL Squads
==========

Requirements
------------

 - django 1.9
 - postgresql >= 9.4
 - django postgresql contrib
 - psycopg2

    ```sudo pip install django django-contrib-postgres psycopg2```

Setup
-----

Postgresql database:

```
sudo  su - postgres
createdb lolsquads
createuser lolsquads
echo "GRANT ALL PRIVILEGES ON DATABASE lolsquads TO lolsquads;" | psql
```


