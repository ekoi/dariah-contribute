from dariah_static_data.models import TADIRAHVCC
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_vcc.csv'
    fieldnames = ['uri', 'name', 'description']
    mapping = [('name', 'name', 1), ('uri', 'uri', 1), ('description', 'description', 1)]  # [('model_fieldname', 'csv_fieldname', required?),...], omit fields that are not in the model
    model = TADIRAHVCC
