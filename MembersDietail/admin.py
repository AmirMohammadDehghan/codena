from django.contrib import admin
from .models import Our_Member, Member_Cantact_Way



class MemberContactWayAdmin(admin.ModelAdmin):
    list_display = ('user', 'name_way', 'way')
    search_fields = ['user__username', 'name_way', 'way']


admin.site.register(Member_Cantact_Way, MemberContactWayAdmin)


class OurMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'small_description', 'slug')
    search_fields = ['user__username', 'small_description', 'slug']
    prepopulated_fields = {'slug': ('user',)}


admin.site.register(Our_Member, OurMemberAdmin)
