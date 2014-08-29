"""
Requires data files to be in project root.
"""

from django.core.management.base import BaseCommand

import csv
from itertools import ifilter

from dariah_static_data.models import TADIRAHTechnique


class Command(BaseCommand):
    """Process a CSV file and add the data to a database table after emptying
    it first."""
    filename = 'tadirah_technique.csv'
    """
    Mapping Example::

        mapping = [('model_fieldname', required?),...]

    * Order is important!, should reflect the CSV file.
    * If a column will not be imported into the model use ``'_'`` for the
      ``model_name`` and ``0`` for ``required?``.
    """
    mapping = [('name', 1), ('uri', 1), ('_', 0)]
    model = TADIRAHTechnique
    delimiter = ';'
    quotechar = '|'

    @property
    def fieldnames(self):
        return map(lambda x: x[0], self.mapping)

    @property
    def name(self):
        """Name of the model, used for stdout information."""
        return self.model._meta.verbose_name.title()

    @property
    def help(self):
        return 'Import %s information from CSV file.' % self.name

    def handle(self, *args, **options):
        """Process a CSV file and add the data to a database table after
        emptying it first."""
        # Empty the database
        self.empty_database_table()
        # Open the CSV file
        self.stdout.write('Opening CSV...')
        with open(self.filename, 'rb') as csvfile:
            self.stdout.write('...done.')
            self.process_csv(csvfile)
        self.stdout.write('Successfully added all %s items to the database!' % self.name)

    def empty_database_table(self):
        """Empty the database table in question before populating it with the
        new values."""
        self.stdout.write('Removing all existing %s items...' % self.name)
        for c in self.model.objects.all():
            c.delete()
        self.stdout.write('...done!')

    def row_has_all_fields(self, row):
        """The row needs to have values for all mandatory fields in the model."""
        for f in self.mapping:
            if f[0] != '_' and f[1] and not row[f[0]]:
                return False
        return True

    def process_csv(self, csvfile):
        """Loop through the CSV file and add the data to the database."""
        reader = csv.DictReader(ifilter(lambda row: row[0] != '#', csvfile), delimiter=self.delimiter, quotechar=self.quotechar, fieldnames=self.fieldnames)
        # Write the items to the database
        self.stdout.write('Adding %s items to the database:' % self.name)
        for row in reader:
            # Check if row contains all necessary fields
            if self.row_has_all_fields(row):
                kwargs = {}
                # Fill up kwargs with attributes from row
                for f in filter(lambda x: x[0] != '_', self.mapping):  # Only use the ones that have a model_fieldname specified
                    if '_' in row[f[0]] and not f[0] == 'uri':
                        # If we're not dealing with an URI, replace all underscores with spaces
                        kwargs[f[0]] = row[f[0]].replace('_', ' ')
                    else:
                        # We ARE dealing with a URI
                        kwargs[f[0]] = row[f[0]]
                # Create and save the instance
                t = self.model(**kwargs)
                t.save()
                self.stdout.write('Successfully added %s %s.' % (self.name, t))
