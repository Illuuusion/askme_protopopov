import copy

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

QUESTIONS = [
    {
    'title': f'Title {i}',
    'id': i,
    'text': f'This is text for question {i}'
  } for i in range(1, 30)
]

TAGS = [
    {
    'title': f'Tag {i}',
    'id': i,
    'text': f'This is text for tag {i}'
    }for i in range(1, 8)
]

def paginate(object_list, request, per_page=5):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(object_list, 5)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def index(request):
    page = paginate(QUESTIONS, request)
    return render(
        request, 'index.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page = paginate(hot_questions, request)
    return render(
        request, 'hot.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def question(request, question_id):
    one_question = QUESTIONS[question_id - 1]
    return render(
        request, 'question.html',
        context={'question': one_question}
    )

def ask(request):
    return render(
        request, 'ask.html',
    )

def tag(request, tag_id):
    curr_tag = TAGS[tag_id]
    return render(
        request, 'tag.html',
        context={'tag': curr_tag}
    )

def login(request):
    return render(
        request, 'login.html',
    )

def register(request):
    return render(
        request, 'register.html',
    )

def settings(request):
    return render(
        request, 'settings.html',
    )