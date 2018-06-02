from django.urls import path
from basket import views


urlpatterns = [
    path('', views.TemplateListNomination, name="player"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
#LIST
    path('testlist', views.index, name="player_list"),
    path('teamlist', views.teamindex, name="team_list"),
#ADD
    path('add',views.TemplateAdd,name='add'),
    path('addTeam',views.TemplateAddTeam,name='addTeam'),
    path('addCoach',views.TemplateAddCoach,name='addCoach'),
    path('addNomination',views.TemplateAddNomination,name='addNomination'),

#LIST WITH OPTIONS
    path('list',views.TemplateList,name='Templatelist'),
    path('listTeam',views.TemplateListTeam,name='TemplatelistTeam'),
    path('listCoach',views.TemplateListCoach,name='TemplatelistCoach'),
    path('listNomination',views.TemplateListNomination,name='TemplateListNomination'),
#EDIT
    path('edit/<int:id_player>',views.edit_player,name='edit_player'),
    path('editTeam/<int:id_team>',views.EditTeam,name='EditTeam'),
    path('editCoach/<int:id_coach>',views.EditCoach,name='EditCoach'),
#DELETE
    path('delete/<int:id_player>',views.delete_player,name='delete_player'),
    path('deleteTeam/<int:id_team>',views.DeleteTeam,name='DeleteTeam'),
    path('deleteCoach/<int:id_coach>',views.DeleteCoach,name='DeleteCoach'),



]
