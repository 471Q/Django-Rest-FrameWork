# DRF

Sample API in Django
To run the tests in this project copy the command ('coverage' library is used for unit testing):

coverage run --omit='_/venv/_' manage.py test (this will exclude the venv folder, and run any test available in other folders)

To list all inventory available:
http://127.0.0.1:8000/inventory

To search by name
inventory names available now: smartphone, tablets. To search just insert the name of the inventory after http://127.0.0.1:8000/inventory/{name of the inventory}
http://127.0.0.1:8000/inventory/smartphone/
