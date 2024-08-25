from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import os
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def accept(request):

    if request.method == "POST":

        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        branch = request.POST.get("branch","")
        cgpa = request.POST.get("cgpa","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,branch=branch,cgpa=cgpa,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
        return render(request,'pdf/select.html')

    return render(request,'pdf/accept.html')

def resume1(request):
    user_profile = Profile.objects.last()
    skills = user_profile.skills
    skill_sentences = skills.split('.')
    skill_sentences = skill_sentences[:-1]

    previous_work = user_profile.previous_work
    previous_work_sentences = previous_work.split('.')
    previous_work_sentences = previous_work_sentences[:-1]

    template = loader.get_template('pdf/resume-1.html')
    html = template.render({'user_profile':user_profile,'skill_sentences':skill_sentences,'previous_work_sentences':previous_work_sentences})

    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)

    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    return response

def resume2(request):
    user_profile = Profile.objects.last()
    skills = user_profile.skills
    skill_sentences = skills.split('.')
    skill_sentences = skill_sentences[:-1]

    previous_work = user_profile.previous_work
    previous_work_sentences = previous_work.split('.')
    previous_work_sentences = previous_work_sentences[:-1]
    template = loader.get_template('pdf/resume-2.html')
    html = template.render({'user_profile':user_profile,'skill_sentences':skill_sentences,'previous_work_sentences':previous_work_sentences})

    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)

    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    filename = 'resume.pdf'
    return response

def resume3(request):
    user_profile = Profile.objects.last()
    skills = user_profile.skills
    skill_sentences = skills.split('.')
    skill_sentences = skill_sentences[:-1]

    previous_work = user_profile.previous_work
    previous_work_sentences = previous_work.split('.')
    previous_work_sentences = previous_work_sentences[:-1]
    template = loader.get_template('pdf/resume-3.html')
    html = template.render({'user_profile':user_profile,'skill_sentences':skill_sentences,'previous_work_sentences':previous_work_sentences})

    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf = pdfkit.from_string(html,False,options)

    response = HttpResponse(pdf,content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'

    return response


def select(request):
    return render(request,'pdf/select.html')
