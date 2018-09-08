from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField()
    summary = models.CharField(max_length = 250)
    body = models.TextField()


    def alter_body(self):
        return self.body[:100]+'...'

    def alter_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.summary
