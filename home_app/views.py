from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from home_app.models import Thestart
from home_app.forms import thestartform
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    values = Thestart.objects.all().filter(user_id= request.user.id)
    sum=0
    for items in values:
        sum=sum+items.price
    return render(request,'home.html',{'values':values,'total':sum})

@login_required
def add(request):
    if request.method=='GET':
        form = thestartform
        return render(request,'add.html',{'form':form})
    else:
        form = thestartform(request.POST)
        if form.is_valid():
            expense=form.cleaned_data['expense']
            price=form.cleaned_data['price']
            
            Thestart.objects.create(expense=expense,price=price, user_id = request.user.id)
            return redirect('home')
        else:
            return render(request,'add.html',{'form':form})
        
@login_required       
def delete(request,id):
    values = Thestart.objects.get(id=id)
    values.delete()
    return redirect('home')

@login_required
def delete_all(request):
    values=Thestart.objects.all().delete()
    return redirect('home')

@login_required   
def edit(request,id):
    try:
        values = Thestart.objects.get(id=id)
    except Thestart.DoesNotExist:
        return render(request,'404.html')
    
    if request.method == 'GET':
        form = thestartform(instance=values)
        return render(request,'edit.html',{'form':form})
    else:
        form=thestartform(request.POST)
        if form.is_valid():
            expense = form.cleaned_data['expense']
            price = form.cleaned_data['price']
            
            Thestart.objects.create(expense=expense,price=price,user_id=request.user.id)
            
            return redirect('home')
