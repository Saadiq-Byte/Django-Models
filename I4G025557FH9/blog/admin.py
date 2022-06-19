from django.contrib import admin

# Register your models here.
from .models import Title, Text, Created_Date, Published_date

admin.site.register(Title)
admin.site.register(Text)
admin.site.register(Created_Date)
admin.site.register(Published_date)