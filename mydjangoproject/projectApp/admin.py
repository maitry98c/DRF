from django.contrib import admin

from .models import Comments, postId

admin.site.register(postId)
admin.site.register(Comments)