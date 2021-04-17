from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

def login(request):
    return render(request, 'login.html', {})

def eleve(request):
    return render(request, 'eleve.html', {})

def eleve_profile(request):
    return render(request, 'eleve_profile.html', {})

def eleve_machine(request):
    return render(request, 'eleve_machine.html', {})

def eleve_mail(request):
    return render(request, 'eleve_mail.html', {})

def enseignant(request):
    return render(request, 'enseignant.html', {})

def enseignant_exercices(request):
    return render(request, 'enseignant_exercices.html', {})

def enseignant_instances(request):
    return render(request, 'enseignant_instances.html', {})

def enseignant_images(request):
    vm_result = Virtualmachine.objects.all()
    return render(request, 'enseignant_images.html', { 'vm_result' : vm_result })

def enseignant_supervision(request):
    return render(request, 'enseignant_supervision.html', {})

def enseignant_mail(request):   #recieved
    msgs_result = Message.objects.filter(type=0)
    return render(request, 'enseignant_mail.html', {'msgs_result' : msgs_result})

def enseignant_mail_sent(request):   #sent
    msgs_result = Message.objects.filter(type=1)
    return render(request, 'enseignant_mail_sent.html', {'msgs_result' : msgs_result})

def enseignant_mail_compose(request):
    """if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get("subject")
            content = form.cleaned_data.get("content")
            return redirect("enseignant/mail")
        else:
            msg = 'Form is not valid'
    else :
        form = MessageForm()
    ctx = {'form' : form}"""
    return render(request, 'enseignant_mail_compose.html' , ctx)

def adminstrator(request):
    #eleve_result = Eleve.objects.filter(id_eleve=1)
    eleve_result = Eleve.objects.all()
    enseignants_result = Enseignant.objects.all()
    score_result = Score.objects.all()
    ctx = {'eleve_result' : eleve_result,
            'enseignants_result': enseignants_result,
            "score_result":score_result}
    return render(request,'admin.html',ctx)

class EleveAPI(viewsets.ModelViewSet):
    serializer_class = EleveSerializer
    queryset = Eleve.objects.all()

class EnseignantAPI(viewsets.ModelViewSet):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()

class ExerciceAPI(viewsets.ModelViewSet):
    serializer_class = ExerciceSerializer
    queryset = Exercice.objects.all()

class ImagedockerAPI(viewsets.ModelViewSet):
    serializer_class = ImagedockerSerializer
    queryset = Imagedocker.objects.all()

class InstanceAPI(viewsets.ModelViewSet):
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()

class RepertoireAPI(viewsets.ModelViewSet):
    serializer_class = RepertoireSerializer
    queryset = Repertoire.objects.all()

class VirtualmachineAPI(viewsets.ModelViewSet):
    serializer_class = VirtualmachineSerializer
    queryset = Virtualmachine.objects.all()

class GroupeAPI(viewsets.ModelViewSet):
    serializer_class = GroupeSerializer
    queryset = Groupe.objects.all()

class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class NiveauAPI(viewsets.ModelViewSet):
    serializer_class = NiveauSerializer
    queryset = Niveau.objects.all()

class ScoreAPI(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()