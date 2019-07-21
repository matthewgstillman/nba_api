from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        request.session['count'] = request.session['count'] + 1
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
        args =  {
            # request.session['name'] = request.POST['name']
            # request.session['dojo_location'] = request.POST['dojo_location']
            # request.session['favorite_language'] = request.POST['favorite_language']
            # request.session['comment'] = request.POST['comment']
            # request.session['count'] = request.session['count']
        }
        return redirect('/result', args)
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')