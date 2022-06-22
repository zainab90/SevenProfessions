from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from serviceApp.models import User, Category, Service, SlidShow


class CategoryAdmin(admin.ModelAdmin):
    def admin_image(self, obj):
        return mark_safe ('<img src="%s" style="width: 145px; height:145px;"/>' % obj.cat_image.url)
    admin_image.allow_tags = True
    admin_image.short_description ='Category Photo'
    list_display = ('cat_name', 'cat_details','admin_image')




class SlidShowAdmin(admin.ModelAdmin):
    def admin_image(self, obj):
        return mark_safe ('<img src="%s" style="width: 145px; height:145px;"/>' % obj.slid_image.url)
    admin_image.allow_tags = True
    admin_image.short_description ='slide_show Photo'
    list_display = ('admin_image','slid_title')




class ServiceAdmin(admin.ModelAdmin):
    def service_image(self, obj):
        return mark_safe ('<img src="%s" style="width: 145px; height:145px;"/>' % obj.serv_Img.url)
    service_image.allow_tags = True
    service_image.short_description ='Service Photo'
    list_display = ('serv_name', 'serv_details','date','serv_cat','service_image')


admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(SlidShow,SlidShowAdmin)
admin.site.site_header='Seven Profession'
