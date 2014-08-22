# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Country.iso3166_2'
        db.delete_column(u'dariah_static_data_country', 'iso3166_2')

        # Deleting field 'Country.uri'
        db.delete_column(u'dariah_static_data_country', 'uri')

        # Adding field 'Country.geonameid'
        db.add_column(u'dariah_static_data_country', 'geonameid',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Country.iso3166_2'
        db.add_column(u'dariah_static_data_country', 'iso3166_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2),
                      keep_default=False)

        # Adding field 'Country.uri'
        db.add_column(u'dariah_static_data_country', 'uri',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Country.geonameid'
        db.delete_column(u'dariah_static_data_country', 'geonameid')


    models = {
        u'dariah_static_data.activitygroupname': {
            'Meta': {'object_name': 'ActivityGroupName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'dariah_static_data.country': {
            'Meta': {'object_name': 'Country'},
            'geonameid': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dariah_static_data']