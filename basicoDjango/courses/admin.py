from django.contrib import admin

# Register your models here.
from courses.models import Course

class CouseAdmin(admin.ModelAdmin):
    list_display = ['name','slug','descricao','update_at',"imagem"]
    search_fields = ['name','descricao','slug']
    prepopulated_fields = {'slug':('name',)}

    
admin.site.register(Course,CouseAdmin)
