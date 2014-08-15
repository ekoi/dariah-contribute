# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for item in orm.Contribution.objects.all():
            item.dc_abstract = item.abstract
            #item.dc_contributor = item.contributor
            item.dc_coverage = item.coverage
            item.dc_date = item.date
            item.dc_description = item.description
            item.dc_identifier = item.id
            item.dc_publisher = item.publisher
            item.dc_relation = item.relation
            item.dc_subject = item.subject
            item.dc_title = item.title
            item.author = item.creator
            item.last_modified_on = item.modify_date
            item.published_on = item.publish_date
            item.is_published = True
            item.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        for item in orm.Contribution.objects.all():
            item.dc_abstract = ""
            #item.dc_contributor = item.contributor
            item.dc_coverage = ""
            #item.dc_creator = item.creator
            item.dc_date = ""
            item.dc_description = ""
            item.dc_identifier = ""
            item.dc_publisher = ""
            item.dc_relation = ""
            item.dc_subject = ""
            item.dc_title = ""
            item.author = 0
            item.last_modified_on = ""
            item.published_on = ""
            item.is_published = False
            item.save()

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dariah_contributions.contribution': {
            'Meta': {'ordering': "['-published_on']", 'object_name': 'Contribution'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'dc_contributor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_contributions.DcContributor']", 'null': 'True', 'blank': 'True'}),
            'dc_coverage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_creator': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_contributions.DcCreator']", 'null': 'True', 'blank': 'True'}),
            'dc_date': ('django.db.models.fields.DateTimeField', [], {'default': "'2014-01-01'"}),
            'dc_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dc_identifier': ('django.db.models.fields.IntegerField', [], {}),
            'dc_publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_relation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_subject': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'dc_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dcterms_abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dcterms_abstract_lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'published_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),

            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'contributor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'coverage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': "'2014-01-01'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'relation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vocabulary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'dariah_contributions.dccontributor': {
            'Meta': {'object_name': 'DcContributor'},
            'foaf_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'foaf_person': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'foaf_publications': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dariah_contributions.dccreator': {
            'Meta': {'object_name': 'DcCreator'},
            'foaf_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'foaf_person': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'foaf_publications': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['dariah_contributions']
    symmetrical = True
