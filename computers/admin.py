from django.contrib import admin

from .models import Computer


# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'picture', 'rent', 'stocks', 'os', 'DISP_size', 'RAM', 'USB_port_num',
                    'HDMI_port_num')
    search_fields = ['brand']


admin.site.register(Computer, ComputerAdmin)

