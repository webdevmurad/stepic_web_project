from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='questions', blank=True)
    def get_absolute_url(self):
        return reverse('question', kwargs={"id": self.id})
    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.text