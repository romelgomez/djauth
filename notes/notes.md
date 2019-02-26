# NOTES

## Auth Transition

Test credentials
user: romel
password: aA123456-

## allauth signals

https://django-allauth.readthedocs.io/en/latest/signals.html

estas señales simplifican una de las direcciones (edited)
es decir, usuarios que se loggean o registran por sistema actual tambien lo hagan en el sistema firebase
luego quedaria la otra parte
los que lo hagan en firebase que tb modifiquen sistema actual

## sketches

```text
si cada segundo hay un nuevo usuario...

    user
        password
        email

middleware python django

[stage-1]
    django auth

[stage-2]
    django auth
    firebase auth

[stage-3]
    firebase auth

Django
    auth
        database

    USER -> [CRUD-AUTH] -> Database

        Signals  >>

firebase
    api
        auth

dijango 1.11
```