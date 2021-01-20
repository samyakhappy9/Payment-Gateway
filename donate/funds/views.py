from django.shortcuts import render
from .forms import DonateForm
import random
from django.conf import settings 
from django.core.mail import send_mail
# Create your views here.
def home(request):
    form = DonateForm()
    content = {'forms':form}
    return render(request, 'home.html', content)

def donate(request, *args, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    amount = request.POST.get('amount')
    number = request.POST.get('mobile')
    orderid = random.randint(100000, 9999999)
    asd = (int(amount) *100)
    content = {'amount':asd, 'number':number, 'id':orderid, 'name':name, 'email':email}
    subject = ' Grow Plant Foundation'
    message = f"Grow Plant Foundation\n Hi {name} thank you for Donation in Grow Plant Foundation. \n Amount = {amount} \n Payment id = {orderid}"
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [email ] 
    send_mail( subject, message, email_from, recipient_list ) 
    return render(request, 'donate.html', content)

def sucess(request, *args, **kwargs):
    
    return render(request, 'success.html')