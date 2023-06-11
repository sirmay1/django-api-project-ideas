from django.db import models


class Idea(models.Model):
    name = models.CharField(max_length=50)
    lang1 = models.CharField(max_length=50)
    lang2 = models.CharField(max_length=50)
    frontend = models.CharField(max_length=50)
    backend = models.CharField(max_length=50)
    database = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' | ' + self.lang1 + ' | ' + self.lang2 + ' | ' + self.frontend + ' | ' + self.backend + '| ' + str(
            self.database)
