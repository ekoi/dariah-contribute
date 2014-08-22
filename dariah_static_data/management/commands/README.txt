Usage of manager commands
=========================

Prerequisites
-------------

Make sure the CSV files are in the root project folder (only place them there
temporarily).

Apply this in Vim to any offending CSV files::

    :set ff=unix                        # Set the filetype to Unix
    :write ++enc=utf-8 russian.txt      # Set the encoding format to UTF-8
    :%s/\r/\r/g                         # Replace all MS line-endings with Unix line-endings
    :%s/Ó/"/g                           # Replace all crazy &rdquo; characters with "
    :%s/Ò/"/g                           # Replace all crazy &ldquo; characters with "
    :%s/Õ/'/g                           # Replace all crazy &lsquo; characters with '
    :%s/;"/;|"/g                        # Start text elements with crazy characters with | (works only if last element on row)
    :%s/\n/|\r/g                        # End text elements with crazy characters with | (works only if last element on row)

Execution
---------

Use the following commands to import the data::

    ./manage.py import_tadirah_activity
    ./manage.py import_tadirah_object
    ./manage.py import_tadirah_technique
    ./manage.py import_tadirah_vcc
    ./manage.py import_geonames_countries


.. TODO:: Add arguments/options to the commands so you can specify the path/URL
of the data, empty or not empty the database tables.

.. TODO:: Add update data functionality. If you replace the data the primary
keys might no longer actually contain the same data and your whole database
(foreign keys, etc...) becomes corrupt.
