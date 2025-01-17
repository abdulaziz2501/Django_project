from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
# Create your views here.


def customer_form(request):
    form=CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect('customer_lists')
    ctx={
        'form':form

    }
    return render(request, 'index.html', ctx)

def customer_list(request):
    customers=Customer.objects.all()
    ctx={
        'customers':customers
    }
    return redirect(request, 'index.html', ctx)