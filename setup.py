"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contribss.

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

import os
import dariah_inkind_contribs
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
REQUIREMENTS_FILE = open(os.path.join(os.path.dirname(__file__), 'requirements.pip'))
REQUIREMENTS = [l.strip() for l in REQUIREMENTS_FILE]

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_install_requires(pip_requirements):
    l = []
    for x in pip_requirements:
        if not 'https://' in x:
            l.append(x)
        else:
            y = x.partition('egg=')[2]
            i = y.rsplit('-', 1)
            l.append("%s<=%s" % (i[0], i[1]))
    return l


def get_dependency_links(pip_requirements):
    return [x for x in pip_requirements if 'https://' in x]


setup(
    name='dariah-contribute',
    version=dariah_inkind_contribs.__version__,
    author='DANS',
    author_email='info@dans.knaw.nl',
    description='Contribute portal for the Dariah project.',
    long_description=README,
    url='http://dariah-contribute.dans.knaw.nl',
    license='Apache License, Version 2.0',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(),
    scripts=['manage.py', 'dariah_inkind_contribs/wsgi.py', ],
    include_package_data=True,
    install_requires=get_install_requires(REQUIREMENTS),
    dependency_links=get_dependency_links(REQUIREMENTS),
)
