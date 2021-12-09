from django.shortcuts import render,HttpResponse
from django.forms import ModelForm  
from .forms import Event_registration_form
# Create your views here.

def register_view(request):
    if request.method =='POST':
        form=Event_registration_form(request.POST or None)
        
        if form.is_valid():
            
            form.save()
            #return redirect('/')
            return HttpResponse(' <center><h1>Thank you.Registration Successful.</h1></center>')

        else:
            return HttpResponse('<h1>Form invalid.Try Again.</h1>')
    
    else:
        form = Event_registration_form()
        context={"form":form}
        return render(request,'form.html',context=context)