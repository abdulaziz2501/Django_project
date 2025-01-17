from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
# Create your views here.


# def customer_form(request):
#     form=CustomerForm(request.POST)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect('customer_lists')
#     ctx={
#         'form':form

#     }
#     return render(request, 'index.html', ctx)

# def customer_list(request):
#     customers=Customer.objects.all()
#     ctx={
#         'customers':customers
#     }
#     return redirect(request, 'index.html', ctx)

def main(request):
    if request.POST:
        model = Customer()
        model.full_name = request.POST.get('full_name','')
        model.user_name = request.POST.get('user_name','')
        model.email = request.POST.get('email', '')
        model.phone_number = request.POST.get('phone_number', '')
        model.password = request.POST.get('password', '')
        model.confirm_password = request.POST.get('confirm_password', '')
        # model.exist = request.POST.get('exist', '')
        model.save()
        print(request.POST)
    return render(request,'index.html')