from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError 

from .models import *
from .forms import *

# Create your views here.

@login_required
def home(request):
    return render(request, "home.html")

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

#-------------------------------------------------------------
#CourseMasterModel
#Insertion
def insertcourse(request):
    return render(request, "insertcourse.html")

def course_entry(request):
    if request.method == 'POST':
        course_details = CourseMasterForm(request.POST)

        # try:
        if course_details.is_valid():
            course_details.save()
            return render(request, "back1.html", {"operation": "course"})
        else:
            return render(request, 'insertcourse.html', {'form':course_details})
        # except IntegrityError:
        #     # Handle the unique constraint error and display a message
        #     return render(request, "insertcourse.html", {"error_message": "error_message"})
    else:
        form = CourseMasterForm()
        return render(request, "insertcourse.html", {'form':form})


#Deletion
def delete1(request,pk):
    CourseMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "course"})

def deletecourse(request):
    course = CourseMasterModel.objects.all().values()
    temp = loader.get_template("deletecourse.html")
    context = {
        'data':course
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update1(request, course_id):
    course = get_object_or_404(CourseMasterModel, pk=course_id)
    if request.method == 'POST':
        form = CourseMasterForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatecourse")}?operation=course')
    else:
        form = CourseMasterForm(instance=course)
    
    return render(request, 'update1.html', {'form': form})

def updatecourse(request):
    course = CourseMasterModel.objects.all().values()
    operation = request.GET.get('operation')
    context = {
        'data':course,
        'operation': operation,
    }
    return render(request, 'updatecourse.html', context)

#searching
def searchcourse(request):
    form = CourseSearchForm(request.GET or None)
    results = None
    
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = CourseMasterModel.objects.filter(course__iexact=query)
    
    return render(request, 'searchcourse.html', {'form': form, 'results': results})

#display
def displaycourse(request):
    course= CourseMasterModel.objects.all().values()
    temp = loader.get_template('displaycourse.html')
    context = {
        'data':course,
    }
    return HttpResponse(temp.render(context,request))

#report
def coursereport(request):
    course = CourseMasterModel.objects.all().values()
    temp = loader.get_template('coursereport.html')
    context = {
        'data':course,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#BatchMasterModel
#Insertion
def insertbatch(request):
    return render(request, "insertbatch.html")

def batch_entry(request):
    if request.method == 'POST':
        batch_details =BatchMasterForm(request.POST)

        if batch_details.is_valid():
            batch_details.save()
            return render(request, "back1.html",{"operation": "batch"})
        else:
            return render(request, "insertbatch.html", {'form':batch_details})
    else:
        form = BatchMasterForm()
        return render(request, "insertbatch.html", {'form':form})

#Deletion
def delete2(request,pk):
    BatchMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "batch"})

def deletebatch(request):
    batch = BatchMasterModel.objects.all().values()
    temp = loader.get_template("deletebatch.html")
    context = {
        'data':batch
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update2(request, batchno_id):
    batch = get_object_or_404(BatchMasterModel, pk=batchno_id)
    if request.method == 'POST':
        form = BatchMasterForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatebatch")}?operation=batch')
    else:
        form = BatchMasterForm(instance=batch)
    
    return render(request, 'update2.html', {'form': form})

def updatebatch(request):
    batch = BatchMasterModel.objects.all().values()
    operation = request.GET.get('operation')
    context = {
        'data':batch,
        'operation': operation,
    }
    return render(request, 'updatebatch.html', context)

#searching
def searchbatch(request):
    form = BatchSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = BatchMasterModel.objects.filter(batchno__iexact=query)
    
    return render(request, 'searchbatch.html', {'form': form, 'results': results})

#display
def displaybatch(request):
    batch = BatchMasterModel.objects.all().values()
    temp = loader.get_template('displaybatch.html')
    context = {
        'data':batch,
    }
    return HttpResponse(temp.render(context,request))

#report
def batchreport(request):
    batch = BatchMasterModel.objects.all().values()
    temp = loader.get_template('batchreport.html')
    context = {
        'data':batch,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#SemMasterModel
#Insertion
def insertsem(request):
    return render(request, "insertsem.html")

def sem_entry(request):
    if request.method == 'POST':
        sem_details = SemMasterForm(request.POST)

        if sem_details.is_valid():
            sem_details.save()
            return render(request, "back1.html",{"operation": "sem"})
        else:        
            return render(request, "insertsem.html", {'form':sem_details})
    else:
        form = SemMasterForm()
        return render(request, "insertsem.html", {'form':form})

#Deletion
def delete3(request,pk):
    SemMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "sem"})

def deletesem(request):
    sem = SemMasterModel.objects.all().values()
    temp = loader.get_template("deletesem.html")
    context = {
        'data':sem
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update3(request, sem_id):
    sem = get_object_or_404(SemMasterModel, pk=sem_id)
    if request.method == 'POST':
        form = SemMasterForm(request.POST, instance=sem)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatesem")}?operation=sem')
    else:
        form = SemMasterForm(instance=sem)
    
    return render(request, 'update3.html', {'form': form})

def updatesem(request):
    sem = SemMasterModel.objects.all().values()
    operation = request.GET.get('operation')
    context = {
        'data':sem,
        'operation': operation,
    }
    return render(request, 'updatesem.html', context)

#searching
def searchsem(request):
    form = SemSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = SemMasterModel.objects.filter(sem__iexact=query)
    
    return render(request, 'searchsem.html', {'form': form, 'results': results})

#display
def displaysem(request):
    sem = SemMasterModel.objects.all().values()
    temp = loader.get_template('displaysem.html')
    context = {
        'data':sem,
    }
    return HttpResponse(temp.render(context,request))

#report
def semreport(request):
    sem = SemMasterModel.objects.all().values()
    temp = loader.get_template('semreport.html')
    context = {
        'data':sem,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#PaperMasterModel
#Insertion
def insertpaper(request):
    return render(request, "insertpaper.html")

def paper_entry(request):
    if request.method == 'POST':
        paper_details = PaperMasterForm(request.POST)

        if paper_details.is_valid():
            paper_details.save()
            return render(request, "back1.html",{"operation": "paper"})
        else:
            return render(request, "insertpaper.html", {'form':paper_details})
    else:
        form = PaperMasterForm()
        return render(request, "insertpaper.html", {'form':form})

#Deletion
def delete4(request,pk):
    PaperMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "paper"})

def deletepaper(request):
    paper = PaperMasterModel.objects.all().values()
    temp = loader.get_template("deletepaper.html")
    context = {
        'data':paper
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update4(request, papername_id):
    paper = get_object_or_404(PaperMasterModel, pk=papername_id)
    if request.method == 'POST':
        form = PaperMasterForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatepaper")}?operation=paper')
    else:
        form = PaperMasterForm(instance=paper)
    
    return render(request, 'update4.html', {'form': form})

def updatepaper(request):
    paper = PaperMasterModel.objects.all().values()
    operation = request.GET.get('operation')
    context = {
        'data':paper,
        'operation': operation,
    }
    return render(request, 'updatepaper.html', context)

#searching
def searchpaper(request):
    form = PaperSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = PaperMasterModel.objects.filter(papercode__iexact=query)
    
    return render(request, 'searchpaper.html', {'form': form, 'results': results})

#display
def displaypaper(request):
    paper = PaperMasterModel.objects.all().values()
    temp = loader.get_template('displaypaper.html')
    context = {
        'data':paper,
    }
    return HttpResponse(temp.render(context,request))

#report
def paperreport(request):
    paper = PaperMasterModel.objects.all().values()
    temp = loader.get_template('paperreport.html')
    context = {
        'data':paper,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#ExamMasterModel
#Insertion
def insertexam(request):
    return render(request, "insertexam.html")

def exam_entry(request):
    if request.method == 'POST':
        exam_details = ExamMasterForm(request.POST)

        if exam_details.is_valid():
            exam_details.save()
            return render(request, "back1.html", {"operation": "exam"})
        else:
            return render(request, "insertexam.html", {'form':exam_details})
    else:
        form = ExamMasterForm()
        return render(request, "insertexam.html", {'form':form})

#Deletion
def delete5(request,pk):
    ExamMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "exam"})

def deleteexam(request):
    exam = ExamMasterModel.objects.all().values()
    temp = loader.get_template("deleteexam.html")
    context = {
        'data':exam
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update5(request, examtype_id):
    exam = get_object_or_404(ExamMasterModel, pk=examtype_id)
    if request.method == 'POST':
        form = ExamMasterForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updateexam")}?operation=exam')
    else:
        form = ExamMasterForm(instance=exam)
    
    return render(request, 'update5.html', {'form': form})

def updateexam(request):
    exam = ExamMasterModel.objects.all().values()
    operation = request.GET.get('operation')
    context = {
        'data':exam,
        'operation': operation,
    }
    return render(request, 'updateexam.html', context)

#searching
def searchexam(request):
    form = ExamSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = ExamMasterModel.objects.filter(examtype__iexact=query)
    
    return render(request, 'searchexam.html', {'form': form, 'results': results})

#display
def displayexam(request):
    examtype = ExamMasterModel.objects.all().values()
    temp = loader.get_template('displayexam.html')
    context = {
        'data':examtype,
    }
    return HttpResponse(temp.render(context,request))

#report
def examreport(request):
    exam = ExamMasterModel.objects.all().values()
    temp = loader.get_template('examreport.html')
    context = {
        'data':exam,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#StudentMasterModel
#Insertion
def insertstudent(request):
    # Fetch all existing records
    batches = BatchMasterModel.objects.all()
    semesters = SemMasterModel.objects.all()
    courses = CourseMasterModel.objects.all()
    
    return render(request, "insertstudent.html", {
        'batches': batches,
        'semesters': semesters,
        'courses': courses,
    })

def student_entry(request):
    if request.method == 'POST':
        student_details = StudentMasterForm(request.POST)

        if student_details.is_valid():
            student_details.save()
            return render(request, "back1.html", {"operation": "student"})
        else:
            batches = BatchMasterModel.objects.all()
            semesters = SemMasterModel.objects.all()
            courses = CourseMasterModel.objects.all()
            return render(request, "insertstudent.html", {
                'form': student_details,
                'batches': batches,
                'semesters': semesters,
                'courses': courses,
            })
    else:
        batches = BatchMasterModel.objects.all()
        semesters = SemMasterModel.objects.all()
        courses = CourseMasterModel.objects.all()
        form = StudentMasterForm()
        return render(request, "insertstudent.html", {
            'form': form,
            'batches': batches,
            'semesters': semesters,
            'courses': courses,
        })

#Deletion
def delete6(request,pk):
    StudentMasterModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "student"})

def deletestudent(request):
    student = StudentMasterModel.objects.select_related('batchno', 'sem', 'course').all()
    temp = loader.get_template("deletestudent.html")
    context = {
        'data':student
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update6(request, studname_id):
    student = get_object_or_404(StudentMasterModel, pk=studname_id)
    if request.method == 'POST':
        form = StudentMasterForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatestudent")}?operation=student')
    else:
        form = StudentMasterForm(instance=student)
    
    return render(request, 'update6.html', {'form': form})

def updatestudent(request):
    student = StudentMasterModel.objects.select_related('batchno', 'sem', 'course').all()
    operation = request.GET.get('operation')
    context = {
        'data':student,
        'operation': operation,
    }
    return render(request, 'updatestudent.html', context)

#searching
def searchstudent(request):
    form = StudentSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = StudentMasterModel.objects.filter(studname__iexact=query)
    
    return render(request, 'searchstudent.html', {'form': form, 'results': results})

#display
def displaystudent(request):
    student = StudentMasterModel.objects.select_related('batchno', 'sem', 'course').all()
    temp = loader.get_template('displaystudent.html')
    context = {
        'data':student,
    }
    return HttpResponse(temp.render(context,request))

#report
def studentreport(request):
    student = StudentMasterModel.objects.select_related('batchno', 'sem', 'course').all()
    temp = loader.get_template('studentreport.html')
    context = {
        'data':student,
    }
    return HttpResponse(temp.render(context,request))

#-------------------------------------------------------------
#StudentInternalTransModel
#Insertion
def insertstudtrans(request):
    # Fetch all existing records
    courses   = CourseMasterModel.objects.all()
    batches   = BatchMasterModel.objects.all()
    semesters = SemMasterModel.objects.all()
    exams     = ExamMasterModel.objects.all()
    studname  = StudentMasterModel.objects.all()
    papername = PaperMasterModel.objects.all()
    
    return render(request, "insertstudtrans.html", {
        'courses': courses,
        'batches': batches,
        'semesters': semesters, 
        'exams':exams,
        'studname':studname,
        'papername':papername,
    })

def studtrans_entry(request): 
    if request.method == 'POST':
        transaction_details = StudentInternalTansForm(request.POST)

        if transaction_details.is_valid():
            transaction_details.save()
            return render(request, "back1.html", {"operation": "transaction"})
        else:
            courses   = CourseMasterModel.objects.all()
            batches   = BatchMasterModel.objects.all()
            semesters = SemMasterModel.objects.all()
            exams     = ExamMasterModel.objects.all()
            studname  = StudentMasterModel.objects.all()
            papername = PaperMasterModel.objects.all()
            return render(request, "insertstudtrans.html", {
                'form':transaction_details,
                'courses': courses,
                'batches': batches,
                'semesters': semesters,
                'exams':exams,
                'studname':studname,
                'papername':papername,     
            })
    else:
        courses   = CourseMasterModel.objects.all()
        batches   = BatchMasterModel.objects.all()
        semesters = SemMasterModel.objects.all()
        exams     = ExamMasterModel.objects.all()
        studname  = StudentMasterModel.objects.all()
        papername = PaperMasterModel.objects.all()
        form      = StudentInternalTansForm()
        return render(request, "insertstudtrans.html", {
            'form':form,
            'courses': courses,
            'batches': batches,
            'semesters': semesters,
            'exams':exams,
            'studname':studname,
            'papername':papername,     
        })

#Deletion
def delete7(request,pk):
    StudentInternalTransModel.objects.get(id=pk).delete()
    return render(request,"back2.html",{"operation": "transaction"})

def deletestudenttrans(request):
    studtrans = StudentInternalTransModel.objects.select_related('batchno', 'course','sem','examtype','studname','papername',).all()
    temp = loader.get_template("deletestudenttrans.html")
    context = {
        'data':studtrans
    }
    return HttpResponse(temp.render(context,request))

#Updation
def update7(request, marks_id):
    marks = get_object_or_404(StudentInternalTransModel, pk=marks_id)
    if request.method == 'POST':
        form = StudentInternalTansForm(request.POST, instance=marks)
        if form.is_valid():
            form.save()
            return redirect(f'{reverse("updatestudenttrans")}?operation=transaction')
    else:
        form = StudentInternalTansForm(instance=marks)
    
    return render(request, 'update7.html', {'form': form})

def updatestudenttrans(request):
    marks = StudentInternalTransModel.objects.select_related('batchno', 'course','sem','examtype','studname','papername',).all()
    operation = request.GET.get('operation')
    context = {
        'data':marks,
        'operation': operation,
    }
    return render(request, 'updatestudenttrans.html', context)

#searching
def searchstudenttrans(request):
    form = TransactionSearchForm(request.GET or None)
    results = None
    if request.method == 'GET' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = StudentInternalTransModel.objects.filter(studname__studname__icontains=query)
    
    return render(request, 'searchstudenttrans.html', {'form': form, 'results': results})

#display
def displaystudenttrans(request):
    studtrans = StudentInternalTransModel.objects.select_related('batchno', 'course','sem','examtype','studname','papername',).all()
    temp = loader.get_template('displaystudenttrans.html')
    context = {
        'data':studtrans,
    }
    return HttpResponse(temp.render(context,request))

#report
def studtransreport(request):
    studtrans = StudentInternalTransModel.objects.select_related('batchno', 'course','sem','examtype','studname','papername',).all()
    temp = loader.get_template('studtransreport.html')
    context = {
        'data':studtrans,
    }
    return HttpResponse(temp.render(context,request))