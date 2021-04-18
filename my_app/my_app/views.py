from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

def login(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
		id_type = request.POST.get('id_type')
		if id_type == '1':
			return HttpResponse('admin :'+uname +' '+pwd+' '+id_type)
		elif id_type == '2':
			check_user_f = Enseignant.objects.filter(username_ens=uname)
			check_user = check_user_f.first()
			if check_user is None:
				return HttpResponse('Username not found')
			elif check_user.pwd_ens == pwd:
				request.session['ens'] = uname
				print('login successed : '+request.session['ens'])
				return redirect('enseignant/acueil')
			else:
				return HttpResponse('Please enter valid Username or Password.')
		elif id_type == '3':
			check_user_f = Eleve.objects.filter(username_elv=uname)
			check_user = check_user_f.first()
			if check_user is None:
				return HttpResponse('Username not found')
			elif check_user.pwd_elv == pwd:
				request.session['elv'] = uname
				return redirect('eleve/acueil')
			else:
				return HttpResponse('Please enter valid Username or Password.')
			#return HttpResponse('eleve :'+uname +' '+pwd+' '+id_type)
		else:
			return HttpResponse('no id_type value returned'+uname +' '+pwd+' ')
	else:
		return render(request, 'login.html', {})

def eleve(request):
	try:
		user = request.session['elv']
		check_user_f = Eleve.objects.filter(username_elv=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'eleve.html', ctx)
	except:
		return HttpResponse('login required')


def eleve_profile(request):
	try:
		user = request.session['elv']
		check_user_f = Eleve.objects.filter(username_elv=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'eleve_profile.html', ctx)
	except:
		return HttpResponse('login required')


def eleve_machine(request):
	try:
		user = request.session['elv']
		check_user_f = Eleve.objects.filter(username_elv=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'eleve_machine.html', ctx)
	except:
		return HttpResponse('login required')

def eleve_mail(request):
	try:
		user = request.session['elv']
		check_user_f = Eleve.objects.filter(username_elv=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'eleve_mail.html', ctx)
	except:
		return HttpResponse('login required')	

def enseignant(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'enseignant.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_exercices(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'enseignant_exercices.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_instances(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'enseignant_instances.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_images(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		vm_result = Virtualmachine.objects.all()
		ctx = {'check_user' : check_user,
				'vm_result' : vm_result }
		return render(request, 'enseignant.html', ctx)
	except:
		return HttpResponse('login required')


def enseignant_supervision(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		ctx = {'check_user' : check_user}
		return render(request, 'enseignant_supervision.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_mail(request):   #recieved
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		msgs_result = Message.objects.filter(type=0)
		ctx = {'check_user' : check_user,
				'msgs_result' : msgs_result}
		return render(request, 'enseignant_mail.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_mail_sent(request):   #sent
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		msgs_result = Message.objects.filter(type=1)
		ctx = {'check_user' : check_user,
				'msgs_result' : msgs_result}
		return render(request, 'enseignant_mail_sent.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_mail_compose(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
		ctx = {'check_user' : check_user,
				'form' : form}
		return render(request, 'enseignant_mail_compose.html', ctx)
	except:
		return HttpResponse('login required')
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

def adminstrator(request):
	#eleve_result = Eleve.objects.filter(id_eleve=1)
	eleve_result = Eleve.objects.all()
	enseignants_result = Enseignant.objects.all()
	score_result = Score.objects.all()
	ctx = {'eleve_result' : eleve_result,
			'enseignants_result': enseignants_result,
			"score_result":score_result}
	return render(request,'admin.html',ctx)

def logout_elv(request):
	try:
		del request.session['elv']
	except:
		return redirect('/')
	return redirect('/')


def logout_ens(request):
	try:
		del request.session['ens']
	except:
		return redirect('/')
	return redirect('/')

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