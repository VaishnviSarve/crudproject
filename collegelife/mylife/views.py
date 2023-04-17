from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from mylife.models import Mylife
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(self):
    if self.method=='POST':
        age=self.POST.get('age')
        topic=self.POST.get('topic')
        college=self.POST.get('college')
        school=self.POST.get('school')
        rollno=self.POST.get('rollno')
        x=Mylife(age=age, topic=topic, college=college, school=school, rollno=rollno)
        x.save()
    return render(self,'index.html')

def life(self):
   mylife=Mylife.objects.all().values()
   template=loader.get_template('register.html')
   xy={
       'mylife':mylife
   }
   return HttpResponse(template.render(xy,self))

def update(self,rollno):
    mylife=Mylife.objects.get(rollno=rollno)
    template=loader.get_template('update.html')
    xy={
        'mylife':mylife
    }
    return HttpResponse(template.render(xy,self))

def updaterequest(self,rollno):
    age=self.POST['age']
    topic=self.POST['topic']
    college=self.POST['school']
    school=self.POST['college']
    rollno=self.POST['rollno']
    mylife=Mylife.objects.get(rollno=rollno)
    mylife.age=age
    mylife.topic=topic
    mylife.college=college
    mylife.school=school
    mylife.rollno=rollno
    mylife.save()
    return HttpResponseRedirect(reverse('life'))

def delete(self,rollno):
    mylife=Mylife.objects.get(rollno=rollno)
    mylife.delete()
    return HttpResponseRedirect(reverse('life'))


