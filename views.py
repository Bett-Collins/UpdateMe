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


context={'businesses':businesses,'users':users,'neighbourhoods':neighbourhoods}
    return render(request,'index.html',context)

def registeruser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')
    else:
        form = CreateUserForm
    context = {
            
            'form':form,
                        }

    return render(request,'registration/register.html',context)


   