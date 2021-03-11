from django.http import HttpResponse
from django.shortcuts import render
from .models import Psc,Home
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
# Create your views here.

# def homeo(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'driver.html',{'pscs':pscs})
# def homeo1(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'TheatreTechnician.html',{'pscs':pscs})   

# def homeo2(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'InteriorDecoration.html',{'pscs':pscs}) 
# def homeo3(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'homeo.html',{'pscs':pscs})    

# def homeo4(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'shiftsupervisor.html',{'pscs':pscs})  
# def medical(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'MedicalEducation.html',{'pscs':pscs})                 

# def home(request):
#     homes=Home.objects.all()
    
#     return render(request, 'home.html',{'homes':homes})    

# def helth(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'HealthServices.html',{'pscs':pscs})  
# def orthotic(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'OrthoticEngineer.html',{'pscs':pscs})  
# def dairyfarm(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'DairyFarmInstructor.html',{'pscs':pscs})  
# def transport(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'MotorTransport.html',{'pscs':pscs})      
# def ophthalmology(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'Ophthalmology.html',{'pscs':pscs})    

# def assistantsurgeon(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'AssistantSurgeon.html',{'pscs':pscs})    

# def liftescalator(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'LiftEscalator.html',{'pscs':pscs})  
# def pumpoperator(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'PumpOperator.html',{'pscs':pscs}) 
# def optometristgr(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'optometristgrII.html',{'pscs':pscs})     


# def pulmonary(request):
#     pscs=Psc.objects.all()
    
#     return render(request, 'PulmonaryMedicine.html',{'pscs':pscs}) 

def aa(request):
    if request.method=='POST':
        s=request.POST['q']
        b=Home.objects.filter(title__contains=s)
        return render(request, 'aa.html',{'homes':b})  
    homes=Home.objects.all()
    paginator = Paginator(homes, 20)
    page = request.GET.get('page')
 
    try:
        homes = paginator.page(page)
    except PageNotAnInteger:
        homes = paginator.page(1)
 
    except EmptyPage:
        homes = paginator.page(paginator.num_pages)
    return render(request, 'aa.html',{'page':page,'homes':homes})  

def bb(request):
    if request.method=='POST':
        s=request.POST['q']
        r=request.POST['bt']
        b=Psc.objects.filter(question__contains=s)
        homes=Home.objects.all() 
        return render(request, 'bb.html',{'system':r,'pscs':b,'homes':homes}) 
    system=request.GET.get('system',None)
    pscs=Psc.objects.all()
    homes=Home.objects.all()
    
    return render(request, 'bb.html',{'system':system,'pscs':pscs,'homes':homes,})   

def test(request):
    if request.method=='POST':
        system=request.POST.get('system',None)
        pscs=Psc.objects.filter(category = system)
        print(system)
        homes=Home.objects.filter(link = system)
        homes2=random.choices(pscs,k=100)
        print(len(homes2))
        homes2=zip(list(range(1,len(homes2)+1)),homes2)
        return render(request, 'test.html',{'system':system,'pscs':homes2,'homes':homes})

def result(request):
    if request.method=='POST':
        count=0
        for key in request.POST:
            if key != 'csrfmiddlewaretoken':
                print()
                pscs=Psc.objects.get(pk = int(key))
                print(request.POST[key][0])
                print(pscs.answer[-2])

                if pscs.answer[-2] == request.POST[key][0]:
                    count=count+1
        print(count) 
        return render(request,'result.html',{'count':count})    
         



          