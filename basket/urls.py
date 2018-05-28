from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="player"),
    path('testlist', views.index, name="player_list"),
    path('view/<int:player_id>', views.detail, name="player_detail"),
    path('add',views.TemplateAdd,name='add'),
    path('list',views.TemplateList,name='Templatelist'),
    path('edit/<int:id_player>',views.edit_player,name='edit_player'),
    path('delete/<int:id_player>',views.delete_player,name='delete_player'),


]
