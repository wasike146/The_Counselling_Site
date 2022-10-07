from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
import datetime # To Parse input DateTime into Python Date Time Object

from Counselling_App.models import CustomUser, Staffs, Courses, Students,CounsellingStudent,NewAppointementStudent


def CounsellingS(request):
    student = Students.objects.get(admin=request.user.id)
    student_result = CounsellingStudent.objects.filter(student_id=student.id)
    context = {
        "student_result": student_result,
    }
    return render(request,'Counselling_App/student_template/counsellingS.html',context)

def student_home(request):
    student_obj = Students.objects.get(admin=request.user.id)
    NewAppointement = NewAppointementStudent.objects.filter(student_id=student_obj)
    context = {
        "NewAppointement": NewAppointement
    }
    return render(request,'Counselling_App/student_template/indexS.html',context)


def NewAppointments(request):
   
    return render(request,'Counselling_App/student_template/new-appointmentS.html')

def student_NewAppointment_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('NewAppointment')
    else:
        Reasons_message = request.POST.get('reasons_message')
        Concern_message=request.POST.get('concern_message')
        Appointment_date = request.POST.get('appointment_date')

        student_obj = Students.objects.get(admin=request.user.id)
        try:
            New_appointment = NewAppointementStudent(student_id=student_obj, Reasons_referral=Reasons_message,date=Appointment_date, concern=Concern_message)
            New_appointment.save()
            messages.success(request, "New Appointment sent.")
            return redirect('student_home')
        except:
            messages.error(request, "Failed to Apply Leave")
            return redirect('NewAppointment')



