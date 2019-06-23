from django.shortcuts import render, redirect   
from django.contrib.messages import error
from .models import data, trip
import bcrypt
from datetime import datetime

def index(request):
    if request.session:
        del request.session

    return render(request, 'first_app/login.html')

def register(request):
    if request.method == "POST":
        errors = data.objects.validate_registration(request.POST)
        if errors:
            for err in errors:
                error(request, err)
            print(errors)
            return redirect('/')
        else:
            new_id = data.objects.register_user(request.POST)
            request.session["id"] = new_id
          
            return redirect('/success')
    
def login(request):
    
    if data.objects.filter(email=request.POST["email"]):
        users = data.objects.filter(email=request.POST["email"])
        user = users[0]
    
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
    print(request.session['id'])
    context={
            'user': trip.objects.filter(created=request.session["id"]).order_by("-id"),
            'join': trip.objects.filter(users_who_join=request.session["id"]).order_by("-id"),
            'all_trips' : trip.objects.all().exclude(created=request.session["id"]).exclude(users_who_join=request.session["id"]).order_by("-id"),
            "people" : data.objects.get(id=request.session["id"]),


    }
    return render(request,'first_app/dashboard.html',context)


def display (request):
    return render (request, "first_app/create.html")


def create (request):
  

    if request.method == "POST":
        errors = data.objects.validate_create(request.POST)
        if errors:
            for err in errors:
                error(request, err)
            print(errors)
            return redirect('/display')
        else:
            
            request.method == 'POST'
            destination=request.POST["destination"]
            plan=request.POST["plan"]
            start_date= request.POST["start_date"]
            end_date= request.POST["end_date"]
           
            created=data.objects.get(id=request.session['id'])
            
            context = {
                'user': data.objects.get(id=request.session["id"]),
                'sd': start_date.date(),
                'ed':end_date.date(),
            } 

            trip.objects.create(destination=destination,plan=plan,start_date=start_date,end_date=end_date, created=created )
        return redirect ("/success", context)

def edit (request, show_id):
    print(trip.objects.filter(id=show_id))
    print(type(trip.objects.filter(id=show_id)))

    context = {
        'user': data.objects.get(id=request.session["id"]),
        "show" : trip.objects.get(id=show_id),
        "start" : trip.objects.get(id=show_id).start_date.strftime('%Y-%m-%d'),
    
        "end" : trip.objects.get(id=show_id).end_date.strftime('%Y-%m-%d'),


    } 
    print(type(context['start']))
    return render (request, "first_app/edit.html", context)
    
def show(request, show_id):
    context = {
        "show" : trip.objects.get(id=show_id),
        "people" : data.objects.get(id=show_id),
        'user': data.objects.get(id=request.session["id"]),
        'users_who_join': trip.objects.get(id=show_id).users_who_join.all()



    } 
    return render(request,"first_app/show.html", context)


def delete(request, show_id):
    x = trip.objects.get(id=show_id)
    x.delete()

    return redirect('/success')


def update (request, show_id):
    errors = trip.objects.validate_create(request.POST)
    id=show_id

    if (len(errors))>0:
        error(request, 'Invalid Please try again')
        return redirect("/display")
    else:
        x=trip.objects.get(id=show_id)
        
        x.destination=request.POST["destination"]
        x.start_date=request.POST["start_date"]
        x.end_date=request.POST["end_date"]
        x.plan=request.POST["plan"]
        x.save()
        error(request, 'Updated Sucessfully!!!')
    return redirect ("/success")



def join(request, show_id):
    trip.objects.get(id=show_id).users_who_join.add(data.objects.get(id=request.session['id']))


    return redirect('/success')

def remove(request, show_id):
    trip.objects.get(id=show_id).users_who_join.remove(data.objects.get(id=request.session['id']))


    return redirect('/success')