======
README
======

DARIAH Contribute: contribute portal for the Dariah project.
This project has been built in `Python <https://www.python.org/>`_ using the
`Django framework <https://www.djangoproject.com/>`_.

-------------------
Quick install guide
-------------------

#. Use virtualenv;
#. ``pip install dariah-contribute-{version no}.tar.gz`` or ``pip install --upgrade dariah-contribute-{version no}.tar.gz``;
#. In ``{virtualenv folder}/dariah-contribute/lib/python{versionno.}/site-packages/dariah_contribute/settings/`` copy ``local.py.default`` to ``local.py`` and adjust the settings to the server configuration. Note: pay attention to the commented out ``# MAINTENANCE_MODE = False``. The default is set to true and means you WILL get 503 errors. This setting is used for when users are not allowed to log in due to maintenance;
#. ``manage.py collectstatic`` (always);
#. ``manage.py syncdb`` (on new install);
#. ``manage.py migrate`` (always);
#. Change directory to ``{virtualenv path}/lib/python{versionno.}/site-packages/dariah_static_data/skos_preflabels_data`` and execute the following commands (only on new install):

   .. code-block:: sh

      manage.py import_disciplines
      manage.py import_geonames_countries
      manage.py import_tadirah_activity
      manage.py import_tadirah_object
      manage.py import_tadirah_technique
      manage.py import_tadirah_vcc

.. Note:: the Dariah Contribute application currently uses SQLite.

-----------------------
Production installation
-----------------------

#. Clone the Dariah Contribute Git repository locally: ``git clone {path-to-repository-on-server}dariah-contribute.git``;
#. Checkout a specific version by checking out a tag with the version name ``git checkout [tagname]``;
#. Build the Python Egg from the repository: ``python setup.py sdist``;
#. Copy the Egg to the server using ``scp``;
#. On the live server make sure you have pip installed: follow the `pip Docs <http://www.pip-installer.org/en/latest/installing.html>`_, and you will also have to have some other packages installed, so run the following to install everything on a Redhat system:

   .. code-block:: sh

      sudo yum install python-devel zlib-devel* libjpeg-devel* freetype-devel* python-pip gcc
      sudo pip install virtualenv

#. Run ``virtualenv dariah-contribute``;
#. You should be working on your virtualenv, if not run ``source dariah-contribute/bin/activate``;
#. Run ``pip install dariah-contribute-{versionno.}.tar.gz``;
#. Make sure the ``local.py`` settings file is present in ``{virtualenv folder}/dariah-contribute/lib/python{versionno.}/site-packages/dariah_contribute/settings/`` and contains the right info (including the database settings);
#. ``manage.py syncdb`` to create the database and the superuser;
#. Then ``manage.py migrate``;
#. Run ``manage.py collectstatic``;
#. Let your IT departement set up Apache;
#. Change directory to ``{virtualenv path}/lib/python{versionno.}/site-packages/dariah_static_data/skos_preflabels_data`` and execute the following commands (only on new install):

   .. code-block:: sh

      manage.py import_disciplines
      manage.py import_geonames_countries
      manage.py import_tadirah_activity
      manage.py import_tadirah_object
      manage.py import_tadirah_technique
      manage.py import_tadirah_vcc

#. When you're done take the project out of maintenance mode by adding ``MAINTENANCE_MODE = False`` to the ``local.py`` settings file and restarting django by 'touching' ``{virtualenv folder}/dariah-contribute/bin/wsgi``.

----------------------------------
Local installation for development
----------------------------------

Do not create a Python Egg from the repository, but instead you can install all the requirements using ``pip install -r requirements.pip``. You can now run the server using ``./manage.py runserver``. You probably don't want to use Apache.
