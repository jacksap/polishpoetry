from django.contrib import admin
from .models import Poet, Poem, Comment

# Register your models here.
admin.site.register(Poet)
admin.site.register(Poem)
admin.site.register(Comment)