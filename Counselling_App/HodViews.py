from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from Counselling_App.models import CustomUser, Staffs, Courses, Students, SessionYearModel, NewAppointementStudent
from .forms import AddStudentForm


def admin_home(request):
    all_student_count = Students.objects.all().count()
    course_count = Courses.objects.all().count()
    staff_count = Staffs.objects.all().count()


    context={
        "all_student_count": all_student_count,
        "course_count": course_count,
        "staff_count": staff_count,
    }

    return render(request,'Counselling_App/hod_template/index.html' ,context)

def AppointmentReport(request):
    return render(request,'Counselling_App/hod_template/appointment-reports.html')

def signIn_Up(request):
    return render(request,'Counselling_App/hod_template/sign-in-up.html')

def Appointment(request):
    return render(request,'Counselling_App/hod_template/appointment.html')


def Counselling(request):
    return render(request,'Counselling_App/hod_template/counselling.html')

def ReferralReports(request):
    return render(request,'Counselling_App/hod_template/referral-reports.html')

def Referral(request):
    return render(request,'Counselling_App/hod_template/referral.html')

def Schedule(request):
    NewAppointement = NewAppointementStudent.objects.all()
    context = {
        "NewAppointement": NewAppointement
    }
    return render(request,'Counselling_App/hod_template/schedule.html',context)

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        coursename = request.POST.get('coursename')
        coursecode = request.POST.get('coursecode')
        try:
            course_model = Courses(course_code=coursecode,course_name=coursename)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')

def Course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request,'Counselling_App/hod_template/course.html',context)


def add_counsellor_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('counsellor')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address =address
            user.staffs.gender =gender
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('counsellor')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('counsellor')

def counsellor(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    
    return render(request,'Counselling_App/hod_template/counsellor.html' , context)



def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student')
    else:
        form = AddStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            session_year_id = form.cleaned_data['session_year_id']
            course_id = form.cleaned_data['course_id']
            gender = form.cleaned_data['gender']

            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None


            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
                user.students.address = address

                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id = course_obj

                session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id = session_year_obj

                user.students.gender = gender
                user.students.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Student Added Successfully!")
                return redirect('student')
            except:
                messages.error(request, "Failed to Add Student!")
                return redirect('student')
        else:
            return redirect('student')


def Student(request):
    form = AddStudentForm()
    students = Students.objects.all()
    context = {
        "students": students,"form": form
    }
    return render(request, 'Counselling_App/hod_template/studentH.html', context)

def add_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_manage_session')
    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Session Year added Successfully!")
            return redirect("add_manage_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect("add_manage_session")

def add_manage_session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        "session_years": session_years
    }
    return render(request, "Counselling_App/hod_template/add_session.html", context)

