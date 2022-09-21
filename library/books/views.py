from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from books.models import Books, admindetails, studentdetails
from django.core.mail import send_mail
import math
import random

# ------------------------------------ADMIN PORTAL ------------------------------------------------------#

def admin(request):

    messages.success(request,"Welcome to the Library management System")
    return render(request,'admin.html')
#------------------------------------ADMIN DASHBOARD-----------------------------------------------------#
def dash(request):
    
    if request.session.get('loggedin1',False)==False:
        messages.success(request,"You need to sign in first!")
        return redirect('/signin')
    print("hiii")    
    messages.success(request,"Welcome to Library!")
    user_id=request.session['user_id']
    user_obj=admindetails.objects.get(user_id=user_id)
    request.session['user_id']=user_id

    context = {'name' : user_obj.username}
    return render(request,'dash.html',context)

#--------------------------------ADMIN SIGN-UP------------------------------------------------------------#

def signup(request):

    print(request.method)
    if request.method == "POST":
        username=request.POST.get('username')
        emailId=request.POST.get('emailId')
        print(emailId)
        password=request.POST.get('Password')
        print(password)

        check_user=admindetails.objects.filter(emailId=emailId).first()
        if check_user:
            messages.success(request,"User Already Exist")
            return render(request,'register.html')
        user_obj=admindetails.objects.create(emailId=emailId,username=username,password=password)
        print(user_obj)
        request.session['user_id']=user_obj.user_id
        
        subject='Verify your email'
        digits = "0123456789"
        signup_otp = ""
        for i in range(4):
            signup_otp += str(digits[math.floor(random.random() * 10)])    

        message='Your OTP for email verification is '+signup_otp
       
        from_email= settings.EMAIL_HOST_USER
       
        to_list = [emailId]
      
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,"OTP sent on your Email!")
        context ={'signupotp' : signup_otp}
        user_id=request.session.get('user_id')
        print(user_id)
        admindetails.objects.update(user_id=user_id,signup_otp=signup_otp)
        return redirect('/otpverify',context)
    return render(request,'register.html')

#-------------------------ADMIN OTP VERIFICATION WHILE SIGN-UP--------------------------------------------------#   

def otpverify(request):
    user_id=request.session.get('user_id')

    if request.method == 'POST':
        signup_otp1 = request.POST.get('otp')
        otp_obj = admindetails.objects.get(user_id=user_id)
        print(otp_obj)
    
        if signup_otp1 == otp_obj.signup_otp:

            otp_obj.verified_status=True
            otp_obj.save()
            messages.success(request,"Successfully Registered!")
            return redirect('/signin')
        else:
            messages.error(request,"Invalid OTP,Try Again!")
            return redirect('/otpverify')

    return render(request,'otp_for_signup.html')

#------------------------------------ADMIN SIGN-IN--------------------------------------------------------------#

def signin(request):
  
    if request.method == "POST":
        emailId=request.POST.get('emailId')
        password=request.POST.get('Password')
        
        user_obj=admindetails.objects.filter(emailId=emailId).first()
        print("user_obj")
        if user_obj is not None:
            print(user_obj.user_id)
            messages.success(request,"Successfully login")
            request.session['user_id']=user_obj.user_id
            request.session['loggedin1']=True
            return redirect('/dash')
        else:
            messages.error(request,"Admin Not Found")
            return render(request,'register.html')
           
    return render(request,'login.html')

#---------------------------------------------ADD BOOK ENTRY------------------------------------------------------------------------#

def add(request):
    user_id=request.session['user_id']
    if request.session.get('loggedin1',False)==False:
            messages.success(request,"You need to sign in first!")
            return redirect('/signin')

    if request.method == "POST":
        book_id=request.POST.get('book_id')
        title=request.POST.get('Title')
        author=request.POST.get('Author')
        issued_to=request.POST.get('Username')

        Books.objects.create(book_id=book_id,title=title,Author=author,issued_to=issued_to,issued_status=True)
        return redirect('/dash')
    return render(request,'add.html')


#---------------------------------------------UPDATE BOOK ENTRY------------------------------------------------------------------------#

def update(request):
    if request.session.get('loggedin1',False)==False:
            messages.success(request,"You need to sign in first!")
            return redirect('/signin')
    if request.method == "PUT":
        book_id=request.POST.get('book_id')
        title=request.POST.get('Title')
        author=request.POST.get('Author')
        issued_to=request.POST.get('Username')
        print(author)
        Books.objects.update(book_id=book_id,title=title,Author=author,issued_to=issued_to)
        return redirect('/update')
    return render(request,'update.html')

#---------------------------------------------DELETE BOOK ENTRY------------------------------------------------------------------------#

def delete(request):

    print(request.method)
    if request.method == "POST":
        book_id=request.POST.get('book_id')
        c=Books.objects.get(book_id=book_id).delete()
        print(c)
        return redirect('/view')
    return render(request,'delete.html')

#---------------------------------------------VIEW ALL BOOK ENTRY------------------------------------------------------------------------#

def history(request):
        if request.session.get('loggedin1',False)==False:
            messages.success(request,"You need to sign in first!")
            return redirect('/signin')
    
        t=Books.objects.all()
        print("**********************")
        print(t)
        context = {'t':t}
        
        return render(request,'history.html',context=context)

#--------------------------------------------- ADMIN SIGN-OUT------------------------------------------------------------------------#

def logout(request):
    if request.session.get('loggedin1',False)==False:
            messages.success(request,"You need to sign in first!")
            return redirect('/signin')

    messages.success(request,'Successfully Logout')
    return redirect('/')

#---------------------------------------------STUDENT PORTAL------------------------------------------------------------------------#

def student(request):
    messages.success(request,"Welcome to the Library management System")
    return render(request,'student.html')

#---------------------------------------------STUDENT DASHBOARD------------------------------------------------------------------------#

def studentdash(request):
    
    if request.session.get('loggedin',False)==False:
        messages.success(request,"You need to sign in first!")
        return redirect('/sign_in')

    messages.success(request,"Welcome to Library!")
    user_id=request.session['user_id']
    user_obj=admindetails.objects.get(user_id=user_id)
    request.session['user_id']=user_id
    return render(request,'studentdash.html')

def sign_up(request):

    print(request.method)
    if request.method == "POST":
        username=request.POST.get('username')
        emailId=request.POST.get('emailId')
        print(emailId)
        password=request.POST.get('Password')
        print(password)

        check_user=studentdetails.objects.filter(emailId=emailId).first()
        if check_user:
            messages.success(request,"Student Already Registered")
            return render(request,'register.html')
        user_obj=studentdetails.objects.create(emailId=emailId,username=username,password=password)
        print(user_obj)
        request.session['user_id']=user_obj.user_id
        
        subject='Verify your email'
        digits = "0123456789"
        signup_otp = ""
        for i in range(4):
            signup_otp += str(digits[math.floor(random.random() * 10)])    

        message='Your OTP for email verification is '+signup_otp
       
        from_email= settings.EMAIL_HOST_USER
       
        to_list = [emailId]
      
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        messages.success(request,"OTP sent on your Email!")
        context ={'signupotp' : signup_otp}
        user_id=request.session.get('user_id')
        print(user_id)
        studentdetails.objects.update(user_id=user_id,signup_otp=signup_otp)
        return redirect('/otp_verify',context)
    return render(request,'register.html')

#-------------------------STUDENT OTP VERIFICATION WHILE SIGN-UP--------------------------------------------------#   

def otp_verify(request):
    user_id=request.session.get('user_id')

    if request.method == 'POST':
        signup_otp1 = request.POST.get('otp')
        otp_obj = studentdetails.objects.get(user_id=user_id)
        print(otp_obj)
    
        if signup_otp1 == otp_obj.signup_otp:

            otp_obj.verified_status=True
            otp_obj.save()
            messages.success(request,"Successfully Registered!")
            return redirect('/sign_in')
        else:
            messages.error(request,"Invalid OTP,Try Again!")
            return redirect('/otp_verify')

    return render(request,'otp_for_signup.html')

#------------------------------------STUDENT SIGN-IN--------------------------------------------------------------#
def sign_in(request):
  
    if request.method == "POST":
        emailId=request.POST.get('emailId')
        password=request.POST.get('Password')
        
        user_obj=studentdetails.objects.filter(emailId=emailId).first()
        print("user_obj")
        if user_obj is not None:
            print(user_obj.user_id)
            messages.success(request,"Successfully login")
            request.session['user_id']=user_obj.user_id
            request.session['loggedin']=True
            return redirect('/studentdash')
        else:
            messages.error(request,"Student Not Found")
            return redirect('/sign_up')
           
    return render(request,'login.html')

#------------------------------------STUDENT SIGN-OUT--------------------------------------------------------------#
def logout(request):
    if request.session.get('loggedin',False)==False:
            messages.success(request,"You need to sign in first!")
            return redirect('/sign_in')

    messages.success(request,'Successfully Logout')
    return redirect('/student')        