from django.urls import path

from players import views

urlpatterns = [
    path('create-match/', views.MatchCreateView.as_view(), name='create_match'),
    path('', views.MatchListView.as_view(), name='list_of_matches'),
    path('create-user/', views.PlayerCreateView.as_view(), name='create_user'),
    path('list-of-fields/', views.FieldListView.as_view(), name='field_list'),
    path('add-fields/', views.FieldCreateView.as_view(), name='add_field'),
    path('field-details/<int:pk>/', views.FieldDetailView.as_view(), name='field_details'),
    path('update-field/<int:pk>/', views.FieldUpdateView.as_view(), name='update_field'),
    path('delete-field/<int:pk>/', views.FieldDeleteView.as_view(), name='delete_field'),
    path('join-match/<int:match_pk>/', views.join_match_view, name='join_match'),
    path('leave-match/<int:match_pk>/', views.leave_match_view, name='leave_match'),
    path('match-details/<int:pk>/', views.MatchDetailView.as_view(), name='match_details'),
    path('update-match/<int:pk>/', views.MatchUpdateView.as_view(), name='update_match'),
    path('delete-match/<int:pk>/', views.MatchDeleteView.as_view(), name='delete_match'),
]
