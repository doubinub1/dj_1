from django.shortcuts import render
from .models import UserMessage
# Create your views here.




def getform(request):
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print message.name
    if request.method == 'POST':
        name = request.POST.get('name','')
        message = request.POST.get('message','')
        address = request.POST.get('address','')
        email = request.POST.get('email','')
        usermessage =UserMessage()
        usermessage.name = name
        usermessage.message = message
        usermessage.address = address
        usermessage.email = email
        usermessage.save()


    return render(request,'message_form.html')
