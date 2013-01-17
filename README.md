# MITIMES

Django/tastypie REST Stack with Fabric remote deploy and gunicorn goodness

## PREPARE

Download the tarbal or clone the repository to your workspace

    $ git clone git://github.com/tezro/mitimes.git

Ensure that you have the Fabric library installed

    $ pip install Fabric

Edit the Fabric settings.py, used by our homebrew fabfile to reflect your remote server and prefered configuration

```python
FABRIC = {
    'HOSTS': ['localhost'],
    'SSH_USER': 'ubuntu',
    'SSH_PASS': 'aaa',
    'DB_PASS' : 'aaa',
    'ADMIN_PASS' : 'aaa',
    'REPO_URL': 'git://github.com/tezro/mitimes.git',
    'PROJECT_NAME': 'mitimes',
}
```

## INSTALL

Install the remote server software

    $ fab install

The following software will be installed

 * nginx
 * libjpeg-dev
 * python-dev
 * python-setuptools
 * git-core
 * postgresql
 * libpq-dev
 * memcached
 * supervisor
 * pip
 * virtualenv
 * mercurial

## CREATE - virtual environment

    $ fab create

The following steps are executed

 * Create virtualenv
 * Create DB and DB user.
 * Set up SSL certificate.
 * Set up project.
 * Install additional libraries
  * gunicorn
  * setproctitle
  * psycopg2
  * django-compressor
  * python-memcached

## REMOVE

    $ fab remove

Drop the database and delete the virtual environment

## DEPLOY

    $ fab deploy

Make a snapshot backup, update remote source, migrate any db changes and start the services

## Test Success

After running deploy the server should be up and running listenig for request 

 * nginx with our self signed certificato on 443 
 * gunicorn on 8000


Authenticate against admin auth and establish a session at

    https://your.remote.host/admin

Explore your REST api nose to the floor from

    https://your.remote.host/api/v1/?format=json
    
Which will produce you a hypermedia list of the api endpoints available

```json
{
  "activity": {
    "list_endpoint": "/api/v1/activity/",
    "schema": "/api/v1/activity/schema/"
  },
  "client": {
    "list_endpoint": "/api/v1/client/",
    "schema": "/api/v1/client/schema/"
  },
  "contact": {
    "list_endpoint": "/api/v1/contact/",
    "schema": "/api/v1/contact/schema/"
  },
  "contactemail": {
    "list_endpoint": "/api/v1/contactemail/",
    "schema": "/api/v1/contactemail/schema/"
  },
  "matter": {
    "list_endpoint": "/api/v1/matter/",
    "schema": "/api/v1/matter/schema/"
  }
}
```

## RESTART

    $ fab restart

Start/Stop Toggle the running state of the server services,
* if running do kill hup
* else start

## ROLLBACK

    $ fab rollback

Reapply snapshot backup from last deploy.

