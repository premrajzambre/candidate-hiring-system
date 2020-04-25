from django.shortcuts import render
from .models import Question

# Create your views here.
def quiz_start(request):
    choices = Question.CAT_CHOICES
    print(choices)
    return render(request, 'quiz/quiz_start.html', {'choices':choices})

def quiz_home(request):
    return render(request, 'quiz/quiz_home.html')

def questions(request , choice):
    print(choice)
    ques = Question.objects.filter(catagory__exact = choice)
    return render(request, 'quiz/questions.html', {'ques':ques})

def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Question.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score/total)*100
    return render(request, 'quiz/result.html', {'score':score, 'eff':eff, 'total':total})

def instructions(request):
    return render(request, 'quiz/instructions.html')

def contact(request):
    return render(request, 'quiz/contact.html')

def start(request):
    choices = Question.CAT_CHOICES
    print(choices)
    return render(request, 'quiz/start.html', {'choices':choices})