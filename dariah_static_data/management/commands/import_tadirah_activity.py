"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contribss.

    Copyright 2014 Data Archiving and Networked Services

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from dariah_static_data.models import TADIRAHActivity
from dariah_static_data.management.commands._private_helper import Command as SuperCommand


class Command(SuperCommand):
    filename = 'tadirah_activity.csv'
    mapping = [('activity_group_name', 1),
               ('activity_name', 0),
               ('uri', 1),
               ('description', 1)]  # [('model_fieldname', required?),...], order same as in CSV
    model = TADIRAHActivity
