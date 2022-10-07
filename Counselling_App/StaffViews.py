from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


from Counselling_App.models import CustomUser, Staffs, Courses, Students, SessionYearModel,CounsellingStudent,NewAppointementStudent


def staff_home(request):

    return render(request,'Counselling_App/staff_template//index.html')

def AppointmentReport(request):
    return render(request,'Counselling_App/staff_template/appointment-reports.html')

def signIn_Up(request):
    return render(request,'Counselling_App/staff_template/sign-in-up.html')

def Appointment(request):
    return render(request,'Counselling_App/staff_template/appointment.html')

def Counsellors(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request,'Counselling_App/staff_template/counsellor.html',context)

def Session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        "session_years": session_years
    }
    return render(request,'Counselling_App/staff_template/session.html',context)

def Counselling(request):
    return render(request,'Counselling_App/staff_template/counselling.html')

def ReferralReports(request):
    return render(request,'Counselling_App/staff_template/referral-reports.html')

def Referral(request):
    return render(request,'Counselling_App/staff_template/referral.html')

def Schedule(request):
    NewAppointement = NewAppointementStudent.objects.all()
    context = {
        "NewAppointement": NewAppointement
    }
    return render(request,'Counselling_App/staff_template/schedule.html',context)

def Course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request,'Counselling_App/staff_template/course.html',context)

def Student(request):
    
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request,'Counselling_App/staff_template/student.html',context)

@csrf_exempt
def get_students(request):
   
    students = Students.objects.all()

    list_data = []

    for student in students:
        data_small={"id":student.admin.id, "name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

def staff_add_Guidance(request):

    students = Students.objects.all()

    context = {
        "students": students
    }
    
    return render(request, "Counselling_App/staff_template/counselling.html", context)

def staff_add_guidance_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('staff_add_guidance')

    else:
        student_admin_id = request.POST.get('student_list')
        Counsellors_guidance = request.POST.get('Counsellors_guidance')
        strategies_use = request.POST.get('strategies_use')
        video_link = request.POST.get('video_link')
        remarks = request.POST.get('remarks')
        date_time = request.POST.get('date_time')
        
        student_obj = Students.objects.get(admin=student_admin_id)

        try:
            guidance = CounsellingStudent(student_id=student_obj,strategies_advice=strategies_use,
            Guidance_Message=Counsellors_guidance,video_room=video_link,remarks=remarks,date=date_time)
            guidance.save()
            messages.success(request, "Guidance Added Successfully!")
            return redirect('staff_add_guidance')

        except:
            messages.error(request, "Failed to Add Guidance!")
            #return redirect('staff_add_guidance')
            return HttpResponse(Counsellors_guidance)


        


        

