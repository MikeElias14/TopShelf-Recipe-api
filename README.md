# TopShelf-Recipe-api

Recipes api for the TopShelf app.

### For DB Migrations:
##### From ./models:
Update `model.py` with the changes to the model, then run:
```
$ python model.py db migrate
```
After you have checked that the SQLAlchemy  migrate script is correct, run:
```
$ python model.py db upgrade
```

The default list of glassware, ingredients, and tags is stored in `recipes_defaults.py`.
To import these defaults run:
```
$ python recipes_defaults.py
```