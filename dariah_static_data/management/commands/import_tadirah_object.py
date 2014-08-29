from dariah_static_data.models import TADIRAHObject
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_object.csv'
    mapping = [('name', 'name', 1), ('uri', 'uri', 1)]  # [('csv_fieldname', 'model_fieldname', required?),...], order same as in CSV
    model = TADIRAHObject
