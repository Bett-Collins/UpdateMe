from django.shortcuts import render

# Create your views here.
def index(request):
    businesses=Business.objects.all()

    if 'item_name' in request.GET:
        item_name=request.GET['item_name']
        businesses=businesses.filter(name__icontains=item_name)
    else:
        businesses=Business.objects.all()

    users=User.objects.all()
    neighbourhoods=NeighbourHood.objects.all()


   