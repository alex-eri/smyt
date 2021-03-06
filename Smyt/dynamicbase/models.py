# coding: utf-8
from datetime import date
from django.db import models
#from django.utils.datetime_safe import date


field_types = {
    'char': (models.CharField, {'max_length': 255, 'default': ''}),
    'int':  (models.IntegerField, {'default': 0}),
    'date': (models.DateField, {'default': date.today()})
}
tables = []


def setup_field(field):
    field_type = field.pop('type')
    field_class, field_kwargs = field_types[field_type]
    field_kwargs['verbose_name'] = field.pop('title',field_type)
    return field_class(**field_kwargs)

def get_files():
    import  glob, os
    path    = os.path.dirname(os.path.abspath(__file__))
    pattern = os.path.join(path, 'model/*.yaml')
    return glob.glob(pattern)
#    yield

def parse_models():
    import yaml, codecs

    for filename in get_files():
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            y = yaml.safe_load(f)
            for k in y:
                v = y[k]
                attrs = {'__module__': __name__}

                fields = v.pop('fields', [])
                title = v.pop('title', k)

                attrs['Meta'] = type('Meta', (), {'verbose_name': title, 'verbose_name_plural': title})

                for field in fields:
                    attrs[field['id']] = setup_field(field)

                globals()[k] = type(k, (models.Model,),attrs)
                tables.append(k)


parse_models()
__all__ = tables