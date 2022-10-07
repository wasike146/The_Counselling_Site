from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Courses, Students, Referral, ReferralReport,reservation, appointment_schedule,AppointmentReport, LeaveReportStaff, referralReportStudent,CounsellingStudent, FeedBackStaffs, NewAppointementStudent, NotificationStaffs, referralReportStudent

# Register your models here.
class UserModel(UserAdmin):  
 pass

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(Referral)
admin.site.register(reservation)
admin.site.register(ReferralReport)
admin.site.register(appointment_schedule)
admin.site.register(referralReportStudent)
admin.site.register(CounsellingStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(AppointmentReport)
admin.site.register(FeedBackStaffs)
admin.site.register(NewAppointementStudent)
admin.site.register(NotificationStaffs)
