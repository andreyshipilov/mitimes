# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Matter'
        db.create_table('core_matter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Client'])),
        ))
        db.send_create_signal('core', ['Matter'])

        # Adding model 'ActivityType'
        db.create_table('core_activitytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('core', ['ActivityType'])

        # Adding model 'ActivityCode'
        db.create_table('core_activitycode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_default_for_call_to', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default_for_call_from', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default_for_email_to', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default_for_email_from', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_default_for_event', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['ActivityCode'])

        # Adding model 'Activity'
        db.create_table('core_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Profile'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ActivityType'])),
            ('code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ActivityCode'])),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('matter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Matter'])),
            ('units', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('core', ['Activity'])


    def backwards(self, orm):
        # Deleting model 'Matter'
        db.delete_table('core_matter')

        # Deleting model 'ActivityType'
        db.delete_table('core_activitytype')

        # Deleting model 'ActivityCode'
        db.delete_table('core_activitycode')

        # Deleting model 'Activity'
        db.delete_table('core_activity')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.activity': {
            'Meta': {'object_name': 'Activity'},
            'code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ActivityCode']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Matter']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ActivityType']"}),
            'units': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Profile']"})
        },
        'core.activitycode': {
            'Meta': {'object_name': 'ActivityCode'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default_for_call_from': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default_for_call_to': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default_for_email_from': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default_for_email_to': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_default_for_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.activitytype': {
            'Meta': {'object_name': 'ActivityType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'core.matter': {
            'Meta': {'object_name': 'Matter'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Client']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.client': {
            'Meta': {'object_name': 'Client'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'users.profile': {
            'Meta': {'object_name': 'Profile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('annoying.fields.AutoOneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']