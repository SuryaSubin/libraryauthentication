from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book

# Create your views here.
def home(request):
    context={'name':'Arun'}
    return render(request,'home.html',context)


@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a= request.POST['a']
        p= request.POST['p']
        l= request.POST['l']
        pa= request.POST['pa']
        c=request.FILES['i']
        f=request.FILES['f']

        b=Book.objects.create(title=t,author=a,price=p,language=l,pages=pa,cover=c,pdf=f)
        b.save()
        return view_books(request)
    return render(request,'add.html')
@login_required
def view_books(request):
    # k=con.execute('select * from Book')
    k=Book.objects.all()  #Reads all records from table Book anD ASSIGNS IT TO K
    return render(request,'view.html',{'book':k})

@login_required
def detail(request,p):
    k=Book.objects.get(id=p)
    return render(request,'detail.html',{'book':k})
@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.pages=request.POST['pa']
        k.language=request.POST['l']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES['i']
        if (request.FILES.get('f') == None):
            k.save()
        else:
            k.pdf = request.FILES['f']
            k.save()
            return view_books(request)


    return render(request,'edit.html',{'book':k})
@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return view_books(request)

from django.db.models import Q
def searchbooks(request):
    k=None   #Initialize k as None
    if(request.method=="POST"):
        query=request.POST['q']#get the input key from form
        print(query)
        if query:
            k=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) # it checks the key in title and author field at every records.
            #filter function returns only the matching records.
            print(k)
    return render(request,'search.html',{'book':k})
