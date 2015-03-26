# -*- coding: utf-8 -*-
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

        # Adding model 'TADIRAHActivity'
        db.create_table(u'dariah_static_data_tadirahactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity_group_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('activity_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHActivity'])

        # Adding model 'TADIRAHObject'
        db.create_table(u'dariah_static_data_tadirahobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHObject'])

        # Adding model 'TADIRAHVCC'
        db.create_table(u'dariah_static_data_tadirahvcc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal(u'dariah_static_data', ['TADIRAHVCC'])

        # Adding model 'Discipline'
        db.create_table(u'dariah_static_data_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=255)),
        ))
        db.send_create_signal(u'dariah_static_data', ['Discipline'])

        # Adding model 'Country'
        db.create_table(u'dariah_static_data_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('geonameid', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'dariah_static_data', ['Country'])


    def backwards(self, orm):
        # Deleting model 'TADIRAHTechnique'
        db.delete_table(u'dariah_static_data_tadirahtechnique')

        # Deleting model 'TADIRAHActivity'
        db.delete_table(u'dariah_static_data_tadirahactivity')

        # Deleting model 'TADIRAHObject'
        db.delete_table(u'dariah_static_data_tadirahobject')

        # Deleting model 'TADIRAHVCC'
        db.delete_table(u'dariah_static_data_tadirahvcc')

        # Deleting model 'Discipline'
        db.delete_table(u'dariah_static_data_discipline')

        # Deleting model 'Country'
        db.delete_table(u'dariah_static_data_country')


    models = {
        u'dariah_static_data.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'geonameid': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dariah_static_data.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
        u'dariah_static_data.tadirahvcc': {
            'Meta': {'object_name': 'TADIRAHVCC'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dariah_static_data']