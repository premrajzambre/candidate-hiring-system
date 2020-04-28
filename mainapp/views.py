from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import ApplicationForm
from .forms import CanPass
# Create your views here.
path = "as"
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        global path
        path = fs.url(name)
        print (path)
    return render(request, 'mainapp/upload.html', context)

def dashboard(request):
	return render(request, 'mainapp/dashboard.html', {})

def hr_admin(request):
	return render(request, 'mainapp/hr_admin.html', {})

def history(request):
    import pandas as pd
    global path
    #path = 'C:\\Users\\premr\\BE Project\\selected1.csv'
    data = pd.read_csv(path)
    data_html = data.to_html()
    context = {'loaded_data': data_html}
    return render(request, 'mainapp/history.html', context)

def user_application(request):
    form = ApplicationForm()
    #email = form.cleaned_data['email']
    #full_name = form.cleaned_data['full_name']
    #print(email,full_name)
    return render(request, 'mainapp/application.html', {'form':form})

def can_pass(request):
    sub = forms.CanPass()
    #global score
    #global total
    #eff = (score/total)*100
    #global eff
    #print (eff)
    #if eff >= 60:
    if request.method == 'POST':
        sub = forms.CanPass(request.POST)
        subject = 'Candidate Hiring System | Congratulations'
        message = 'Dear Candidate,\n\tCongratulations! We are glad to inform you that we will be taking your candidature forward in the Selection process based on your performance in the online assessment.\n Click the link below to fill some primary details http://localhost:8000/mainapp/application \n\n\n\t\t Sent from candidate_hiring_system project'
        recepient = request.POST['email']
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.success(request, ('Email sent successfully.'))
        return render(request, 'home')
    return render(request, 'quiz/can_pass.html', {'form':sub})
