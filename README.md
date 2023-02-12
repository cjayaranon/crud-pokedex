# crud-pokedex
A Pokedex with CRUD functions; uses a version of PokeAPI.

## Before anything else
These must be satisfied first before going to the next step
1. Python == 3.11.2
2. virtualenv == 20.19.0
3. virtualenvwrapper-win == 1.2.7
4. npm == 9.3.1

## Cloning instructions
1. On your terminal navigate to your desired folder location
2. Setup virtualenvwrapper using `mkvirtualenv -a "<folder_location>" <env_name>`
3. Clone this repo using `git clone <https_link>`. Make sure you use the **master** branch.
4. Change directory to `/crud-pokedex/dexapoke` where **requirements.txt** is.
5. Run `pip install -r requirements.txt`.
6. Go to `/crud-pokedex/dexapoke/frontend/static` and run `npm install`.
7. Go back to `/crud-pokedex/dexapoke` where `manage.py` is, and run `collectstatic`.
8. Afterwards, do not forget to run `makemigrations` and `migrate`.

## Populating the Database
Run `python manage.py import_from_pokeapi`
This will use <https://pokeapi.co> as its source.[^1]
[^1]: InsecureRequestWarning will be raised due to unverified HTTPS requests without verified SSL certificates. These are perfectly fine for beta purposes.

Home address is 'localhost:8000'