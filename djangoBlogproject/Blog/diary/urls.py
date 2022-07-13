from django.urls import path, include
from . import views


urlpatterns = [
    path('diary/', views.PostListView.as_view(), name='page-list'),
    # path('diafy/info/', views.info, name='info),
    path('diary/write/', views.PostCreateView.as_view(), name='page-create'),
    path('diary/page/<int:page_id>/', views.page_detail, name="page-detail"),
    path('diary/page/<int:page_id>/edit/',
         views.PostUpdateView.as_view(), name='page-update'),
    path('diary/page/<int:page_id>/delete/',
         views.PostDeleteView.as_view(), name='page-delete'),
]
