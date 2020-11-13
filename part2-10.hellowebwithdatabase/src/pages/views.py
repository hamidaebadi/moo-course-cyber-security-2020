from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    mid = request.GET.get('id')
    content = Message.objects.get(id = mid)		
    return HttpResponse(content.content )
