# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contribution'
        db.create_table(u'dariah_contributions_contribution', (
            ('dc_identifier', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dc_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dc_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('dc_relation', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dc_publisher', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dc_coverage', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dc_subject', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('dcterms_abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dcterms_abstract_lang', self.gf('django.db.models.fields.CharField')(default='en', max_length=2)),
            ('dc_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'dariah_contributions', ['Contribution'])

        # Adding M2M table for field dc_creator on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_contributions_contribution_dc_creator')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_contributions.contribution'], null=False)),
            ('dccreator', models.ForeignKey(orm[u'dariah_contributions.dccreator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'dccreator_id'])

        # Adding M2M table for field dc_contributor on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_contributions_contribution_dc_contributor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_contributions.contribution'], null=False)),
            ('dccontributor', models.ForeignKey(orm[u'dariah_contributions.dccontributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'dccontributor_id'])

        # Adding model 'DcCreator'
        db.create_table(u'dariah_contributions_dccreator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foaf_person', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('foaf_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('foaf_publications', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'dariah_contributions', ['DcCreator'])

        # Adding model 'DcContributor'
        db.create_table(u'dariah_contributions_dccontributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foaf_person', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('foaf_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('foaf_publications', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'dariah_contributions', ['DcContributor'])


    def backwards(self, orm):
        # Deleting model 'Contribution'
        db.delete_table(u'dariah_contributions_contribution')

        # Removing M2M table for field dc_creator on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_contributions_contribution_dc_creator'))

        # Removing M2M table for field dc_contributor on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_contributions_contribution_dc_contributor'))

        # Deleting model 'DcCreator'
        db.delete_table(u'dariah_contributions_dccreator')

        # Deleting model 'DcContributor'
        db.delete_table(u'dariah_contributions_dccontributor')


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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'dc_contributor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_contributions.DcContributor']", 'null': 'True', 'blank': 'True'}),
            'dc_coverage': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_creator': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_contributions.DcCreator']", 'null': 'True', 'blank': 'True'}),
            'dc_date': ('django.db.models.fields.DateTimeField', [], {}),
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
