from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100) 
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # connect to the class, models.CASCADE
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # default is an optional parameter