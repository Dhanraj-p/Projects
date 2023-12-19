from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ecom.models import items
from ecom.models import product
from ecom.models import productcategory
from ecom.models import categorizer

def home(request):
    return render(request,"home.html")

def sdta(request):
    return render(request,"employee.html")   

def store(request):
    if request.method=="POST":
        eid=request.POST['employee_id']
        na=request.POST['name']
        em=request.POST['email']
        ml=request.POST['mobile']
        ct=request.POST['city']
        do=request.POST['dob']
        pf=request.POST['profession']
        sa=request.POST['salary']
        st=request.POST['shift']
        ag=request.POST['age']

        dta=items()
        dta.employee_id=eid
        dta.name=na
        dta.email=em
        dta.mobile=ml
        dta.city=ct
        dta.dob=do
        dta.profession=pf
        dta.salary=sa
        dta.shift=st
        dta.age=ag

        dta.save()
        res="Datastored successfully"
        return render(request,"employee.html",{"result":res})

def change(request):
    if request.method=="POST":
        eid=request.POST['employee_id']
        na=request.POST['name']
        em=request.POST['email']
        ml=request.POST['mobile']
        ct=request.POST['city']
        do=request.POST['dob']
        pf=request.POST['profession']
        sa=request.POST['salary']
        st=request.POST['shift']
        ag=request.POST['age']

        dta=items.objects.get(employee_id=eid)
        dta.name=na
        dta.email=em
        dta.mobile=ml
        dta.city=ct
        dta.dob=do
        dta.profession=pf
        dta.salary=sa
        dta.shift=st
        dta.age=ag

        dta.save()
        return HttpResponseRedirect('eview')

def eview(request):
    vu=items.objects.all()
    return render(request,"eview.html",{"net":vu})

def slt(request,st):
    sl=items.objects.get(id=st)
    rel=product.objects.all()
    total = 0
    matching_results = []

    for res in rel:
        if sl.employee_id == res.employee_id:
            price_as_int = int(res.price)
            total += price_as_int
            matching_results.append(price_as_int)

    return render(request,"select.html",{"result":sl, "net":rel, "matching_results": matching_results, "total":total})  

def upd(request,ud):
    ue=items.objects.get(id=ud)
    return render(request,"update.html",{"res":ue})

def delet(request,de):
    dl=items.objects.get(id=de)
    dl.delete()
    return HttpResponseRedirect("/eview")                   

def ordernew(request):
    if request.method=="POST":
        od=request.POST['order_id']
        ed=request.POST.get('employee_id')
        pt=request.POST.get('product')
        cy=request.POST['category']
        cr=request.POST['color']
        br=request.POST['brand']
        pe=request.POST['price']
        mo=request.POST['model']
        dt=request.POST['date']    

        pda=product()
        pda.order_id=od
        pda.employee_id=ed
        pda.product=pt
        pda.category=cy
        pda.color=cr
        pda.brand=br
        pda.price=pe
        pda.model=mo
        pda.date=dt

        pda.save()
        dhr="data stored"
        return render(request,"order.html",{"result":dhr})

def new(request):
    ot=items.objects.all()
    pc=productcategory.objects.all()
    cz=categorizer.objects.all()
    return render(request,"order.html",{"net":ot ,"dha":pc, "cat":cz })
    
def orderview(request):
    od=product.objects.all()
    empData=items.objects.all()
    return render(request,"orderview.html",{"net":od , "empData":empData})
  
# Create your views here.
