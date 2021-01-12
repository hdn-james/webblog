# CS300_WebBlog

**Create a new virtual environment (optional):**
<br />
- From the root folder, run this command:
```
python -m venv venv
```
- Activate it (on windows):
```
venv\Scripts\activate.bat
```
- Activate it (on linux or mac):
```
source venv/bin/activate
```
<br />

**Run django web app:**
<br />
- install all dependencies:
```
pip install -r requirements.txt
```
- config database info in `cs300_webblog.config.local`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': <your database name>,
        'HOST': <your database host name>,
        'USER': <your database user name>,
        'PASSWORD': <your database password>,
    }
}
```
- run local web app _**(from root folder of the project)**_:
```
python manage.py runserver 0.0.0.0:8000 --settings=cs300_webblog.config.local
```

- run test _**(from root folder of the project)**_:
```
python manage.py test --settings=cs300_webblog.config.test
```
<br />
