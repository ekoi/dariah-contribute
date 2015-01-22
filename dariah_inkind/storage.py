"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.

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

from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        If the name is not free, it deletes the original file so it can be
        replaced by the new one.
        This file storage solves overwrite on upload problem.

        Based on http://djangosnippets.org/snippets/976/ and
        http://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name
        """
        # If the filename already exists, remove it as if it was a true file system
        self.delete(name)
        return name
