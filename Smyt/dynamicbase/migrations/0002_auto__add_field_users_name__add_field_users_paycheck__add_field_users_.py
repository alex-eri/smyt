# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'users.name'
        db.add_column(u'dynamicbase_users', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'users.paycheck'
        db.add_column(u'dynamicbase_users', 'paycheck',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'users.date_joined'
        db.add_column(u'dynamicbase_users', 'date_joined',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 4, 4, 0, 0)),
                      keep_default=False)

        # Adding field 'rooms.department'
        db.add_column(u'dynamicbase_rooms', 'department',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'rooms.spots'
        db.add_column(u'dynamicbase_rooms', 'spots',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'users.name'
        db.delete_column(u'dynamicbase_users', 'name')

        # Deleting field 'users.paycheck'
        db.delete_column(u'dynamicbase_users', 'paycheck')

        # Deleting field 'users.date_joined'
        db.delete_column(u'dynamicbase_users', 'date_joined')

        # Deleting field 'rooms.department'
        db.delete_column(u'dynamicbase_rooms', 'department')

        # Deleting field 'rooms.spots'
        db.delete_column(u'dynamicbase_rooms', 'spots')


    models = {
        u'dynamicbase.rooms': {
            'Meta': {'object_name': 'rooms'},
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'dynamicbase.users': {
            'Meta': {'object_name': 'users'},
            'date_joined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 4, 4, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['dynamicbase']