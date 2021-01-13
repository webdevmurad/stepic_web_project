from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')



def question_list(request):
    qs = Question.objects.all()
    qs = self.order_by('-id')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('question_list') + '?page='

    return render(request, 'list.html', {
        'questions': page.object_list,
        'page': page,
    })

def popular(request):
    qs = Question.objects.all()
    qs = self.order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'list_rating.html', {
        'questions': page.object_list,
        'page': page,
    })

def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'detail.html', {
        'question': question,
    })