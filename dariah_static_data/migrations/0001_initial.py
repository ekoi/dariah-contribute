# -*- coding: utf-8 -*-
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

from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TADIRAHTechnique'
        db.create_table(u'dariah_static_data_tadirahtechnique', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHTechnique'])

        # Adding model 'RelatedActivity'
        db.create_table(u'dariah_static_data_relatedactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tadirah_technique', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_activities', to=orm['dariah_static_data.TADIRAHTechnique'])),
        ))
        db.send_create_signal(u'dariah_static_data', ['RelatedActivity'])

        # Adding model 'TADIRAHActivity'
        db.create_table(u'dariah_static_data_tadirahactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity_group_name', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tadirah_activities', to=orm['dariah_static_data.ActivityGroupName'])),
            ('activity_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHActivity'])

        # Adding model 'ActivityGroupName'
        db.create_table(u'dariah_static_data_activitygroupname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'dariah_static_data', ['ActivityGroupName'])

        # Adding model 'TADIRAHObject'
        db.create_table(u'dariah_static_data_tadirahobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHObject'])

        # Adding model 'VCC'
        db.create_table(u'dariah_static_data_vcc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dariah_static_data', ['VCC'])

        # Adding model 'Country'
        db.create_table(u'dariah_static_data_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('iso3166_2', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'dariah_static_data', ['Country'])


    def backwards(self, orm):
        # Deleting model 'TADIRAHTechnique'
        db.delete_table(u'dariah_static_data_tadirahtechnique')

        # Deleting model 'RelatedActivity'
        db.delete_table(u'dariah_static_data_relatedactivity')

        # Deleting model 'TADIRAHActivity'
        db.delete_table(u'dariah_static_data_tadirahactivity')

        # Deleting model 'ActivityGroupName'
        db.delete_table(u'dariah_static_data_activitygroupname')

        # Deleting model 'TADIRAHObject'
        db.delete_table(u'dariah_static_data_tadirahobject')

        # Deleting model 'VCC'
        db.delete_table(u'dariah_static_data_vcc')

        # Deleting model 'Country'
        db.delete_table(u'dariah_static_data_country')


    models = {
        u'dariah_static_data.activitygroupname': {
            'Meta': {'object_name': 'ActivityGroupName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dariah_static_data.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso3166_2': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dariah_static_data.relatedactivity': {
            'Meta': {'object_name': 'RelatedActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tadirah_technique': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_activities'", 'to': u"orm['dariah_static_data.TADIRAHTechnique']"}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dariah_static_data.tadirahactivity': {
            'Meta': {'object_name': 'TADIRAHActivity'},
            'activity_group_name': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tadirah_activities'", 'to': u"orm['dariah_static_data.ActivityGroupName']"}),
            'activity_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dariah_static_data.tadirahobject': {
            'Meta': {'object_name': 'TADIRAHObject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dariah_static_data.tadirahtechnique': {
            'Meta': {'object_name': 'TADIRAHTechnique'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'dariah_static_data.vcc': {
            'Meta': {'object_name': 'VCC'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dariah_static_data']