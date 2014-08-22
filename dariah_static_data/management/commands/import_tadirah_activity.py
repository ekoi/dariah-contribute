from dariah_static_data.models import TADIRAHActivity
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_activity.csv'
    fieldnames = ['activity_group_name', 'activity_name', 'uri', 'description']
    mapping = [('activity_group_name', 'activity_group_name', 1),
               ('activity_name', 'activity_name', 0),
               ('uri', 'uri', 1),
               ('description', 'description', 1)]  # [('model_fieldname', 'csv_fieldname', required?),...], omit fields that are not in the model
    model = TADIRAHActivity
