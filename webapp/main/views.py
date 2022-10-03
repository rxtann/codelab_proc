from django.shortcuts import render

# Create your views here.
def list_view(request):
   
    actors = [{"id": '1',"name": 'Rocket falconnine'}, {"id": '2',"name": 'Dragon lowrence'}]
    
    return render(request, "main/home.html",  {'actors': actors})