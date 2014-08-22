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
    fieldnames = ['name', 'uri', 'related_activity']  # Order is important!, should reflect the CSV file.
    mapping = [('name', 'name', 1), ('uri', 'uri', 1)]  # [('model_fieldname', 'csv_fieldname', required?),...], omit fields that are not in the model
    model = TADIRAHTechnique

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
            if f[2] and not row[f[1]]:
                return False
        return True

    def process_csv(self, csvfile):
        """Loop through the CSV file and add the data to the database."""
        reader = csv.DictReader(ifilter(lambda row: row[0] != '#', csvfile), delimiter=";", quotechar="|", fieldnames=self.fieldnames)
        # Write the items to the database
        self.stdout.write('Adding %s items to the database:' % self.name)
        for row in reader:
            # Check if row contains all necessary fields
            if self.row_has_all_fields(row):
                kwargs = {}
                for f in self.mapping:
                    if '_' in row[f[1]] and not f[0] == 'uri':
                        # If we're not dealing with an URI, replace all underscores with spaces
                        kwargs[f[0]] = row[f[1]].replace('_', ' ')
                    else:
                        # We ARE dealing with a URI
                        kwargs[f[0]] = row[f[1]]
                t = self.model(**kwargs)
                t.save()
                self.stdout.write('Successfully added %s %s.' % (self.name, t))
