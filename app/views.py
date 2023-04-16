from django.shortcuts import render

# Create your views here.from app.models import *

def display_dept(request):
    LOD=Department.objects.all()
    d={"dept":LOD}
    return render(request,'display_dept.html',context=d)    

def display_emp(request):
    LOE=Worker.objects.all()
  
    LOE=Worker.objects.filter(sal__lt=1000)
    LOE=Worker.objects.exclude(sal=800)
    LOE=Worker.objects.filter(sal__lt=2500)
    LOE=Worker.objects.filter(sal__gt=1000)
    LOE=Worker.objects.filter(sal__gte=1000)
    LOE=Worker.objects.filter(sal__lte=2500)
    
    
    LOE=Worker.objects.filter(hiredate__year='1881')
    LOE=Worker.objects.filter(hiredate__month='5')
    LOE=Worker.objects.filter(hiredate__day='2')
    LOE=Worker.objects.all()
    
    
    LOE=Worker.objects.filter(ename__startswith='A')
    LOE=Worker.objects.filter(ename__startswith='s')
    LOE=Worker.objects.filter(ename__endswith='n')
    LOE=Worker.objects.filter(ename__in=('ALLEN','SMITH'))
    LOE=Worker.objects.filter(ename__contains='A')
    LOE=Worker.objects.filter(ename__regex='[a-zA-Z]{4}')
    d1={"work":LOE}
    return render(request,'display_emp.html',context=d1)
    
    
    
def updating_data(request):
    
    Worker.objects.filter(ename="ALLEN").update(sal=3400)
    d1={"work":Worker.objects.all()}
    return render(request,'display_emp.html',context=d1)

def deleting_data(request):
    Worker.objects.filter(ename="ALLEN").delete()
    d1={"work":Worker.objects.all()}
    return render(request,'display_emp.html',context=d1)
def upadate_dept(request):
    TO=Department.objects.get(dname="Sales")
    TO.save()
    Department.objects.update_or_create(dname="HR department",default={'dept_no':'20','loc':'india'})
    d={"dept":Department.objects.all()}
    return render(request,'display_dept.html',context=d)    

    
                                        

    
    
    
    
    
    