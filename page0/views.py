from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
import pickle
# Create your views here.

def verify(ques, ans, request):
    f = open("data.dat", "rb")
    s = []
    while True:
        try:
            s.append(pickle.load(f))
        except EOFError:
            break
    for questions in s:
        for q, a in questions.items():
            if q == ques:
                if a[-1] == ans:
                    request.session['score'] += 2
                    return True
                else:
                    request.session['score'] -= 1
                    return a[-1]

def home(request):
    if request.method == "POST":
        if request.POST.get('name') == '__create':
            return HttpResponseRedirect('/create')
        else:
            request.session['username'] = request.POST.get('name')
            request.session['count'] = 0
            request.session['score'] = 0
            return HttpResponseRedirect("/play")
    if request.session.is_empty():
        del request.session['username']
        del request.session['count']
        del request.session['score']
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

def play(request):
    s = []
    f = open("data.dat", "rb")
    i = 0
    while True:
        try:
            s = pickle.load(f)
            if i == request.session['count']:
                break
            i+=1
        except EOFError:
            return HttpResponseRedirect('/score')
    q = list(s.keys())[0]
    a = list(s.values())[0]
    template = loader.get_template("play.html")
    return HttpResponse(template.render({'q': q, 'a': a, 's': request.session['score'], 'c': i, "name": request.session['username']}, request))

def score(request):
    template = loader.get_template('score.html')
    context = {
        'username': request.session['username'],
        's': request.session['score'],
        'c': request.session['count']
    }
    return HttpResponse(template.render(context, request))

def receive(request):
    if request.method == 'POST':
        request.session['count'] += 1
        v = verify(request.POST.get('question'), request.POST.get('answer'), request)
        if v == True:
            messages.add_message(request, messages.SUCCESS, 'Correct Answer')
        else:
            messages.add_message(request, messages.ERROR, f'Wrong Answer\nThe Answer Was {v}')
        return HttpResponseRedirect('play')

def upload_all_ques(request):
    f = open("data.dat", 'rb')
    s = []
    while True:
        try:
            s.append(pickle.load(f))
        except EOFError:
            break
    template = loader.get_template("list.html")
    return HttpResponse(template.render({'q': s}, request))

def create(request):
    if request.method == "POST":
        data = request.POST
        ques = {data.get('question'): [
            data.get('option1'),
            data.get('option2'),
            data.get('option3'),
            data.get('option4'),
            data.get('answer')
        ]}
        f = open("data.dat", "ab")
        pickle.dump(ques, f)
        f.close()
        return HttpResponse("Got The Question")
    template = loader.get_template("create.html")
    return HttpResponse(template.render({}, request))