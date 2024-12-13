from django.contrib import admin
from catalog.models import Genre,Language,Author,Book,BookInstance

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)