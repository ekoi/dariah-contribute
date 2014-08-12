import os
import contributions
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
    name='contributions',
    version=contributions.__version__,
    author='DANS',
    author_email='info@dans.knaw.nl',
    description='Contribute portal for the Dariah project.',
    long_description=README,
    url='http://',
    license='',
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
    scripts=['manage.py', 'contributions/wsgi.py', ],
    include_package_data=True,
    install_requires=get_install_requires(REQUIREMENTS),
    dependency_links=get_dependency_links(REQUIREMENTS),
)
