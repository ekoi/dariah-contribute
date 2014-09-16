"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.

    Copyright 2014 Data Archiving and Networked Services

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from django.core.management.base import BaseCommand

import urllib2
import csv
from itertools import ifilter

from dariah_static_data.models import Country


class Command(BaseCommand):
    help = 'Imports country information from the Geonames countryInfo.txt file.'
    url = 'http://download.geonames.org/export/dump/countryInfo.txt'
    fieldnames = ['ISO', 'ISO3', 'ISO-Numeric', 'fips', 'Country', 'Capital', 'Area(in sq km)', 'Population', 'Continent', 'tld', 'CurrencyCode', 'CurrencyName', 'Phone', 'Postal Code Format', 'Postal Code Regex', 'Languages', 'geonameid', 'neighbours', 'EquivalentFipsCode']

    def handle(self, *args, **options):

        # Empty the database
        self.empty_country_database()
        # Open the remote Geonames file
        self.cr = self.open_geonames_file()
        # Write the countries to the database
        self.save_countries_to_database()

    def empty_country_database(self):
        self.stdout.write('Removing all existing countries...')
        for c in Country.objects.all():
            c.delete()
        self.stdout.write('...done!')

    def open_geonames_file(self):
        self.stdout.write('Opening Geonames countryInfo.txt file...')
        response = urllib2.urlopen(self.url)
        self.stdout.write('...done!')
        return csv.DictReader(ifilter(lambda row: row[0] != '#', response), delimiter='\t', fieldnames=self.fieldnames)

    def save_countries_to_database(self):
        self.stdout.write('Adding countries to the database:')
        for row in self.cr:
            if row['geonameid'] and row['Country']:
                country = Country(name=row['Country'], geonameid=int(row['geonameid']), iso=row['ISO'])
                country.save()
                self.stdout.write('Successfully added country %s.' % country)
        self.stdout.write('Successfully added all countries to the database!')
