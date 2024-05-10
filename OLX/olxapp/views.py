from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.views.generic import DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    b=product.objects.all()
    return render(request,'view.html',{'b':b})
# def detail(request,n):
#     b=product.objects.all(id=n)
#     return render(request, 'view.html', {'b': b})


class detail(DetailView):
    model=product
    template_name="detail.html"
    context_object_name="b"

# def delete(request,n):
#     b=product.objects.get(id=n)
#     b.delete()
#     return home(request)

class delete(DeleteView):
    model=product
    template_name='delete.html'
    success_url = reverse_lazy('olxapp:view')

class update(UpdateView):
    model=product
    template_name='edit.html'
    fields = ['product_name','price','product_desc','year_reg','product_image',]
    success_url = reverse_lazy('olxapp:view')

@login_required
def Add(request):
    if(request.method=='POST'):
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.FILES['d']
        e=request.POST['e']

        p=product.objects.create(product_name=a,price=b,year_reg=c,product_image=d,product_desc=e)
        p.save()
        return home(request)
    return render(request,'add.html')


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        if(c==p):
          b=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
          b.save()
          return redirect('olxapp:view')
        else:
            return HttpResponse("Passwords are not same")
    return render (request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('olxapp:view')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

