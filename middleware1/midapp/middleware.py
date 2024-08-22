from django.core.cache import cache

#This middleware used to count the number of page views perform by user
class PageViewMiddleware:
    def __init__(self,get_response) :
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        path=request.path
        page_views=cache.get(path,0)+1
        cache.set(path,page_views)
        return response


#this request prints the count of page views in console
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        page_views = cache.get(request.path, 0)
        print(page_views+1)
        response=self.get_response(request)
        
        return response