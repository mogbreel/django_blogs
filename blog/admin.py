from django.contrib import admin
from .models import Post

admin.site.site_header = "Django Blog"
admin.site.register(Post)
