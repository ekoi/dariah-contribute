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
