from django.shortcuts import render, redirect
from .models import Url
import uuid
# Create your views here.
def home(request):
    if request.method == 'POST':
        link = request.POST['link']
        uuid_url = str(uuid.uuid4())[:5]
        new_link = Url(link=link, uuid=uuid_url)
        new_link.save()
        return render(request, 'shorter/home.html', {'uuid':uuid_url,'link':link})
    return render(request, 'shorter/home.html')

def create(request, url):
    link = Url.objects.get(uuid = url)
    print(url)
    return redirect(link.link)
