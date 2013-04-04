# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'users'
        db.create_table(u'dynamicbase_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dynamicbase', ['users'])

        # Adding model 'rooms'
        db.create_table(u'dynamicbase_rooms', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'dynamicbase', ['rooms'])


    def backwards(self, orm):
        # Deleting model 'users'
        db.delete_table(u'dynamicbase_users')

        # Deleting model 'rooms'
        db.delete_table(u'dynamicbase_rooms')


    models = {
        u'dynamicbase.rooms': {
            'Meta': {'object_name': 'rooms'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dynamicbase.users': {
            'Meta': {'object_name': 'users'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['dynamicbase']