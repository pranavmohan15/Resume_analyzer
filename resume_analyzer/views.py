from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Resume, Job, MatchResult
from .forms import AnalyzeForm
from .services.resume_parser import extract_text_from_docx, extract_text_from_pdf
from .services.skill_extractor import extract_skills
from .services.matching_engine import calculate_similarity
from .services.matching_engine import advanced_score
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect


# HOME
def home_view(request):
    return render(request, 'home.html')


# REGISTER
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')  # go to login page
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
# ANALYZE (Protected)
@login_required
@never_cache
def analyze_view(request):

    if request.method == 'POST':
        form = AnalyzeForm(request.POST, request.FILES)

        if form.is_valid():

            # Save Resume
            resume = Resume.objects.create(
                user=request.user,
                file=form.cleaned_data['resume_file']
            )

            file_path = resume.file.path

            if file_path.endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            elif file_path.endswith('.docx'):
                text = extract_text_from_docx(file_path)
            else:
                text = ""

            resume.extracted_text = text
            resume.save()

            # Save Job
            job = Job.objects.create(
            user=request.user,
            position=form.cleaned_data['position'],
            company=form.cleaned_data['company_name'],
            description=form.cleaned_data['description']
            )

            score = advanced_score(text, job.description, extract_skills)
            # 🔥 2️⃣ Skill Extraction
            resume_skills = extract_skills(text)
            job_skills = extract_skills(job.description)

            missing_skills = list(set(job_skills) - set(resume_skills))

            # Save Result
            result = MatchResult.objects.create(
                resume=resume,
                job=job,
                match_score=score,
                missing_skills=", ".join(missing_skills)
            )

            return render(request, 'result.html', {'result': result})

    else:
        form = AnalyzeForm()

    return render(request, 'analyze.html', {'form': form})
@login_required
@never_cache
def result_view(request, result_id):
    result = MatchResult.objects.get(id=result_id, resume__user=request.user)

    return render(request, 'result.html', {
        'result': result
    })