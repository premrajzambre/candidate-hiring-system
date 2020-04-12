from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
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
