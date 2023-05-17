from django.db import models


class Word(models.Model):
    subject = models.CharField(max_length=100)
    meaning = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Example(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
