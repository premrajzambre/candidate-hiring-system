from django.shortcuts import render, get_object_or_404, redirect
from newquiz.models import Question
#from mainapp.models import applicant
from django.http import HttpResponse
#from quiz.utils import get_rank

def newquiz_home(request):
    question = Question.objects.first()
    return render(request, 'newquiz/newquiz_home.html', {'question': question})
#--------------------------------------------------------------------------------
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        if 'answers' not in request.session:
            request.session['answers'] = {}

        request.session['answers'][str(question.id)] = (
            request.POST.get('option')
        )
        request.session.modified = True
        next_question = question.get_next_question()

        if next_question:
            return redirect('newquiz:question_detail', question_id=next_question.id)
        else:
            return redirect('newquiz:newquiz_results')

    context = {
        'question': question,
        'options': question.options.all(),
        'nb_questions': Question.objects.count(),
        'question_number': question.get_number(),
    }
    return render(request, 'newquiz/question_detail.html', context)
#--------------------------------------------------------------------------------
def newquiz_results(request):
    total_questions = Question.objects.count()
    answered_questions = len(request.session.get('answers', {}))

    if answered_questions != total_questions:
        return redirect('newquiz:newquiz_home')

    score = 0
    for question in Question.objects.all():
        answer = request.session['answers'][str(question.id)]
        if question.is_correct(answer):
            score += 1

    score_percentage = int(score / total_questions * 100)
    rank = get_rank(score_percentage)
    del request.session['answers']

    #form=PassForm(request.POST or None)
    response = "Thanks for showing interest in us. We'll contact you shortly. Please click on button and enter your basic details."
    context = {
        'score': score_percentage,
        'title': rank['title'],
        'description': rank['description'],
        'response': response,
    }

    if score_percentage > 60:
        #em=form['email'].value()
        #applicant.objects.filter(pk=em).update(aptitude_score=score_percentage)
        return render(request, 'newquiz/results.html', context)
    else:
        return HttpResponse('Thank You for showing such a greatfull interest towards us. Better luck next time...!!!')
"""
    return render(request, 'newquiz/results.html', {
        'score': score_percentage,
        'title': rank['title'],
        'description': rank['description']
    })
"""
#--------------------------------------------------------------------------------
def get_rank(score_percentage):
    ranks = [
        [100, "Impressive!", "Wow! You are a genius."],
        [75, "Well done!", "You know more than most people!"],
        [50, "Not bad!", "Please improve your performance."],
        [25, "Uh oh!", "You seriously need to work on yourself"],
        [0, "Not good!", "Did you do it on purpose ??"],
    ]

    for rank in ranks:
        if rank[0] <= score_percentage:
            return {'title': rank[1], 'description': rank[2]}

    raise ValueError("Invalid score %s" % score_percentage)
