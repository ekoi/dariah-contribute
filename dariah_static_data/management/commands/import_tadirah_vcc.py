from dariah_static_data.models import TADIRAHVCC
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_vcc.csv'
    mapping = [('uri', 1), ('name', 1), ('description', 1)]  # [('model_fieldname', required?),...], order same as in CSV
    model = TADIRAHVCC
