from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
from service.models import Service
from News.models import News

def newsDetails(request , news_id):
    newsDetails = News.objects.get(id = news_id)
    data = {
        'newsDetails' :  newsDetails
    }
    return render(request , "newsDetails.html" , data)

def homePage(request):
    newsData = News.objects.all();
    data = {
        'newsData' : newsData,
        'title': "Home Page",
        'content': "Welcome to my Django Project.",
        'names': ["Anto", "Nahid" , "Imtiaj"],
        'numbers': [34,54,545,6546,75,76,65,34],
        'friend_details' : [
            {'name' : "Anto" , 'phone' : '01903465436'},
            {'name' : "Shahrair" , 'phone': '01557393897'}
        ]
    }
    return render(request , "index.html" , data)

def aboutUs(request):
    output = 0
    if request.method == "GET":
        output = request.GET.get('output')
    data = {
        'title': "Home Page",
        'content': "Welcome to my Django Project.",
        'names': ["Anto", "Nahid" , "Imtiaj"],
        'numbers': [34,54,545,6546,75,76,65,34],
        'friend_details' : [
            {'name' : "Anto" , 'phone' : '01903465436'},
            {'name' : "Shahrair" , 'phone': '01557393897'}
        ],
        'output' : output
    }
    return render(request , "about-us.html" , data)


def submitForm(request):
    finalAns = 0;
    data = {}
    try:
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        finalAns = n1 + n2
        data = {
            'num1' : n1,
            'num2' : n2,
            'finalAns' : finalAns
        }
        
        return HttpResponse(finalAns)
    except:
        pass

def anotherFunction(request):
    return HttpResponse("<h1>This view from another function</h1>")

def anotherPageFunction(request):
    serviceData = Service.objects.all().order_by('service_title')
    # for a in serviceData:
    #     print(a)

    if request.method == "GET":
        st = request.GET.get('searchData')
        if st != None:
            serviceData = Service.objects.filter(service_title__icontains = st)

    data = {
        'serviceData' : serviceData
    }

    return render(request , "another-page.html" , data)


def courseDetails(request,courseId):
    return HttpResponse(f'<div style="display: flex; border:red 5px solid"><span style = "background: green; width:50%; text-align:center; color: white;"><h3 style = "margin-top: 40px;">This data from Dynamic URL</h3> </span>  <span><h1 style = "padding-left: 100px">{courseId}</h1></span></div> ')

def userFormGet(request):
    finalAns = 0;
    data = {}
    try:
        n1 = int(request.GET.get('num1'))
        n2 = int(request.GET.get('num2'))
        finalAns = n1 + n2
        data = {
            'num1' : n1,
            'num2' : n2,
            'finalAns' : finalAns
        }
    except:
        pass

    return render(request , "user-form-get.html", data)


def userFormPost(request):
    finalAns = 0
    fn = usersForm()
    data = {'form' : fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalAns = n1 + n2
            data = {
                'form': fn,
                'finalAns' : finalAns
            }
            url = "/about-us/?output={}".format(finalAns)
            return HttpResponseRedirect(url)
    except:
        pass

    return render(request , "user-form-post.html" , data)



def calculatorProject(request):
    data = {}
    try:
        val_1 = int(request.POST.get('val_1'))
        operator = request.POST.get('operator')
        val_2 = int(request.POST.get('val_2'))
        if(operator == "+"):
            ans = val_1 + val_2
        elif(operator == "-"):
             ans = val_1 - val_2
        elif(operator == "*"):
             ans = val_1 * val_2
        elif(operator == "/"):
             ans = val_1 / val_2
        
             
        data = {
            'first_val' : val_1,
            'second_val': val_2,
            'operator': operator,
            'output' : ans
        }
    except:
        pass
    return render(request , "calculator.html" , data)


def evenOdd(request):
    data = {}
    checker = ""
    try:
        if request.method == "POST":
            if request.POST.get('val_1') == "":
                return render(request , "even-odd.html" , {'error' : True})
            c = int(request.POST.get('val_1'))
            if(c%2):
                checker = "Odd"
            else:
                checker = "Even"
            data = {
                'val_1' : c,
                'output' : checker
            }
            

    except:
        pass
    return render(request , "even-odd.html" , data)


def markSheet(request):
    data = {}
    checker = ""
    try:
        if request.method == "POST":
            s_1 = eval(request.POST.get('s_1'))
            s_2 = eval(request.POST.get('s_2'))
            s_3 = eval(request.POST.get('s_3'))
            s_4 = eval(request.POST.get('s_4'))
            s_5 = eval(request.POST.get('s_5'))
            total = s_1 + s_2 + s_3 + s_4 + s_5
            per = (total * 100)/500
            division = ""
            if(per >= 60):
                division = "First"
            elif(per >= 45):
                division = "Second"
            elif(per >= 33):
                division = "Third"
            else:
                division = "Failed"

            data = {
                'subject_1' : s_1,
                'subject_2' : s_2,
                'subject_3' : s_3,
                'subject_4' : s_4,
                'subject_5' : s_5,
                'total' : total,
                'percentage' : per,
                'division' : division,
            }

    except:
        pass

    return render(request , "markSheet.html" , data)