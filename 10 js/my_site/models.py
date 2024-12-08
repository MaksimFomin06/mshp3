from django.db import models


class NotesModel(models.Model):
    note_text: models.TextField = models.TextField()
