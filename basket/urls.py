from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('testlist', views.index, name="player_list"),
    path('teamlist', views.teamindex, name="team_list"),

    path('view/<int:player_id>', views.detail, name="player_detail"),
    path('add',views.TemplateAdd,name='add'),
    path('addTeam',views.TemplateAddTeam,name='addTeam'),
#LIST
    path('list',views.TemplateList,name='Templatelist'),
    path('listTeam',views.TemplateListTeam,name='TemplatelistTeam'),

    path('edit/<int:id_player>',views.edit_player,name='edit_player'),
    path('editTeam/<int:id_team>',views.EditTeam,name='EditTeam'),

    path('delete/<int:id_player>',views.delete_player,name='delete_player'),
    path('deleteTeam/<int:id_team>',views.DeleteTeam,name='DeleteTeam'),



]
