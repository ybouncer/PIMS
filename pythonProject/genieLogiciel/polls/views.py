from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection

from .queries import find_student_by_id_personne, find_professeur_by_id_personne, \
    find_course_by_student, find_course_by_professeur_or_superviseur, get_student_by_id_personne, get_delais
from django.views.decorators.csrf import csrf_exempt
from .forms import ConnectForm
from .restrictions import prof_or_superviseur_or_student_required, admin_or_professor_required
from .utils.date import get_today_date
from .mailNotification import sendMail

from.models import Cours, Sujet, Etudiant, Personne, Professeur, Periode


# Create your views here.


# obliger de passer tous les élements nécessaires dans le context donc, attention aux id
@login_required(login_url='/polls')
@prof_or_superviseur_or_student_required
def accueil(request) -> HttpResponse:
    user = request.user
    if "professeur" in user.role["role"] or "superviseur" in user.role['role'] or "etudiant" in user.role['role']:
        context = {
            'user': user
        }
        return render(request, "otherRole/otherRole.html", context=context)
    else:
        return redirect('/polls')


@login_required(login_url='/polls')
@prof_or_superviseur_or_student_required
def home(request) -> HttpResponse:
    user = request.user
    courses = []
    role = user.role["role"]
    if "professeur" in role or "superviseur" in role:
        course = find_course_by_professeur_or_superviseur(user.idpersonne)
        courses.append(course)
    else:
        course = find_course_by_student(user.idpersonne)
        courses.append(course)
    sideBar = not ('professeur' in role or "superviseur" in role)
    context = {
        'cours': courses,
        'noSideBar': sideBar
    }

    return render(request, 'otherRole/home.html', context)


@login_required(login_url='/polls')
def course(request, code) -> HttpResponse:
    return render(request, 'otherRole/course.html', {})


@csrf_exempt
def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():

            user = authenticate(request, mail=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None and user.is_authenticated:
                auth_login(request, user)
                if 'admin' in user.role['role'] and user.role['view'] == 'admin':
                    return HttpResponseRedirect(redirect_to="admin/")
                else:
                    #sendMail("Connexion Réussie", f"Vous vous êtes connecté à la plateforme PIMS le {get_today_date()}")
                    return HttpResponseRedirect(redirect_to="home/")
            else:
                form = ConnectForm()
    else:
        form = ConnectForm()
    context = {
        "form": form
    }
    return render(request, 'login.html', context)


@login_required(login_url='/polls')
def logout(request):
    #user = request.user
    #sendMail("Déconnexion réussie", f"Vous vous êtes déconnecté de la plateforme PIMS le {get_today_date()}")

    auth_logout(request)
    return redirect('/polls')


def yes(request):
    return render(request, 'suivi.html', {})


@login_required(login_url='/polls')
def fiche(request):
    user = request.user
    student = find_student_by_id_personne(user.idpersonne)
    if student is None:
        personne = find_professeur_by_id_personne(user.idpersonne)
    else:
        personne = student
    context = {
        'user': user,
        'personne': personne,
        'noSideBar': 'true'
    }
    return render(request, 'otherRole/fiche.html', context)


@login_required(login_url='/polls')
@admin_or_professor_required
def switchRole(request, role):
    user = request.user
    redirect_url = ""
    if role == "admin":
        redirect_url = "/polls/admin/"
    elif role == "professeur" or role == "superviseur":
        redirect_url = "/polls/course/"

    user.role['view'] = role
    user.save()

    return HttpResponseRedirect(redirect_to=redirect_url)


@login_required(login_url='/polls')
def echeance(request):
    user = request.user
    if "etudiant" in user.role['role']:
        etudiant = get_student_by_id_personne(user.idpersonne)
        delais_query = get_delais(etudiant.idsujet.idperiode.idperiode)

        delais = []
        for delai in delais_query:
            delais.append(delai)
        context = {
            'cours': etudiant.idsujet.idcours,
            'periode': etudiant.idsujet.idperiode,
            'delais': delais
        }
        for delai in delais:
            print(delai.iddelivrable)
        return render(request, 'otherRole/echeance.html', context)


@login_required(login_url="polls/")
def delivrable(request, delivrable):
    context = {
        'iddelivrable': delivrable
    }
    return render(request, 'otherRole/delivrable.html', context=context)


@login_required(login_url='/polls')
def vue_historique(request):
    resultats = (
        Cours.objects.all()
      .select_related('sujet__etudiant__personne', 'sujet__professeur__personne', 'sujet__periode')
      .order_by('sujet__periode__annee', 'nom')
      .values_list(
            'sujet__periode__annee',
            'nom',
            'sujet__titre',
            'sujet__descriptif',
            'sujet__etudiant__personne__nom',
            'sujet__etudiant__personne__prenom',
            'sujet__professeur__personne__nom',
            'sujet__professeur__personne__prenom',
        )
    )
    print(resultats)

    return render(request, 'otherRole/historique.html', {'resultats': resultats})



