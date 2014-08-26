======
README
======

-------------
Documentation
-------------

This is a summary of the official documentation. It is highly recommended that you read the official documentation as it is more likely to be accurate and up-to-date. You can find it in the ``docs`` folder and you can build it using `Sphinx <http://sphinx-doc.org/>`_ (``make html``).


-------------------
Quick install guide
-------------------

#. Use virtualenv;
#. ``pip install contributions-{version no}.tar.gz`` or ``pip install --upgrade contributions-{version no}.tar.gz``;
#. In ``{virtualenv folder}/dariah-contribute/lib/python{versionno.}/site-packages/contributions/settings/`` copy ``local.py.default`` to ``local.py`` and adjust the settings to the server configuration. Note: pay attention to the commented out ``# MAINTENANCE_MODE = False``. The default is set to true and means you WILL get 503 errors. This setting is used for when users are not allowed to log in due to maintenance;
#. ``manage.py collectstatic`` (always);
#. ``manage.py syncdb`` (on new install);
#. ``manage.py migrate`` (always).

.. Note:: the Dariah Contribute application currently uses SQLite.

-----------------------
Production installation
-----------------------

#. Clone the Dariah Contribute Git repository locally: ``git clone {your username}@develop.dans.knaw.nl:/development/git/blessed/project/dariah-contributions.git``;
#. Checkout a specific version by checking out a tag with the version name ``git checkout [tagname]``;
#. Build the Python Egg from the repository: ``python setup.py sdist``;
#. Copy the Egg to the server using ``scp``;
#. On the live server make sure you have pip installed: follow the `pip Docs <http://www.pip-installer.org/en/latest/installing.html>`_, and you will also have to have some other packages installed, so run the following to install everything on a Redhat system:

   .. code-block:: sh

      foo@bar:~$ sudo yum install python-devel zlib-devel* libjpeg-devel* freetype-devel* python-pip gcc
      foo@bar:~$ sudo pip install virtualenv virtualenvwrapper

#. You've just installed ``virtualenv`` and ``virtualenvwrapper`` and so you should configure your virtualenv folder by adding the following to your ``.bashrc`` and resourcing ``.bashrc`` by doing ``. ~/.bashrc``:

   .. code:: sh

      export PIP_REQUIRE_VIRTUALENV=true
      export PIP_RESPECT_VIRTUALENV=true
      export WORKON_HOME=/opt/django
      source /usr/local/bin/virtualenvwrapper.sh

#. Run ``mkvirtualenv dariah-contribute``;
#. You should be working on your virtualenv, if not run ``workon dariah-contribute``;
#. Run ``pip install contributions-{versionno.}.tar.gz``;
#. Make sure the ``local.py`` settings file is present in ``{virtualenv folder}/dariah-contribute/lib/python{versionno.}/site-packages/contributions/settings/`` and contains the right info (including the database settings);
#. ``manage.py syncdb`` to create the database and the superuser;
#. Then ``manage.py migrate``;
#. Run ``manage.py collectstatic``;
#. Let IA set up Apache;
#. When you're done take the project out of maintenance mode by adding ``MAINTENANCE_MODE = False`` to the ``local.py`` settings file (and restarting the Apache server).

----------------------------------
Local installation for development
----------------------------------

Follow the same steps as the Live Installation, but instead of checking out a specific tag you can just keep to the master branch and you probably want to clone it from ``git clone {your username}@develop.dans.knaw.nl:/home/heleens/git/project/dariah-contributions.git``. You should also not create a Python Egg from the repository, but instead you can install all the requirements using ``pip install -r requirements.pip``. You can now run the server using ``./manage.py runserver``. You probably don't want to use Apache or cron, you will need to create the database.
