from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# req -> Response
# request handler
# action

def say_hello(request):
        # return HttpResponse('Hello world')
        return render(request, 'hello.html', {'name' : 'Gayatri'})
 