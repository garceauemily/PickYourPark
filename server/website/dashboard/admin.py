from django.contrib import admin

from dashboard.models import Space
from dashboard.models import LotSize
# Register your models here.

# Admin site
# Databases
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('Lot','Username')
    list_filter = ('Lot',)
admin.site.register(Space, SpaceAdmin)

class LotSizesAdmin(admin.ModelAdmin):
    list_display=('name','num_spaces','percentage_full')
admin.site.register(LotSize,LotSizesAdmin)
# Register your models here.
