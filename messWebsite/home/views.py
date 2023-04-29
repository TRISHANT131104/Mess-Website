from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate, File, Allocation, Student, RebateAutumnSem, RebateSpringSem
import pandas as pd
import datetime
from django.views.generic import TemplateView
import io
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_date
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.
def home(request):
    aboutInfo=About.objects.all()
    update=Update.objects.all()
    caterer=Caterer.objects.all()
    carousel=Carousel.objects.all()
    photos=Photos.objects.all()
    context={'about': aboutInfo, 'updates': update,'caterer':caterer,'carousel':carousel,'photos':photos}
    return render(request,'home.html',context)



def rules(request):
    rules=Rule.objects.all()
    shortRebates=ShortRebate.objects.all()
    LongRebates=LongRebate.objects.all()
    form=Form.objects.all()
    caterer=Caterer.objects.all()
    params={'rule':rules,'shortRebate':shortRebates,'longRebate': LongRebates,'form':form,'caterer':caterer}
   
    return render(request,'rules.html',params)


def caterer(request,name):
    caterer = Caterer.objects.get(name=name)
    context={'caterer':caterer}
    return render(request,'caterer.html',context)

# def kanaka(request):
#     caterer=Caterer.objects.all()
#     context={'caterer':caterer}
#     return render(request,'caterer2.html',context)

# def ajay(request):
#     caterer=Caterer.objects.all()
#     context={'caterer':caterer}
#     return render(request,'caterer1.html',context)

def links(request):
    """ allLinks=link.objects.all()
    context={'allLinks': allLinks} """
    caterer=Caterer.objects.all()
    form=Form.objects.all()
    context={'caterer':caterer,'form':form}
    return render(request,'links.html',context)

def cafeteria(request):
    caterer=Caterer.objects.all()
    cafeteria=Cafeteria.objects.all()
    context={'caterer':caterer,'cafeteria':cafeteria}
    return render(request,'cafeteria.html',context)

def contact(request):
    caterer=Caterer.objects.all()
    contact=Contact.objects.all()
    context={'caterer':caterer,'contact':contact}
    return render(request,'contact.html',context)

# def days(s,list):
#     total_days = 0
#     try:
#         count = Rebate.objects.filter(allocation_id = s).count()
#         for i in range(count):
#             rebate = Rebate.objects.filter(allocation_id = s)[i]
#             start_date = rebate.start_date
#             end_date = rebate.end_date
#             list.append([(start_date),(end_date)])
#             total_days += ((end_date-start_date).days)+1
#         return total_days
#     except Exception as e:
#         print(e)
#         return total_days
    
def count(start,end,sum):
    sum += ((end-start).days)+1
    return sum

def is_present_autumn(s):
    try:
        student = RebateAutumnSem.objects.get(email = str(s.email))
    except:
        print(Exception)
        student = RebateAutumnSem(
            email=str(s.email)
        )
        student.save()
    return student
def is_present_spring(s):
    try:
        student = RebateSpringSem.objects.get(email = str(s.email))
    except:
        print(Exception)
        print(2)
        student = RebateSpringSem(
            email=str(s.email)
        )
        student.save()
    return student    

def check(a,s,start,end,month):
    match month:
        case "january":
            student = is_present_spring(s)
            student.january = count(start,end,student.january)
            student.highTeaJanuary = a.high_tea
            if(student.january<=8):
                student.save(update_fields=["january","highTeaJanuary"])
                return 1
            if(start.month==1 and end.month==1):
                return 2
            else:
                return 0
        case "feburary":
            student = is_present_spring(s)
            student.feburary = count(start,end,student.feburary)
            student.highTeaFeburary = a.high_tea
            if(student.feburary<=8):
                student.save(update_fields=["feburary","highTeaFeburary"])
                return 1
            elif(start.month!=2 and end.month!=2):
                return 2
            else:
                return 0
        case "march":
            student = is_present_spring(s)
            student.march = count(start,end,student.march)
            student.highTeaMarch = a.high_tea
            if(student.march<=8):
                student.save(update_fields=["march","highTeaMarch"])
                return 1
            elif(start.month!=3 and end.month!=3):
                return 2
            else:
                return 0
        case "april":
            student = is_present_spring(s)
            student.april = count(start,end,student.april)
            student.highTeaApril = a.high_tea
            if(student.april<=8):
                student.save(update_fields=["april","highTeaApril"])
                return True
            elif(start.month!=4 and end.month!=4):
                return 2
            else:
                return False
        case "may":
            student = is_present_spring(s)
            student.may = count(start,end,student.may)
            student.highTeaMay = a.high_tea
            if(student.may<=8):
                student.save(update_fields=["may","highTeaMay"])
                return 1
            elif(start.month!=5 and end.month!=5):
                return 2
            else:
                return 0
        case "june":
            student = is_present_spring(s)
            student.june = count(start,end,student.june)
            student.highTeaJune = a.high_tea
            if(student.june<=8):
                student.save(update_fields=["june","highTeaJune"])
                return 1
            elif(start.month!=6 and end.month!=6):
                return 2
            else:
                return 0
        case "july":
            student = is_present_autumn(s)
            student.july = count(start,end,student.july)
            student.highTeaJuly = a.high_tea
            if(student.july<=8):
                student.save(update_fields=["july","highTeaJuly"])
                return 1
            elif(start.month!=7 and end.month!=7):
                return 2
            else:
                return 0
        case "august":
            student = is_present_autumn(s)
            student.august = count(start,end,student.august)
            student.highTeaAugust == a.high_tea
            if(student.august<=8):
                student.save(update_fields=["august","highTeaAugust"])
                return 1
            elif(start.month!=8 and end.month!=8):
                return 2
            else:
                return 0
        case "september":
            student = is_present_autumn(s)
            student.september = count(start,end,student.september)
            student.highTeaSeptember = a.high_tea
            if(student.september<=8):
                student.save(update_fields=["september","highTeaSeptember"])
                return 1
            elif(start.month!=9 and end.month!=9):
                return 2
            else:
                return 0
        case "october":
            student = is_present_autumn(s)
            student.october = count(start,end,student.october)
            student.highTeaOctober = a.high_tea
            if(student.october<=8):
                student.save(update_fields=["october","highTeaOctober"])
                return 1
            elif(start.month!=10 and end.month!=10):
                return 2
            else:
                return 0
        case "november":
            student = is_present_autumn(s)
            student.november = count(start,end,student.november)
            student.highTeaNovember = a.high_tea
            if(student.november<=8):
                student.save(update_fields=["november","highTeaNovember"])
                return 1
            elif(start.month!=11 and end.month!=11):
                return 2
            else:
                return 0
        case "december":
            student = is_present_autumn(s)
            student.december = count(start,end,student.december)
            student.highTeaDecember = a.high_tea
            if(student.december<=8):
                student.save(update_fields=["december","highTeaDecember"])
                return 1
            elif(start.month!=12 and end.month!=12):
                return 2
            else:
                return 0
        # case default:
        #     return "something"

def rebate(request):
    text=""
    list=[]
    try:
        allocation_id = Allocation.objects.get(roll_no__email = str(request.user.email))
        key = str(allocation_id.student_id)
    except Allocation.DoesNotExist:
        key = "Signed in account does not does not have any allocation ID"
    except Allocation.MultipleObjectsReturned:
        allocation_id = Allocation.objects.filter(roll_no__email = str(request.user.email)).first()
        key = str(allocation_id.student_id)
    if request.method =='POST' and request.user.is_authenticated:
            try:
                start_date = parse_date(request.POST['start_date'])
                end_date = parse_date(request.POST['end_date'])
                if(start_date.month == end_date.month):
                    diff = ((end_date-start_date).days)+1
                    diff2 = (start_date-datetime.date.today()).days
                    try:
                        Allocation.objects.get(student_id = request.POST['allocation_id'])
                        try:
                            a=Allocation.objects.get(roll_no__email = str(request.user.email), student_id = request.POST['allocation_id'])
                            s=Student.objects.filter(email = str(request.user.email)).first()
                            month = a.month
                            print(month)
                            # total_days = days(a,list)+diff
                            # print(total_days)
                            # print(list)
                            ch = check(a,s,start_date,end_date,month)
                            if(ch==2):
                                text = "Please fill the rebate of this month only"
                            elif(ch==0): 
                                text="You can only apply for max 8 days in a month"                            
                            else:
                                print(ch)
                                if((diff)<=7 and diff>=2 and diff2>=2):
                                    r = Rebate(
                                        email=request.user.email,
                                        allocation_id = a,
                                        start_date = request.POST['start_date'],
                                        end_date = request.POST['end_date'],
                                        approved=False
                                    )
                                    r.save()
                                    text="You have successfully submitted the form. Thank you"
                                else:
                                    text="Your rebate application has been rejected due to non-compliance of the short term rebate rules"
                        except Allocation.DoesNotExist:
                            text ="Email ID does not match with the allocation ID"
                    except Allocation.DoesNotExist:
                        text=" The asked allocation ID does not exist. Please enter the correct ID."
                else:
                    text="Please enter the rebate dates within this month only"       
            except Exception as e:
                print(e)
                text="Invalid Dates filled"  
    context = {'text': text, "key":key, "list": list}
    return render(request,"rebateForm.html",context)



def allocation(request):
    messages=""
    if request.method =='POST'and request.user.is_authenticated and request.user.is_staff :
        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )
        print(csv_data.head())
    
        for record in csv_data.to_dict(orient="records"):
            try:
                first_pref = str(record["first_pref"]).capitalize()
                second_pref = str(record["second_pref"]).capitalize()
                third_pref = str(record["third_pref"]).capitalize()
                high_tea = record["high_tea"]
                r = Student.objects.get(roll_no = record["roll_no"])    
                print(r)
                print("hi1")
                for pref in [first_pref,second_pref,third_pref]:
                    kanaka = Caterer.objects.get(name = "Kanaka")
                    ajay = Caterer.objects.get(name = "Ajay")
                    gauri = Caterer.objects.get(name = "Gauri")
                    if(pref == kanaka.name and kanaka.student_limit>0):
                        student_id=str(kanaka.name[0])
                        if(high_tea==True): student_id+="H"
                        student_id+=str(kanaka.student_limit) 
                        caterer_name = kanaka.name
                        kanaka.student_limit-=1
                        kanaka.save(update_fields=["student_limit"])
                        break 
                    elif(pref == ajay.name and ajay.student_limit>0):
                        student_id=str(ajay.name[0])
                        if(high_tea==True): student_id+="H"
                        student_id+=str(ajay.student_limit) 
                        caterer_name = ajay.name
                        ajay.student_limit-=1
                        ajay.save(update_fields=["student_limit"])
                        break
                    elif(pref == gauri.name and gauri.student_limit>0):
                        student_id=str(gauri.name[0])
                        if(high_tea==True): student_id+="H"
                        student_id+=str(gauri.student_limit) 
                        caterer_name = gauri.name
                        gauri.student_limit-=1
                        gauri.save(update_fields=["student_limit"])
                        break
                a = Allocation(
                    roll_no = r,
                    student_id = student_id,
                    month = record["month"],
                    caterer_name = caterer_name,
                    high_tea = high_tea,
                    first_pref = first_pref,
                    second_pref = second_pref,
                    third_pref = third_pref
                )
                a.save()
            except Exception as e:
                print(e)  
        messages="Form submitted. Please check the admin page."
    context={'messages':messages}            
    return render(request, "allocation.html",context)



def addAllocation(request):
    text="hi"
    caterers={'Kanaka','Gauri','Ajay'}
    context = {'text': text,'caterers':caterers}
    return render(request,"addAllocation.html",context)