# django-startapp-template

This is a template for a Django app. It contains a basic Django app with customs files and folders.

## Usage

In your Django project to create a custom app, run the following command:

```shell
django-admin startapp --template=https://github.com/bepatient-fr/django-startapp-template/archive/main.zip  app_name
```

If you want to use a specific branch, you can use the following command:

```shell
django-admin startapp --template=https://github.com/bepatient-fr/django-startapp-template/archive/branche_name.zip  app_name
```

## Issues

We can't exclude files Readme and .gitignore from the template. 
So, if you want to remove a file, you have to remove it manually.
