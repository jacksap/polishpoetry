from django.contrib import admin
from .models import Poet, Poem, Comment, Collection

# Register your models here.
admin.site.register(Poet)
admin.site.register(Poem)
admin.site.register(Comment)
admin.site.register(Collection)