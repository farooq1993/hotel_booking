from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.db.models import Q
from .serializer import *
from .models import *
from . forms import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
import razorpay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import date, datetime
from django.contrib.auth import logout





# Create your views here.
# @api_view(['post'])
def index(request):
    return render(request, 'index.html')
    # if request.method == 'POST':
    #     serializer = qgeneratorserializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
def about(request):
    return render (request, 'about.html')


def ourtourse(request):
    return render(request, 'tours.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    #bookplace=tours.objects.get(id=book_id)
    return render(request, 'reservation.html')

def alltourse(request):
    alltour=Tours.objects.all()
    return render (request, 'main.html',{"alltour":alltour})


# for view single record 
def toursview(request, id):
    obj=Tours.objects.get(id=id)
    
    return render (request, 'book.html', {'obj':obj})

# from this function User will create account
def user(request):
    if request.method=='POST':
        alpha='abcdefgHIGKLMN'
        num='123456789'
        char='*=&%$#@'
        ganrete=alpha+num+char
        print(random.choice(ganrete))
        # random_username=random.random(alpha_numerics)
        username=request.POST['username']
        # email=request.POST['email']
        password=make_password(request.POST['password'])
        print(password)
        create=User.objects.create_user(username=username, password=password)
        # create=creatuser(username=username, password=password)
        create.save()
        print('user created', create)
        return redirect('Login')
    return render(request, 'createaccount-2.html')

# For user Login 
def Login(request):
    #book=Tours.objects.filter(id=id)
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alltourse')
        else:
            return HttpResponse("<h2>Login Not Possible</h2>")
    return render (request, 'login-2.html')


def logout_view(request):
    logout(request)
    return redirect("/")

#for tour booking 
@login_required(login_url='Login')
def bookingform(request,id):
    room_number=rooms.objects.all()
    obj=Tours.objects.filter(id=id).first()
    
    if request.method=='POST':
        user_name=User.objects.get(user=user.request)
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        checkindate=request.POST['checkindate']
        checkoutdate=request.POST['checkoutdate']
        numberofadult=request.POST['numberofadult']
        numberofrooms=request.POST['numberofrooms']
        hote_add=Tours.objects.get(id=id)
        date_format = "%Y/%m/%d"
        a = datetime.strptime(checkindate, "%Y-%m-%d")
        b = datetime.strptime(checkoutdate, "%Y-%m-%d")
        total_days = (b - a).days

        amount=float(total_days*float(obj.amount))
        book=tourbooking.objects.create(user_name=user_name,name=name, phone=phone, email=email, checkindate=checkindate, checkoutdate=checkoutdate, 
        numberofadult=numberofadult,numberofrooms=numberofrooms,amount=amount,  hote_add=hote_add)
        mydict={'name':name,
        'checkindate':checkindate,
        'checkoutdate':checkoutdate,
        'hote_add':hote_add}
        book.save()
        print(numberofadult)
        
        # For Booking conformation email 
        html_template='email.html'
        html_message=render_to_string(html_template, context=mydict)
        subject="Hotel Booking"
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[email]
        message=EmailMessage(subject, html_message,email_from, recipient_list)
        message.content_subtype='html'
        message.send()

        return redirect('/payment/'+str(book.id))
    return render(request, 'reservation.html', {"obj":obj, 'room_number':room_number})

# this is for payment collect Function 
def payment(request,id): # id of sigle booking item get and payment
    print(request)
    #single_tour=tourbooking.objects.filter(id=id)

    if request.method=='POST':
        name = request.POST.get('name')

        book= tourbooking.objects.get(id=id)
        amt=book.amount.amount
        # print(amt)
        amount = amt * 100

        # amount = 50000
        client = razorpay.Client(auth=('rzp_live_ObeJRPPN5M7S33', 'YHHbfU27sWKXuCoVZazKnVkp')) # payment Gateway API key
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
        data = {
            "name" : name,
            "merchantId": "",
            "amount": amount,
            "currency" : 'INR' ,
           # "orderId" : razorpay_order["id"],
            }
    book= tourbooking.objects.get(id=id)
    amt=book.amount
    chk=book.checkindate
    chkout=book.checkoutdate
    # print(amt)
    amount = amt * 100
    data = {
        "amount": amount,
        "chk":chk,
        "chkout":chkout,
       # "orderId" : razorpay_order["id"],
        }
    print(data)
    return render (request, 'payment.html',data)



# for search 
def search(request):
    if request.method=='POST':
        searched=request.POST['search']
        checkin=request.POST['check_in']
        checkout=request.POST['check_out']
        print("search", searched)
        alltour=Tours.objects.filter(Q(hotel_name__contains=searched) | Q(amount__contains=searched)  | Q(availble_date__contains=checkin))
        print(alltour)
        #pricerange=Tours.objects.aaggregate(Max('amount'))
        #print('Price range',pricerange)
        ctx = {
            "location": alltour,
            "search": searched
        }
        return render (request, 'search-2.html', ctx)
    else:
        return render (request, 'search-2.html')
    #return render (request, 'search-2.html')



@login_required(login_url='Login')
def user_booking_details(request):
    bookinghistory=tourbooking.objects.filter(user_name=request.user)
    print("user booking history",bookinghistory)
    user = request.user
    return render(request, 'booking_history.html', {'bookinghistory': bookinghistory})
    


def deals(request):
    hotdeal=weekenddeals.objects.all()
    return render(request, 'deals.html', {'hotdeal':hotdeal})

def favoriteplace(request):
    #fav=favoritedestination.objects.filter(id=id).first()
    fav=favoritedestination.objects.all()
    return render (request, 'favoriteplace.html', {'fav':fav})

def filtersearch(request, hotel_rating):
    fil_search=Tours.objects.filter(hotel_rating=hotel_rating)
    return render(request, 'search-2.html', {'fil_search':fil_search})

@login_required(login_url='Login')
def updatehotel(request):
    hotel_obj=Tours.objects.filter(user.request==user.request)

    if request.method=="POST":
        pass
    
    return render (request,'hotel.html',{'hotel_obj':hotel_obj})

# #@api_view(['get'])
# def team(request):
#     return render(request, 'team.html')
#     # if request.method == 'GET':
#     #     transformer = qgenerator.objects.all()
#     #     serializer = qgeneratorserializer(transformer, many=True)
#     #     return Response(serializer.data)


# def contact(request):
#     if request.method == "POST":
#         Name = request.POST["name"]
#         PhoneNumber = request.POST["Phone"]
#         email = request.POST["Email"]
#         message = request.POST["Message"]

#         sendmail=send_mail(message,PhoneNumber,Name,['saviofenandes@karyarobotics.com'], fail_silently=True)
#         print("----------")
#         print(sendmail)
#         return redirect("/")
#     return render(request, "contact.html")

# def all_data(request):
#     data=email_post.objects.all()
#     return render(request, 'test.html', {'data':data})