# web-scraper
A simple web app that use web scraping technique to get tech news. 

## Quick Start

### Requirements

- [__Python >= 3__](https://www.python.org/downloads/) and `pip`

### Basics

Create and activate a virtualenv

```sh
$ sudo pip install virtualenv # if not installed
$ virtualenv env
$ source env/bin/activate
```

Install the required packages

```sh
$ pip install -r requirements.txt
```

### Get news

```sh
$ python manage.py capturar_noticias
```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:8000/](http://localhost:8000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```
