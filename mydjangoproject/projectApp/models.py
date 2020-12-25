from django.db import models


class postId(models.Model):
    userId = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)

    class Meta:
        verbose_name = "Posts"

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    postId = models.ForeignKey(postId, on_delete=models.CASCADE)
    name = models.CharField(max_length=5000)
    email = models.EmailField(max_length=5000)
    body = models.CharField(max_length=500000)

    class Meta:
        verbose_name = "Comments"

    def __unicode__(self):
        return '%s %s' % (self.name, self.email)