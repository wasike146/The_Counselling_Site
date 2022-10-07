
from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews


urlpatterns = [
    path('', views.signIn_Up, name='login'),

    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name='admin_home'),
    path('appointment-report/', HodViews.AppointmentReport, name='appointment1'),
    path('appointment/', HodViews.Appointment, name='appointment'),
    path('counselling/', HodViews.Counselling, name='counselling'),
    path('add_course_save/', HodViews.add_course_save, name="add_course_save"),
    path('course/', HodViews.Course, name='add_course'),
    path('referralR/', HodViews.ReferralReports, name='referralR'),
    path('referral/', HodViews.Referral, name='referral'),
    path('schedule/', HodViews.Schedule, name='schedule'),
    path('counsellor/', HodViews.counsellor, name='counsellor'),
    path('add_counsellor_save/', HodViews.add_counsellor_save, name="add_counsellor_save"),
    path('add_session_save/', HodViews.add_session_save, name="add_session_save"),
    path('add_manage_session/', HodViews.add_manage_session, name="add_manage_session"),
    path('student/', HodViews.Student, name='student'),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    
   
    # URLS for Staff
    path('staff_home', StaffViews.staff_home, name='staff_home'),
    path('get_students/', StaffViews.get_students, name="get_students"),
    path('staff_add_guidance/', StaffViews.staff_add_Guidance, name="staff_add_guidance"),
    path('staff_add_guidance_save/', StaffViews.staff_add_guidance_save, name="staff_add_guidance_save"),
    path('manage_session/', StaffViews.Session, name="staff_session"),
    path('staff_appointment-report/', StaffViews.AppointmentReport, name='staff_appointment1'),
    path('staff_appointment/', StaffViews.Appointment, name='staff_appointment'),
    path('staff_counselling/', StaffViews.Counselling, name='staff_counselling'),
    path('staff_counsellor/', StaffViews.Counsellors, name='staff_counsellor'),
    path('staff_course/', StaffViews.Course, name='staff_course'),
    path('staff_referralR/', StaffViews.ReferralReports, name='staff_referralR'),
    path('staff_referral/', StaffViews.Referral, name='staff_referral'),
    path('staff_schedule/', StaffViews.Schedule, name='staff_schedule'),
    path('staff_student/', StaffViews.Student, name='staff_student'),
    
    

    # URSL for Student
    path('student_home/', StudentViews.student_home, name='student_home'),
    path('CounsellingS/', StudentViews.CounsellingS, name='counselling2'),
    path('New-appointments/', StudentViews.NewAppointments, name='NewAppointment'),
    path('NewAppointment_save',StudentViews.student_NewAppointment_save,name='student_NewAppointment_save'),


    # URSL for room
    path('room/', views.room,name="room_home"),
    path('get_token/', views.getToken,name="get_token"),
    path('create_member/',views.createMember,name="create_member"),
    path('get_member/', views.getMember,name="get_member"),
    path('delete_member/',views.deleteMember,name="delete_member"),
]
