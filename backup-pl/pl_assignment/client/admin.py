from django.contrib import admin
from client.models import Book, RackBook, UserRole, Rack


admin.site.register(Book)
admin.site.register(Rack)
admin.site.register(RackBook)
admin.site.register(UserRole)