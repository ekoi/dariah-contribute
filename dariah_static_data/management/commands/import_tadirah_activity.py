from dariah_static_data.models import TADIRAHActivity
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_activity.csv'
    mapping = [('activity_group_name', 1),
               ('activity_name', 0),
               ('uri', 1),
               ('description', 1)]  # [('model_fieldname', required?),...], order same as in CSV
    model = TADIRAHActivity
