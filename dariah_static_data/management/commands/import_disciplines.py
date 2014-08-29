from dariah_static_data.models import Discipline
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'disciplines.csv'
    mapping = [('name', 1), ('uri', 1), ('description', 1)]  # [('csv_fieldname', 'model_fieldname', required?),...], order same as in CSV
    model = Discipline
