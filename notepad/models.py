from django.db import models

class Note(models.Model):
    title = models.Charfield(max_length=120)
    image = models.ImageField(null=True,Blank=True)
    Content= models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return '/notes/{}/delete'.format(self.pk)

    def get_update_url(self):
        return '/notes/{}/update'.format(self.pk)
