from django.urls import path
from . import views, courseViews, adminViews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("course/", views.home, name="home"),
    path("course/<str:code>/topics/", courseViews.topics, name="topics"),
    path("course/<str:code>/new/", courseViews.addTopic, name="addTopic"),
    path("topic/", courseViews.topics, name="topic"),
    path("home/",views.accueil,name="accueil"),
    path("", views.login, name="login"),
    path("ok/", courseViews.ok, name="ok"),
    path("logout/", views.logout, name="logout"),
    path("admin/", adminViews.admin, name="admin"),
    path("admin/role/", adminViews.role, name="role"),
    path("admin/role/<str:view>", adminViews.role, name="roleView"),
    path("suivi/", views.yes, name="yes"),
    path("fiche/", views.fiche, name="fiche"),
    path('sujet/edit/<int:sujet_id>/', courseViews.editTopic, name='edit_topic'),
    path('sujet/delete/<int:sujet_id>/', courseViews.deleteTopic, name='delete_topic'),
    path('course/<str:idue>/gestion/', courseViews.gestion_etape, name='gestion_etape'),
    path("course/<str:idue>/steps/", courseViews.afficher_etapes_ue, name="steps"),
    path("course/inscription",courseViews.inscription,name="inscription"),
    path("course/inscription/<str:idue>/<str:nom>",courseViews.inscriptionValidation,name="inscription"),
    path("course/mycourses",courseViews.mycourses,name="mycourses"),
    path("switch_role/<str:role>", views.switchRole, name="switch_role"),
    path("echeance/",views.echeance,name="echeance"),
    #path("steps/<int:idue>",courseViews.afficher_etapes_ue,name="afficherEtape"),
    path("echeance/<int:delivrable>",views.delivrable,name="delivrable"),
    path("sujet/reservation",courseViews.reservation,name="reservation"),
    path("sujet/reservation/<int:idsujet>", courseViews.reservationValidation, name="reservation"),
    path("sujet/reservation/confirmation/<int:idsujet>",courseViews.reservationConfirmation,name="confirmation"),
    path("sujet/history/", courseViews.vue_historique, name="vue_historique"),
    path("sujet/history/<int:annee>", courseViews.vue_historiqueAnnee, name="vue_historaieAnnee"),
    path("sujet/cours_timeline/", courseViews.query_vue_historique, name="cours_timeline_view")


]

urlpatterns += staticfiles_urlpatterns()