from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'receptionist/register.html')

#  def appoinment(request):
#      return render(request,'receptionist/appoinment.html')