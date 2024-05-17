from django.shortcuts import render
from .models import Student, Active
from django.core.files.storage import FileSystemStorage
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def Forms(request):
    fr = Form()
    active = Active.objects.latest('id')
    return render(request, "form.html", {"form": fr, "active": active})

# Create your views here.

def Make_Pdf_Page(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            full_name_1 = request.POST["full_name"]
            class_of_year = request.POST["class_of_year"]
            if Student.objects.filter(full_name=full_name_1.strip()).exists():
                messages.error(request, 'Мындай Фамилиядагы окуучу мурда катталган...')
                return redirect("form")
            else:
                form.save()
                img_obj = form.instance
        full_name = request.POST["full_name"]
        gender = request.POST["gender"]
        birth_day = request.POST["birth_day"]
        class_of_year = request.POST["class_of_year"]
        region = request.POST["region"]
        phone_number_student = request.POST["phone_number_student"]
        name_of_dud_mum = request.POST["name_of_dud_mum"]
        phone_of_dud_mum = request.POST["phone_of_dud_mum"]
        name_guardian = request.POST["name_guardian"]
        phone_guardian = request.POST["phone_guardian"]
        whatsapp = request.POST["whatsapp"]
        interesting_lesson = request.POST["interesting_lesson"]
        success = request.POST["success"]
        hobbies = request.POST["hobbies"]
        lang = request.POST["lang"]
        if class_of_year == '7-класс':
            students = Student_7.objects.create(full_name=full_name.title(), gender=gender, birth_day=birth_day,
                                            class_of_year=class_of_year, region=region,
                                            phone_number_student=phone_number_student,
                                            name_of_dud_mum=name_of_dud_mum, phone_of_dud_mum=phone_of_dud_mum,
                                            name_guardian=name_guardian, phone_guardian=phone_guardian,
                                            whatsapp=whatsapp, interesting_lesson=interesting_lesson,
                                            success=success, hobbies=hobbies, lang = lang
                                            )
            students.save()
        elif class_of_year == '8-класс':
            students = Student_8.objects.create(full_name=full_name.title(), gender=gender, birth_day=birth_day,
                                            class_of_year=class_of_year, region=region,
                                            phone_number_student=phone_number_student,
                                            name_of_dud_mum=name_of_dud_mum, phone_of_dud_mum=phone_of_dud_mum,
                                            name_guardian=name_guardian, phone_guardian=phone_guardian,
                                            whatsapp=whatsapp, interesting_lesson=interesting_lesson,
                                            success=success, hobbies=hobbies, lang = lang
                                            )
            students.save()
        elif class_of_year == '9-класс':
            students = Student_9.objects.create(full_name=full_name.title(), gender=gender, birth_day=birth_day,
                                            class_of_year=class_of_year, region=region,
                                            phone_number_student=phone_number_student,
                                            name_of_dud_mum=name_of_dud_mum, phone_of_dud_mum=phone_of_dud_mum,
                                            name_guardian=name_guardian, phone_guardian=phone_guardian,
                                            whatsapp=whatsapp, interesting_lesson=interesting_lesson,
                                            success=success, hobbies=hobbies, lang = lang
                                            )
            students.save()
        elif class_of_year == '10-класс':
            students = Student_10.objects.create(full_name=full_name.title(), gender=gender, birth_day=birth_day,
                                            class_of_year=class_of_year, region=region,
                                            phone_number_student=phone_number_student,
                                            name_of_dud_mum=name_of_dud_mum, phone_of_dud_mum=phone_of_dud_mum,
                                            name_guardian=name_guardian, phone_guardian=phone_guardian,
                                            whatsapp=whatsapp, interesting_lesson=interesting_lesson,
                                            success=success, hobbies=hobbies, lang = lang
                                            )
            students.save()
        else:
            print('Мындай класс жок')
            

        context = {
            "full_name": full_name.title(),
            "gender": gender,
            "birth_day": birth_day,
            "class_of_year": class_of_year,
            "region": region,
            "phone_number_student": phone_number_student,
            "name_of_dud_mum": name_of_dud_mum,
            "phone_of_dud_mum": phone_of_dud_mum,
            "name_guardian": name_guardian,
            "phone_guardian": phone_guardian,
            "whatsapp": whatsapp,
            "interesting_lesson": interesting_lesson,
            "success": success,
            "hobbies": hobbies,
            "lang": lang,

        }
        return render(request, "make_pdf_page.html", {"context": context, "url":img_obj})
    else:
        pass
    return render(request, "make_pdf_page.html")
