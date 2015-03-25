# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contribution'
        db.create_table(u'dariah_inkind_contribution', (
            ('dc_identifier', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dc_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dc_date', self.gf('django.db.models.fields.PositiveIntegerField')(default=2015, max_length=4)),
            ('dc_relation', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('vcard_logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('dc_publisher', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dc_publisher_description_en', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dc_publisher_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dc_publisher_lang', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('dc_publisher_relation', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('dc_coverage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dariah_static_data.Country'], null=True, blank=True)),
            ('dcterms_abstract_en', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('dcterms_abstract', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dcterms_abstract_lang', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('dc_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dcterms_typeofindkindcontribs', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dcterms_compliancetoreq', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dcterms_contribanddariah', self.gf('django.db.models.fields.CharField')(default='No', max_length=10)),
            ('dcterms_reason', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('skos_preflabel_vcc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dariah_static_data.TADIRAHVCC'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dariah_inkind', ['Contribution'])

        # Adding M2M table for field skos_preflabel_activity on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_activity')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('tadirahactivity', models.ForeignKey(orm[u'dariah_static_data.tadirahactivity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'tadirahactivity_id'])

        # Adding M2M table for field skos_preflabel_object on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_object')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('tadirahobject', models.ForeignKey(orm[u'dariah_static_data.tadirahobject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'tadirahobject_id'])

        # Adding M2M table for field skos_preflabel_technique on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_technique')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('tadirahtechnique', models.ForeignKey(orm[u'dariah_static_data.tadirahtechnique'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'tadirahtechnique_id'])

        # Adding M2M table for field skos_preflabel_discipline on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_discipline')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('discipline', models.ForeignKey(orm[u'dariah_static_data.discipline'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'discipline_id'])

        # Adding M2M table for field dc_creator on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_dc_creator')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('dccreator', models.ForeignKey(orm[u'dariah_inkind.dccreator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'dccreator_id'])

        # Adding M2M table for field dc_contributor on 'Contribution'
        m2m_table_name = db.shorten_name(u'dariah_inkind_contribution_dc_contributor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contribution', models.ForeignKey(orm[u'dariah_inkind.contribution'], null=False)),
            ('dccontributor', models.ForeignKey(orm[u'dariah_inkind.dccontributor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contribution_id', 'dccontributor_id'])

        # Adding model 'DcCreator'
        db.create_table(u'dariah_inkind_dccreator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('foaf_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('foaf_person', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'dariah_inkind', ['DcCreator'])

        # Adding model 'DcContributor'
        db.create_table(u'dariah_inkind_dccontributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('foaf_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('foaf_person', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'dariah_inkind', ['DcContributor'])


    def backwards(self, orm):
        # Deleting model 'Contribution'
        db.delete_table(u'dariah_inkind_contribution')

        # Removing M2M table for field skos_preflabel_activity on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_activity'))

        # Removing M2M table for field skos_preflabel_object on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_object'))

        # Removing M2M table for field skos_preflabel_technique on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_technique'))

        # Removing M2M table for field skos_preflabel_discipline on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_skos_preflabel_discipline'))

        # Removing M2M table for field dc_creator on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_dc_creator'))

        # Removing M2M table for field dc_contributor on 'Contribution'
        db.delete_table(db.shorten_name(u'dariah_inkind_contribution_dc_contributor'))

        # Deleting model 'DcCreator'
        db.delete_table(u'dariah_inkind_dccreator')

        # Deleting model 'DcContributor'
        db.delete_table(u'dariah_inkind_dccontributor')


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
        u'dariah_inkind.contribution': {
            'Meta': {'ordering': "['-published_on']", 'object_name': 'Contribution'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'dc_contributor': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_inkind.DcContributor']", 'null': 'True', 'blank': 'True'}),
            'dc_coverage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dariah_static_data.Country']", 'null': 'True', 'blank': 'True'}),
            'dc_creator': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_inkind.DcCreator']", 'null': 'True', 'blank': 'True'}),
            'dc_date': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2015', 'max_length': '4'}),
            'dc_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dc_identifier': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'dc_publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_publisher_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dc_publisher_description_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dc_publisher_lang': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'dc_publisher_relation': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_relation': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'dc_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dcterms_abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dcterms_abstract_en': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'dcterms_abstract_lang': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'dcterms_compliancetoreq': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dcterms_contribanddariah': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '10'}),
            'dcterms_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dcterms_typeofindkindcontribs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'published_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'skos_preflabel_activity': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_static_data.TADIRAHActivity']", 'null': 'True', 'blank': 'True'}),
            'skos_preflabel_discipline': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_static_data.Discipline']", 'null': 'True', 'blank': 'True'}),
            'skos_preflabel_object': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_static_data.TADIRAHObject']", 'null': 'True', 'blank': 'True'}),
            'skos_preflabel_technique': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dariah_static_data.TADIRAHTechnique']", 'null': 'True', 'blank': 'True'}),
            'skos_preflabel_vcc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dariah_static_data.TADIRAHVCC']", 'null': 'True', 'blank': 'True'}),
            'vcard_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'dariah_inkind.dccontributor': {
            'Meta': {'object_name': 'DcContributor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'foaf_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'foaf_person': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'dariah_inkind.dccreator': {
            'Meta': {'object_name': 'DcCreator'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'foaf_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'foaf_person': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'last_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
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

    complete_apps = ['dariah_inkind']