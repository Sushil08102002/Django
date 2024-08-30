from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,generics,mixins,viewsets
from .serializers import ProfileSerializer,PostSerializer,BooksSerializer
from .models import Profile,Post,Books
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser






class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    http_method_names=['get','post','retrieve','put','patch']



@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET','POST'])
def print_msg(request):
    if request.method=='POST':
        return Response({"message":"Got some data !", "data":request.data})
    return Response({"message":"Hello , World!"})    

    
class UserList(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[]
    
    
#here we are using mixins for implementation and practice
class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def get(self,request,*args,**kwargs):   # this is called as ListModelMixin return list of all data
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):  # this comes under CreateModelMixin
        return self.create(request,*args,**kwargs)
    
    
class PostListRetrieve(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
    def get(self,request,*args,**kwargs):  #this is used for retriving a particular data with priamry key
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,*kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

# class BooksViewSet(viewsets.ViewSet):
#     """A simple viewset for listing and retriving users"""
#     def list(self,request):
#         queryset=Books.objects.all()
#         serializer=BooksSerializer(queryset,many=True)
#         return Response(serializer.data)
    
'''now we make book viewset from modelViewset'''
'''these is a model viewset that create all 
   operations for model in a single class'''
class BooksViewSet(viewsets.ModelViewSet):
    serializer_class=BooksSerializer
    queryset=Books.objects.all()
    