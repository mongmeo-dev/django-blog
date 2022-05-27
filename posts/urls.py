from django.urls import path

from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate

app_name = 'posts'

urlpatterns = [
    path('new', PostCreate.as_view(), name='post_create'),
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
