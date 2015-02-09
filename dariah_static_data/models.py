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

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TADIRAHTechnique(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255)
    uri = models.URLField(
        _('uri'))

    class Meta:
        verbose_name = _('TADIRAH Technique')
        verbose_name_plural = _('TADIRAH Techniques')

    def __unicode__(self):
        return self.name


class TADIRAHActivity(models.Model):
    activity_group_name = models.CharField(
        _('activity group name'),
        max_length=255)
    activity_name = models.CharField(
        _('activity name'),
        max_length=255,
        blank=True)
    uri = models.URLField(
        _('uri'))
    description = models.TextField(
        _('description'))

    class Meta:
        verbose_name = _('TADIRAH Activity')
        verbose_name_plural = _('TADIRAH Activities')

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return "{group_name} {activity_name}".format(group_name=self.activity_group_name,
                                                     activity_name=self.activity_name)


class TADIRAHObject(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255)
    uri = models.URLField(
        _('uri'))

    class Meta:
        verbose_name = _('TADIRAH Object')
        verbose_name_plural = _('TADIRAH Objects')

    def __unicode__(self):
        return self.name


class TADIRAHVCC(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255)
    uri = models.URLField(
        _('uri'))
    description = models.TextField(
        _('description'),
        max_length=255)

    class Meta:
        verbose_name = _('TADIRAH VCC')
#         verbose_name_plural = _('TADIRAH VCC')

    def __unicode__(self):
        return "{name} - {description}".format(name=self.name,
                                               description=self.description)
    

class Discipline(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255)
    uri = models.URLField(
        _('uri'))
    description = models.TextField(
        _('description'),
        max_length=255)

    class Meta:
        verbose_name = _('Discipline')
        verbose_name_plural = _('Disciplines')

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        _('name'),
        max_length=255)
    iso = models.CharField(
        _('ISO Country Code'),
        max_length=2)
    geonameid = models.PositiveIntegerField(
        _('geoname id'))

    class Meta:
        verbose_name = _('geonames Country')
        verbose_name_plural = _('geonames Countries')
        ordering = ['name', ]

    def __unicode__(self):
        return self.name

    @property
    def uri(self):
        return "http://sws.geonames.org/{geonameid}/about.rdf".format(geonameid=self.geonameid)
