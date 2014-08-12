======
README
======

-------------
Documentation
-------------

This is a summary of the official documentation. It is highly recommended that you read the official documentation as it is more likely to be accurate and up-to-date. You can find it in the ``docs`` folder and you can build it using `Sphinx <http://sphinx-doc.org/>`_ (``make html``).

-----------------
Notes / Debugging
-----------------

* ``mod_wsgi`` should be installed and loaded (don't forget Apache restart);
* The server should have access to MySQL01.dans.knaw.nl on port 3306.
* ``heleens`` folder should be executable for group and other (``chmod +x /home/heleens``);
* if you're using a specific port number, make sure it is open in SELinux;
* if you get a server 500 error without any errors in the logging, make sure the ``ALLOWED_HOSTS`` setting in your Django settings contains the host from which you're trying to load the website;
* BACKUP the old database!

-----------------------
Production installation
-----------------------

#. Clone the DSA Git repository locally: ``git clone {your username}@develop01.dans.knaw.nl:/development/git/blessed/heleens/dsatool.git``;
#. Checkout a specific version by checking out a tag with the version name ``git checkout [tagname]``;
#. Build the Python Egg from the repository: ``python setup.py sdist``;
#. Copy the Egg to the server using ``scp``;
#. On the live server make sure you have pip installed: follow the `pip Docs <http://www.pip-installer.org/en/latest/installing.html>`_, and you will also have to have some other packages installed, so run the following to install everything on a Redhat system:

   .. code-block:: sh

      foo@bar:~$ sudo yum install python-devel mysql-devel* zlib-devel* libjpeg-devel* freetype-devel* python-pip gcc
      foo@bar:~$ sudo pip install virtualenv virtualenvwrapper

#. You've just installed ``virtualenv`` and ``virtualenvwrapper`` and so you should configure your virtualenv folder by adding the following to your ``.bashrc`` and resourcing ``.bashrc`` by doing ``. ~/.bashrc``:

   .. code:: sh

      export PIP_REQUIRE_VIRTUALENV=true
      export PIP_RESPECT_VIRTUALENV=true
      export WORKON_HOME=/Volumes/DATA/virtualenvs
      source /usr/local/bin/virtualenvwrapper.sh

#. Run ``mkvirtualenv dsatool``;
#. You should be working on your virtualenv, if not run ``workon dsatool``;
#. Run ``pip install dsatool-{versionno.}.tar.gz``;
#. Setup the database;
   #. ``mysql -u root -p``
   #. ``create database dsadb;``
   #. ``grant all privileges on dsadb.* to 'dsauser'@'localhost' identified by 'password';``
   #. ``exit;``
   #. Restore the database: ``mysql -u root -p dsadb < {your-dsa-db-backup}.sql``
   #. Run ``manage.py syncdb``;
   #. Fake migrate ``assessment_data``, ``contact_data``, ``content``, ``dsa_data`` and ``notifications`` apps: ``manage.py migrate [app] 0001 --fake``;
   #. Then ``manage.py migrate``;
#. Make sure the ``local.py`` settings file is present in ``{virtualenv folder}/dsatool/lib/python{versionno.}/site-packages/dsatool/settings/`` and contains the right info (including the database settings);
#. Run ``manage.py collectstatic``;
#. Setup cron by adding a file with the following contents to ``/etc/cron.hourly/``:

   .. code-block:: sh

      #!/bin/bash
      /home/[username]/virtualenvs/dsatool/bin/python /home/[username]/virtualenvs/dsatool/bin/manage.py runcrons

#. Setup Apache.
#. When you're done take the project out of maintenance mode by adding ``MAINTENANCE_MODE = False`` to the ``local.py`` settings file (and restarting the Apache server).

----------------------------------
Local installation for development
----------------------------------

Follow the same steps as the Live Installation, but instead of checking out a specific tag you can just keep to the master branch and you probably want to clone it from ``git clone {your username}@develop01.dans.knaw.nl:/development/git/dev-public/heleens/dsatool.git``. You should also not create a Python Egg from the repository, but instead you can install all the requirements using ``pip install -r requirements.pip``. You can now run the server using ``./manage.py runserver``. You probably don't want to use Apache or cron.
