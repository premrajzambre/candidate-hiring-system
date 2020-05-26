from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage
from .forms import ApplicationForm, Salaryprediction, UpinfoForm
from .forms import mailsearch, ApplicantSearchForm
from django.http import HttpResponse, JsonResponse
from .models import applicant
from posts.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from django.db.models import Q
from candidate_hiring_system.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

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
        #qs_count = applicant.objects.all().count()
        ob=applicant.objects.filter(date_of_interview__icontains='').order_by('-date_of_interview').first()
        #print(ob)
        dt=applicant.objects.values_list('date_of_interview', flat=True).get(pk=ob)
        #print(we)
        tc=applicant.objects.filter(date_of_interview=dt).count()
        sc=applicant.objects.filter(Q(date_of_interview__gte=dt), Q(category=1)).count()
        rj=tc-sc
        labels= ['Total Applicants', 'Selected', 'Rejected']
        default_items = [tc, sc, rj]
        data = {
            "labels":labels,
            "default":default_items,
        }
        return Response(data)

class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainapp/statistics.html', {'selected': 100})

def history(request):
    form = ApplicantSearchForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        hr=form['hr_id'].value()
        #print(hr)
        dt=request.POST.get('date_of_interview')
        #print(dt)
        if hr != '' and dt != '':
            queryset = applicant.objects.all().filter(hr_id__iexact=form['hr_id'].value(),date_of_interview__icontains=request.POST.get('date_of_interview'))
        elif hr != '' and dt == '':
            queryset = applicant.objects.all().filter(hr_id__iexact=hr)
        elif hr == '' and dt !='':
            queryset = applicant.objects.all().filter(date_of_interview__iexact=dt)
        elif hr == '' and dt == '':
            queryset = applicant.objects.all().filter(technical_score=0)
        #queryset = applicant.objects.all().filter(hr_id__iexact=form['hr_id'].value(),date_of_interview__icontains=request.POST.get('date_of_interview'))
        context = {
        'queryset': queryset,
        'form': form
        }
    return render(request, 'mainapp/past.html', context)

def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    context = {'form': form}
    return render(request, 'mainapp/application.html', context)

def salary(request):
    if request.method == 'POST':
        form = Salaryprediction(request.POST)
        if form.is_valid():
            level=form.cleaned_data['level']
            print(level)
            ans=salarystatus(level)
            messages.success(request, "Your salary range is from {} Lpa to {} Lpa".format(ans[0],ans[1]))
            #print(ans)
    form=Salaryprediction()
    context={
        'form':form
    }
    return render(request, 'mainapp/salary.html', context)

def salarystatus(X):
    try:
        salmdl = joblib.load('media/salary_predict.pkl')
        y_pred=salmdl.predict(X)
        y_pred=y_pred[0]
        s_min=(int)(y_pred-100000)/100000
        s_min=(int)(s_min)
        s_max=(y_pred+100000)/100000
        s_max=(int)(s_max)
        print(y_pred)
        print(s_min)
        print(s_max)
        return (s_min,s_max)
    except ValueError as e:
        return (e.args[0])

pst = '0'
def new_process(request):
    vc=Post.objects.filter(job_status__iexact='Active').values_list('job_title', flat=True)
    if request.method =='POST':
        global pst
        pst=request.POST.get('Job_post')
        return redirect('/mainapp/interview')
    context = {
        'vacancies':vc
    }
    return render(request, 'mainapp/new_process.html',context)

def interview(request):
    global pst
    post=pst
    vc=Post.objects.values_list('vacancy', flat=True).get(job_title__iexact=pst)
    form = mailsearch(request.POST or None)
    context = {
        'post':post,
        'vacancies':vc,
        'form':form
    }
    """ml=mail(request)
    print(ml)"""
    data = applicant.objects.all().filter(Q(technical_score=0), Q(job_post=post))
    context = {
        'post':post,
        'vacancies':vc,
        'data':data
    }
    return render(request, 'mainapp/interview.html', context)

def update_candidate(request, pk):
    ml = applicant.objects.get(email=pk)
    form = UpinfoForm(instance=ml)

    if request.method=='POST':
        form = UpinfoForm(request.POST, instance=ml)
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            myDict = (request.POST).dict()
            df=pd.DataFrame(myDict, index=[0])
            #print(df)
            ans=approvalsuggest(df)[0]
            print(ans)
            if ans == 1:
                messages.success(request, "Suggestion : Select")
            else:
                messages.success(request, "Suggestion : Reject")

    context = {
        'form':form,
    }
    return render(request, 'mainapp/update_candidate.html', context)

def approvalsuggest(df):
    try:
        scaler = joblib.load('media/i_scaler.pkl')
        model = joblib.load('media/i_predict.pkl')
        X = ['aptitude_score', 'technical_score', 'personality_score','average_score']
        y = 'category'
        df_sca = scaler.transform(df[X])
        y_predict = model.predict(df_sca)
        #print(y_predict)
        #if y_predict == 1:
        #    ans = 'Select'
        #elif y_predict == 0:
        #    ans = 'Reject'
        return y_predict
    except ValueError as e:
        return (e.args[0])

def invitation(request):
    dt=applicant.objects.values_list('email', flat=True).get(technical_score=0)
    if request.method == 'POST':
        subject = 'Candidate Hiring System | Congratulations'
        message = request.POST.get('msg')
        recepient = dt
        send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.success(request, ('Invitation sent successfully.'))
        return redirect('/mainapp/hr_admin')
    return render(request, 'mainapp/invitation.html',{})

def temp(request):
    #import pandas as pd
    #data = pd.read_csv('media/Salary.csv')
    #data_html = data.to_html()
    #context = {'loaded_data': data_html}

    return render(request, 'mainapp/temp.html', {})

def abouta(request):
	return render(request, 'mainapp/about_admin.html', {})

"""def jobportal(request):
	return render(request, 'mainapp/jobportal.html', {})
"""
