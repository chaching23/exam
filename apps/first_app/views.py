from django.shortcuts import render, redirect   
from django.contrib.messages import error
from .models import users, messages
import bcrypt
from datetime import datetime

def index(request):

    return render(request, 'first_app/login.html')

def register(request):
    if request.method == "POST":
        errors = users.objects.validate_registration(request.POST)
        if errors:
            for err in errors:
                error(request, err)
            print(errors)
            return redirect('/')
        else:
            new_id = users.objects.register_user(request.POST)
            request.session["id"] = new_id
          
            return redirect('/success')
    
def login(request):
    
    if users.objects.filter(email=request.POST["email"]):
        x = users.objects.filter(email=request.POST["email"])
        user = x[0]
    
    else:
        
        error(request, 'Invalid Email')
        return redirect("/")

        
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['id']= user.id
        request.session['first_name']= user.first_name
        print(success)
        return redirect("/success")

    else: 
            
        error(request, 'Invalid Password')
        return redirect("/")


def success(request):
    if 'id' not in request.session:
        return redirect('/')

    else:  
        context={
                'users_who': messages.objects.filter(users_who_create=request.session["id"]).order_by("-id"),
                'add_fav': messages.objects.filter(users_who_favorite=request.session["id"]).order_by("-id"),
                # 'all_fav' : trip.objects.all().exclude(created=request.session["id"]).exclude(users_who_favorite=request.session["id"]).order_by("-id"),
                
                'people' : users.objects.get(id=request.session["id"]),
                'all_messages': messages.objects.all(),



             }
    return render(request,'first_app/dashboard.html',context)




def create (request):
    if 'id' not in request.session:
        return redirect('/')
    
    if request.method == "POST":
        errors = users.objects.validate_create(request.POST)
        if errors:
            for err in errors:
                error(request, err)
                return redirect('/success')
     
        
        else:
            request.method == 'POST'
            message=request.POST["message"]
            quoted_by=request.POST["quoted_by"]
            print('XXXXXX')
            users_who_create = users.objects.get(id=request.session['id'])

            messages.objects.create(users_who_create=users_who_create,message=message,quoted_by=quoted_by)
            return redirect ("/success")



def show(request, show_id):
    if 'id' not in request.session:
        return redirect('/')
        
    else: 
        request.method == 'POST'

        context = {

            'user': users.objects.get(id=request.session["id"]),
            "show" : messages.objects.get(id=show_id),
            # 'all_messages': messages.objects.all()
            'all_messages': messages.objects.filter(users_who_create=show_id),


                #   'all_messages': messages.objects.all().filter(messages.objects.get(id=request.session['id']),

        } 
        return render(request,"first_app/show.html", context)




def logout(request):
    del request.session['id']
    return redirect('/')

def join(request, show_id):
    messages.objects.get(id=show_id).users_who_favorite.add(users.objects.get(id=request.session['id']))


    return redirect('/success')

def remove(request, show_id):
    messages.objects.get(id=show_id).users_who_favorite.remove(users.objects.get(id=request.session['id']))


    return redirect('/success')



    