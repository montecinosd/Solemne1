from django.contrib import admin
from .models import Team, Player,Coach,Nomination
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo','code',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name','age','email','nickname','rut','dv',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'full_rut', 'age', 'height', 'weight', 'thumb', )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' \
            % (obj.picture.url))
@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ('name_Match','date','hour', )
