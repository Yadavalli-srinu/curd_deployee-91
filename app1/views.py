from django.shortcuts import render,redirect

from app1.models import employee
from app1.forms import employee_form
def details(request):
    data=employee.objects.all()
    content={
        "data":data
    }
    return render(request,'frontend_app1/table.html',content)

def form_details(request):
    if request.method == "POST":
        form = employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("table101")
    else:
        form = employee_form()
    
    content = {
        "form": form
    }
    return render(request, "frontend_app1/form.html", content)