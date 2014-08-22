from dariah_static_data.models import TADIRAHTechnique
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_technique.csv'
    fieldnames = ['name', 'uri', 'related_activity']
    mapping = [('name', 'name', 1), ('uri', 'uri', 1)]  # [('model_fieldname', 'csv_fieldname', required?),...], omit fields that are not in the model
    model = TADIRAHTechnique
