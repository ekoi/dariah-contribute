# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.alter_column(u'dariah_contributions_contribution',
                        'dc_identifier', 
                        self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Deleting field 'Contribution.description'
        db.delete_column(u'dariah_contributions_contribution', 'description')

        # Deleting field 'Contribution.vocabulary'
        db.delete_column(u'dariah_contributions_contribution', 'vocabulary')

        # Deleting field 'Contribution.creator'
        db.delete_column(u'dariah_contributions_contribution', 'creator_id')

        # Deleting field 'Contribution.abstract'
        db.delete_column(u'dariah_contributions_contribution', 'abstract')

        # Deleting field 'Contribution.contributor'
        db.delete_column(u'dariah_contributions_contribution', 'contributor')

        # Deleting field 'Contribution.relation'
        db.delete_column(u'dariah_contributions_contribution', 'relation')

        # Deleting field 'Contribution.coverage'
        db.delete_column(u'dariah_contributions_contribution', 'coverage')

        # Deleting field 'Contribution.date'
        db.delete_column(u'dariah_contributions_contribution', 'date')

        # Deleting field 'Contribution.id'
        db.delete_column(u'dariah_contributions_contribution', u'id')

        # Deleting field 'Contribution.subject'
        db.delete_column(u'dariah_contributions_contribution', 'subject')

        # Deleting field 'Contribution.publisher'
        db.delete_column(u'dariah_contributions_contribution', 'publisher')

        # Deleting field 'Contribution.title'
        db.delete_column(u'dariah_contributions_contribution', 'title')

        # Deleting field 'Contribution.publish_date'
        db.delete_column(u'dariah_contributions_contribution', 'publish_date')

        # Deleting field 'Contribution.modify_date'
        db.delete_column(u'dariah_contributions_contribution', 'modify_date')

    def backwards(self, orm):

        # Adding field 'Contribution.description'
        db.add_column(u'dariah_contributions_contribution', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5000, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.vocabulary'
        db.add_column(u'dariah_contributions_contribution', 'vocabulary',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Contribution.creator'
        raise RuntimeError("Cannot reverse this migration. 'Contribution.creator' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contribution.creator'
        db.add_column(u'dariah_contributions_contribution', 'creator',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True),
                      keep_default=False)

        # Adding field 'Contribution.abstract'
        db.add_column(u'dariah_contributions_contribution', 'abstract',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2000, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.contributor'
        db.add_column(u'dariah_contributions_contribution', 'contributor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.relation'
        db.add_column(u'dariah_contributions_contribution', 'relation',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.coverage'
        db.add_column(u'dariah_contributions_contribution', 'coverage',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.date'
        db.add_column(u'dariah_contributions_contribution', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default='2014-01-01'),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contribution.id'
        raise RuntimeError("Cannot reverse this migration. 'Contribution.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contribution.id'
        db.add_column(u'dariah_contributions_contribution', u'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Adding field 'Contribution.subject'
        db.add_column(u'dariah_contributions_contribution', 'subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'Contribution.publisher'
        db.add_column(u'dariah_contributions_contribution', 'publisher',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Contribution.title'
        raise RuntimeError("Cannot reverse this migration. 'Contribution.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contribution.title'
        db.add_column(u'dariah_contributions_contribution', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=100),
                      keep_default=False)

        # Adding field 'Contribution.publish_date'
        db.add_column(u'dariah_contributions_contribution', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Contribution.modify_date'
        db.add_column(u'dariah_contributions_contribution', 'modify_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

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
            'dc_identifier': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'dc_publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_relation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_subject': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'dc_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dcterms_abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dcterms_abstract_lang': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'published_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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
