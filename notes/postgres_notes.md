# Postgres NOTES

## List of roles

`\du`

## List of databases

`\l`


## I forgot the password I entered during postgres installation

https://stackoverflow.com/questions/10845998/i-forgot-the-password-i-entered-during-postgres-installation

Steps::
    sudo cp /etc/postgresql/9.6/main/pg_hba.conf /etc/postgresql/9.6/main/pg_hba.conf-backup
    sudo nano /etc/postgresql/9.6/main/pg_hba.conf
    sudo /etc/init.d/postgresql restart
    psql -U postgres
    ALTER USER {role_name} with password 'my_secure_password';
    sudo cp /etc/postgresql/9.6/main/pg_hba.conf-backup /etc/postgresql/9.6/main/pg_hba.conf

## How To Use Roles and Manage Grant Permissions in PostgreSQL on a VPS

https://www.digitalocean.com/community/tutorials/how-to-use-roles-and-manage-grant-permissions-in-postgresql-on-a-vps--2

```text
Steps:
    psql -U postgres
    \du
    CREATE ROLE {new_role_name} 
    \h CREATE ROLE
    \du

    CREATE ROLE name [ [ WITH ] option [ ... ] ]

    where option can be:

        SUPERUSER | NOSUPERUSER
        | CREATEDB | NOCREATEDB
        | CREATEROLE | NOCREATEROLE
        | INHERIT | NOINHERIT
        | LOGIN | NOLOGIN
        | REPLICATION | NOREPLICATION
        | BYPASSRLS | NOBYPASSRLS
        | CONNECTION LIMIT connlimit
        | [ ENCRYPTED | UNENCRYPTED ] PASSWORD 'password'
        | VALID UNTIL 'timestamp'
        | IN ROLE role_name [, ...]
        | IN GROUP role_name [, ...]
        | ROLE role_name [, ...]
        | ADMIN role_name [, ...]
        | USER role_name [, ...]
        | SYSID uid
```

## Create data base demos

`CREATE DATABASE demo;`

## add permissions to user

```text
GRANT ALL PRIVILEGES ON DATABASE demo TO romelgomez;

-------- Rextie ---------
    Postgres Database
        rextie_db_dev
    Postgres Roles
        rextie_web_dev

DEFAULT DEV PASSWORD: 123456

export DATABASE_HOST='localhost'
export DATABASE_PORT='5432'
export DATABASE_NAME='demo'
export DATABASE_USER='romelgomez'
export DATABASE_PASSWORD='123456'
```

## Search Examples

```text
>>> from polls.models import Question, Choice

>>> Question.objects.all()
[<Question: What's up?>]

>>> Question.objects.filter(id=1)
[<Question: What's up?>]

>>> Question.objects.filter(question_text__startswith='What')
[<Question: What's up?>]
```
