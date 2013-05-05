#coding:utf8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import date

from django.test import TestCase
from django.db.models import CharField,IntegerField,DateField
import models

class ModelsTest(TestCase):

    def setUp(self):
        self.models = []
        for k in models.tables:
            self.models.append(models.__dict__[k])

    def test_save_and_get(self):
        for Model in self.models:
            instance = Model()
            for fieldname in instance.__dict__:
                if fieldname[0] == '_': break
                if fieldname == 'id': break
                field = getattr(instance,fieldname)
                if isinstance(field,CharField): field = u'Test String'
                elif isinstance(field,IntegerField): field = 12345
                elif isinstance(field,DateField): field = date.today()

            instance.save()
            id = instance.id
            self.assertIsNotNone(id,msg="cant save %s" % instance.__repr__())
            self.assertEqual(Model.objects.get(id=id),instance, msg=" cant get %s" % instance.__repr__())

