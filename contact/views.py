from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['message']

        if user_id != 0:
            has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.warning(request, "You have already made inquiry about this car! Please wait until we get back to you.")
                return redirect('/cars/'+car_id)
        
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, firstname=firstname, lastname=lastname, 
        customer_need=customer_need, city=city, state=state, email=email, phone=phone, comment=comment)

        contact.save()
        
        messages.success(request, "Your request has been submitted! We will get back to you shortly.")
        return redirect('/cars/'+car_id)


    return render(request, 'contact/inquiry.html')