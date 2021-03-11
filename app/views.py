from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html') 
def contact(request):
    return render(request,'contact.html')   
def doctors(request):
    return render(request,'doctors.html')
def services(request):
    return render(request,'services.html') 
def blog_single(request):
    return render(request,'blog-single.html')   
def about(request):
    return render(request,'about.html')           
def Appointment(request):
    o=Appointment.objects.all()
    con={
        'o':o
    }
    return render(request,'index.html',con)    