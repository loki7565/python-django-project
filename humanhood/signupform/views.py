from django.http import HttpResponse
from django.shortcuts import render
from signupform.models import Signup

def signupform(request):
    return render(request, "signup_form.html")

def signup_data_entry(request):
    if request.method == 'POST':
        signup_fname = request.POST.get('fname')
        signup_lname = request.POST.get('lname')
        signup_email = request.POST.get('email')
        # signup_gender = request.POST.get('gender')
        signup_product = request.POST.get('product')
        signup_number = request.POST.get('number')

        try:
            submit_form = Signup(signup_fname=signup_fname, signup_lname=signup_lname, 
                                  signup_email=signup_email,
                                  signup_product=signup_product, signup_number=signup_number)
            submit_form.save()
            return HttpResponse("Data Successfully Inserted")
        
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
        
    else:
        return HttpResponse("Invalid Request Method.")