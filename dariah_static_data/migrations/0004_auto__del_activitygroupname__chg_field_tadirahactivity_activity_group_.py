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

from django.db.utils import OperationalError

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ActivityGroupName'
        db.delete_table(u'dariah_static_data_activitygroupname')


        # Renaming column for 'TADIRAHActivity.activity_group_name' to match new field type.
        db.rename_column(u'dariah_static_data_tadirahactivity', 'activity_group_name_id', 'activity_group_name')
        # Changing field 'TADIRAHActivity.activity_group_name'
        db.alter_column(u'dariah_static_data_tadirahactivity', 'activity_group_name', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Removing index on 'TADIRAHActivity', fields ['activity_group_name']
        try:
            db.delete_index(u'dariah_static_data_tadirahactivity', ['activity_group_name_id'])
        except OperationalError:
            pass


    def backwards(self, orm):
        # Adding index on 'TADIRAHActivity', fields ['activity_group_name']
        db.create_index(u'dariah_static_data_tadirahactivity', ['activity_group_name_id'])

        # Adding model 'ActivityGroupName'
        db.create_table(u'dariah_static_data_activitygroupname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'dariah_static_data', ['ActivityGroupName'])


        # Renaming column for 'TADIRAHActivity.activity_group_name' to match new field type.
        db.rename_column(u'dariah_static_data_tadirahactivity', 'activity_group_name', 'activity_group_name_id')
        # Changing field 'TADIRAHActivity.activity_group_name'
        db.alter_column(u'dariah_static_data_tadirahactivity', 'activity_group_name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dariah_static_data.ActivityGroupName']))

    models = {
        u'dariah_static_data.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'geonameid': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dariah_static_data.tadirahactivity': {
            'Meta': {'object_name': 'TADIRAHActivity'},
            'activity_group_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dariah_static_data']
