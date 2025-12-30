from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import UserAccount as user_a
from .models import customeradd as customer_a
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=user_a.objects.get(email=email,password=password)
            if user.password==password:
                return redirect('dashboard')
            else:
                return HttpResponse('Invalid email or password')              
        except user_a.DoesNotExist:
            return HttpResponse('Invalid email or password')
    
    return render(request, 'login.html')
    # return HttpResponse("Hello, welcome to the shop!")
def createaccount(request):
    if request.method == 'POST':
        # Process the form data here
        username = request.POST.get('name')
        state=request.POST.get('state')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        aadhaar=request.POST.get('aadhaar')
        pin=request.POST.get('pin')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            user = user_a(username=username,email=email,phone=phone,password=password,state=state,addhar=aadhaar,pin=pin)
            user.save()
            send_mail("registration","Thank you for registering",settings.EMAIL_HOST_USER,[email])
            # return redirect('dashboard')
            return HttpResponse('Account created successfully')
            
        else:
            return HttpResponse('Password not matched')
    

    return render(request, 'create_account.html')

# @login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def customer_details(request):
    if request.method == 'POST':
        accnumber=request.POST.get('accnumber')
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        pan=request.POST.get('pan')
        aadhaar=request.POST.get('aadhaar')
        amount=request.POST.get('amount')
        
        # Check if accnumber already exists
        if customer_a.objects.filter(accnumber=accnumber).exists():
            messages.warning(request, "Account number already exists!")
            return redirect(customer_details)

        customer=customer_a(accnumber=accnumber,name=name,phone=phone,pan=pan,aadhaar=aadhaar,amount=amount)
        customer.save()

        return redirect (customer_details)
    
      
        
    
    accounts = customer_a.objects.all()
    return render(request, 'customaradd.html', {'accounts': accounts})     
        # return HttpResponse('Customer details added successfully')

    # return render(request, 'customaradd.html')


def delete_customer(request, accnumber):
    if request.method == 'GET':
        customer = customer_a.objects.get(accnumber=accnumber)
        customer.delete()      # Delete immediately
    return redirect('customer_details')   # Refresh page


    # if request.method == "POST":
    #     customer.delete()
    #     return redirect('customer_details')

    # return render(request, "confirm_delete.html", {"customer": customer})
    # return redirect (request,'customeradd.html', {'accounts': accounts})
    # return redirect('customer_details')

def edit_customer(request, accnumber):
        customer = customer_a.objects.get(accnumber=accnumber)
        if request.method == 'POST':
            
            customer.name = request.POST.get('name')
            customer.phone = request.POST.get('phone')
            customer.pan = request.POST.get('pan')
            customer.aadhaar = request.POST.get('aadhaar')
            customer.amount = request.POST.get('amount')
            customer.save()
            return redirect('customer_details')
        return render(request, 'edit_customar.html', {'customer': customer})

def logout(request):
    return redirect('home')
