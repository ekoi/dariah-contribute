from dariah_static_data.models import TADIRAHObject
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_object.csv'
    fieldnames = ['name', 'uri']
    mapping = [('name', 'name', 1), ('uri', 'uri', 1)]  # [('model_fieldname', 'csv_fieldname', required?),...], omit fields that are not in the model
    model = TADIRAHObject
