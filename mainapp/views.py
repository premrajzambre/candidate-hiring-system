from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage
from .forms import ApplicationForm
from .forms import CanPass, ApplicantSearchForm
from django.http import HttpResponse, JsonResponse
from .models import applicant
from rest_framework.views import APIView
from rest_framework.response import Response
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
        path = path[1:]
        print (path)
    return render(request, 'mainapp/upload.html', context)

def dashboard(request):
	return render(request, 'mainapp/dashboard.html', {})

#qw=applicant.objects.all().count()
#dte=applicant.objects.latest('date_of_interview')
#dtecount=applicant.objects.filter(date_of_interview__iexact=dte).count()

def get_data(request, *args, **kwargs):
    data = {
    "selected":100,
    "rejected":10,
    }
    return JsonResponse(data)

class hr_admin_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/hr_admin.html', {'selected': 100})

class ChartView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = applicant.objects.all().count()
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items : [qs_count, 819, 753, 555, 652, 300]
        data = {
        "labels":labels,
        "default":default_items,
        }
        return Response(data)

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter(request):
    qs = applicant.objects.all()
    title_contains_query = request.GET.get('title_contains')
    date_of_interview = request.GET.get('date_of_interview')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(email__iexact=title_contains_query)

    if is_valid_queryparam(date_of_interview):
        qs = qs.filter(date_of_interview__gte=date_of_interview)

    return qs

def history(request):
    qs = filter(request)
    """title_contains_query = request.GET.get('title_contains')
    if title_contains_query != '' and title_contains_query is not None:
        qs = applicant.objects.get(hr_id__iexact=title_contains_query)"""
    #context = {'queryset': qs}
    #title = 'List of all items'
    #form = ApplicantSearchForm(request.POST or None)
    context = {'queryset': qs,}
    if request.method == 'POST':
        queryset = applicant.objects.all().filter(hr_id__iexact=request.POST.get('hr_id'),date_of_interview__icontains=request.POST.get('date_of_interview'))
        context = {
        'queryset': queryset,
        'form': form,
        }
    return render(request, 'mainapp/past.html', context)

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            #form.save()
            #return HttpResponse('You filled the form successfully. We will contact you shortly. Thank You...!!!')
            #return render(request, 'authenticate/home.html',{})
            #return render(request, 'newquiz/newquiz_home.html')
            return redirect('/newquiz/newquiz_home')
    else:
        form = ApplicationForm()
    context = {'form': form}
    return render(request, 'mainapp/application.html', context)

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

def new_process(request):
	return render(request, 'mainapp/new_process.html', {})
