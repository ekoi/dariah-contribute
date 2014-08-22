"""
Apply this in Vim to any offending CSV files::

    :set ff=unix                        # Set the filetype to Unix
    :write ++enc=utf-8 russian.txt      # Set the encoding format to UTF-8
    :%s/\r/\r/g                         # Replace all MS line-endings with Unix line-endings
    :%s/Ó/"/g                           # Replace all crazy &rdquo; characters with "
    :%s/Ò/"/g                           # Replace all crazy &ldquo; characters with "
    :%s/Õ/'/g                           # Replace all crazy &lsquo; characters with '
    :%s/;"/;|"/g                        # Start text elements with crazy characters with | (works only if last element on row)
    :%s/\n/|\r/g                        # End text elements with crazy characters with | (works only if last element on row)
"""
