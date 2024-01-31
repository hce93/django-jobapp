from django.contrib import admin
from app.models import JobPost, Location, Author, Skills

class JobAdmin(admin.ModelAdmin):
    # modify what displays on admin panel. This overrides str representation on the admin panel
    list_display = ('title', 'salary', 'date')
    list_filter = ('date','salary', 'expiry')
    search_fields=('title','description')
    search_help_text = "Search for title or description"
    # fields = (('title', 'description'), 'expiry')
    # exclude = ('title', 'description', 'expiry')
    # fieldsets = (
    #     ("Basic information", {
    #         'fields':('title', 'description')
    #         }),
    #     ("Further information", {
    #         'classes':('collapse',),
    #         'fields':('salary', 'expiry')
    #         })
    # )

# Register your models here.
admin.site.register(JobPost, JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)