# -*- coding:utf-8 -*-
from django.forms import DateField, ModelForm, IntegerField
from widgets import H5DateInput, H5NumberInput
import models


class H5ModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(H5ModelForm, self).__init__(*args, **kwargs)
        for k in self.fields:
            if isinstance(self.fields[k],DateField): self.fields[k].widget=H5DateInput()
            if isinstance(self.fields[k],IntegerField): self.fields[k].widget=H5NumberInput()
            self.fields[k].widget.attrs['placeholder'] = self.fields[k].label

    def to_data(self):
        data={}
        data['name']   = self._meta.model._meta.module_name
        data['title']  = self._meta.model._meta.verbose_name_plural
        data['fields'] = [{
                'name':   w.name,
                'label':  w.label,
                'widget': unicode(w),
            } for w in self]
        return data


for k in models.tables:
    Meta = type('Meta', (), {'model': models.__dict__[k]})
    globals()[k] = type(k, (H5ModelForm,), {'Meta': Meta})
