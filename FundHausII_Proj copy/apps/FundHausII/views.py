
from django.shortcuts import render, redirect
from .models import User, Project
# Create your views here.
def index(request):
    return render(request, 'FundHausII/index.html')

def projects(request):
    projects = Project.objects.all()
    context ={
        'projects': projects
    }
    return render(request, 'FundHausII/projects.html', context)

def register(request):
    #print request.POST
    if request.method == 'POST':
        messages = User.objects.register(request.POST)
        #Above line might be postData
    if not messages:
        print "No messages! Success!"
        # fetch user id and name via email
        user_list = User.objects.all().filter(email=request.POST['email'])
        request.session['id'] = user_list[0].id
        request.session['name'] = user_list[0].firstName
        return redirect('/users')
    else:
        request.session['messages'] = messages
        print messages
    return redirect('/signup')

def newproject(request):
    #print request.POST
    name = request.session['name']
    print name
    if request.method == 'POST':
        print request.POST
        messages = Project.objects.createproject(request.POST)
        #Above Line Might Be Post postData
    if not messages:
        print "No messages! Success!"
        #fetch project id and name using title
        projectList = Project.objects.all().filter(title=request.POST['title'])
        return redirect('/projects')
    else:
        request.session['messages'] = messages
        print messages
    return redirect('/projects')

def login(request):
    users = User.objects.all()
    postData = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    if request.method == 'POST':
        messages = User.objects.login(request.POST)
    if not messages:
        print "No messages! Success!"
        user_list = User.objects.all().filter(email=request.POST['email'])
        request.session['id'] = user_list[0].id
        request.session['name'] = user_list[0].firstName
        return redirect('/projects')
    else:
        request.session['messages'] = messages
        return redirect('/')

def signin(request):
    return render(request, 'FundHausII/signIn.html')

def signup(request):
    return render(request, 'FundHausII/signUp.html')

def users(request):
    users = User.objects.all()
    context={
        'users': users
    }
    return render(request, 'fundHausII/users.html', context)

def projects(request):
    projects = Project.objects.all()
    users = User.objects.all()
    context={
        'projects': projects,
        'users': users
    }
    return render(request, 'fundHausII/projects.html', context)

def project(request, id):
    # name = request.session['name']
    # print "{} is the name I Want to print!".format(name)
    users = User.objects.all()
    # userdonations = User.objects.donations.all().filter(gte=1)
    # donations = Project.objects.donations.all().filter(id=id)
    projects = Project.objects.all()
    project = Project.objects.all().filter(id=id)
    print project
    # if Project.donations == None:
    #     Project.donations = 0
    # else:
    #     Project.donations = Project.progress.filter(id=id)
    context={
        'projects': projects,
        'project': project,
        # 'donations': donations,
        # 'userdonations': userdonations,
        'users': users,
        'id': id
    }
    return render(request, 'fundHausII/project.html', context)

def donate(request, id):
    # projects = Project.objects.all()
    project = Project.objects.all().filter(id=id)
    context={
        # 'projects': projects,
        'project': project,
        'id': id
    }
    return render(request, 'fundHausII/donate.html', context)

def newdonation(request):
    currentuser = request.session['name']
    print currentuser
    users = User.objects.all()
    projects = Project.objects.all()
    #Attempt to change above line to project singularly using id parameter
    # current_project = Project.objects.all().filter(id=id)
    # print current_project
    donations = []
    donors = []
    #print request.POST
    if request.method == 'POST':
        messages = Project.objects.donate(request.POST)
        User.objects.donor = request.session['name']
        print "Donor is: {}".format(User.objects.donor)
        #Above Line might be postData
    if not messages:
        print "No Errors! Sucess!"
        donor = request.session['name']
        donors.append(donor)
        print donors
        donation = request.POST['donation']
        donations.append(donation)
        donations.append(str(donor) + " - " + str(donation))
        print donations
        context ={
            'donors': donors,
            'currentuser': currentuser,
            'donations': donations,
            'donation': donation,
            'users': users
        }
        return redirect('/projects', context)
    else:
        request.session['messages'] = messages
        print messages
    return redirect('/projects')

def trending(request):
    trending_projects = Project.objects.all().order_by('goal')
    context={
        'trending_projects': trending_projects
    }
    return render(request, 'fundHausII/projects.html', context)

def createproject(request):
    return render(request, 'fundHausII/createProject.html')

def logout(request):
    request.session.clear()
    return redirect('/')