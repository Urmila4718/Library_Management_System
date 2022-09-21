from django.contrib import admin


from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display =['user_id','username','signup_otp','emailId','password']

admin.site.register(admindetails,UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display =['user_id','username','signup_otp','emailId','password']

admin.site.register(studentdetails,StudentAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display =['book_id','title','Author','issued_to','issued_at','issued_status']

admin.site.register(Books,BookAdmin)
