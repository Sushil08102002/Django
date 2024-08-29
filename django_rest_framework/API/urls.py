from django.urls import path,include
from .views import ProfileViewSet,hello_world,print_msg,UserList,PostList
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('profile',ProfileViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('hello/',hello_world,name='hello_world'),
    path('hello1/',print_msg),
    path('users/',UserList.as_view()),
    path('post_list/',PostList.as_view())
]
