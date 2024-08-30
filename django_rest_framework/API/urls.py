from django.urls import path,include
from .views import (ProfileViewSet,hello_world,print_msg,UserList,PostList,PostListRetrieve,BooksViewSet)
from rest_framework.routers import SimpleRouter,Route,DynamicRoute,DefaultRouter

class CustomRouters(SimpleRouter):
    routes=[
        Route(
            url=r'^{prefix}$',
            mapping={'get':'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix':'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get':'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix':'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url-path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]

# router=SimpleRouter()
router=CustomRouters()
router.register('profile',ProfileViewSet)
router.register('books',BooksViewSet,basename='books')

urlpatterns = [
    path('',include(router.urls)),
    path('hello/',hello_world,name='hello_world'),
    path('hello1/',print_msg),
    path('users/',UserList.as_view()),
    path('post_list/',PostList.as_view()),
    path('post_list/<int:pk>/',PostListRetrieve.as_view())
]
