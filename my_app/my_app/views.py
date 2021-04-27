from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from business.dict_to_json import dict_to_json
import requests


def index(request):
    if request.method == "POST":
        post_data = request.POST.copy()

        # there is a bunch of info to add to the post_data before transmitting it to json format
        del post_data['csrfmiddlewaretoken']

        # todo this data must be retrieved from the database
        post_data['vagrantEnvPath'] = "/home/pfe21/Documents/cyber_range/vagrant_environments/prof_1/exo1/instance-1"
        post_data['dockerImagesPaths'] = {"vulnerables/web-dvwa": "/home/pfe21/Desktop/TP01/dockerimage"}
        post_data['vagrantBoxesPaths'] = {}

        json_data = dict_to_json(post_data)
        print(json_data)
        print("------------------------------------------ requests -------------------------------------------")
        response = requests.post("http://localhost:8080/cyber_range_api/virtual_machine/create", json=json_data)
        print(response.status_code)
        return HttpResponseRedirect("/done")

    return render(request, "index.html")


def done(request):
    return HttpResponse("done")

def sign_up_admin(request):
	form = AdminForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request, 'signup_admin.html', {'form' : form})

def sign_up_ens(request):
	form = EnseignantForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request, 'signup_ens.html', {'form' : form})

def sign_up_eleve(request):
	form = EleveForm(request.POST)
	print(request.POST)
	if form.is_valid():
		form.save()
	return render(request, 'signup_eleve.html', {'form' : form})


def login(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
		id_type = request.POST.get('id_type')
		check_user_f = Admin.objects.filter(username_admin=uname)
		check_user = check_user_f.first()
		if check_user is None:
			# check if enseignant
			check_user_f = Enseignant.objects.filter(username_ens=uname)
			check_user = check_user_f.first()
			if check_user is None:
				#check if eleve
				check_user_f = Eleve.objects.filter(username_elv=uname)
				check_user = check_user_f.first()
				if check_user is None:
					return HttpResponse('Username not found')
				elif check_user.pwd_elv == pwd:
					request.session['elv'] = uname
					return redirect('eleve/acueil')
				else:
					return HttpResponse('Please enter valid Username or Password.')
			elif check_user.pwd_ens == pwd:
				request.session['ens'] = uname
				return redirect('enseignant/acueil')
			else:
				return HttpResponse('Please enter valid Username or Password.')
		elif check_user.pwd_admin == pwd:
			request.session['admin'] = uname
			print("session created : " + request.session['admin'])
			return redirect('adminstrator')
		else:
			return HttpResponse('Please enter valid Username or Password.')
	else:
		return render(request, 'login.html')

def login2(request):
	if request.method == 'POST':
		uname = request.POST.get('uname')
		pwd = request.POST.get('pwd')
		id_type = request.POST.get('id_type')
		if id_type == '1':
			check_user_f = Admin.objects.filter(username_admin=uname)
			check_user = check_user_f.first()
			if check_user is None:
				return HttpResponse('Username not found')
			elif check_user.pwd_admin == pwd:
				request.session['admin'] = uname
				print("session created : " + request.session['admin'])
				return redirect('adminstrator')
			else:
				return HttpResponse('Please enter valid Username or Password.')
		elif id_type == '2':
			check_user_f = Enseignant.objects.filter(username_ens=uname)
			check_user = check_user_f.first()
			if check_user is None:
				return HttpResponse('Username not found')
			elif check_user.pwd_ens == pwd:
				request.session['ens'] = uname
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
		return render(request, 'login.html')

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
		repert_f = Repertoire.objects.filter(enseignant=check_user)
		repert = repert_f.first()
		exercice_ress = Exercice.objects.filter(repertoire=repert)
		form = ExerciceForm(request.POST)
		if form.is_valid():
			form.save()
		ctx = {'check_user' : check_user,
			'exercice_ress' : exercice_ress,
			'form' : form}
		return render(request, 'enseignant_exercices.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_instances(request):
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		repert_f = Repertoire.objects.filter(enseignant=check_user)
		repert = repert_f.first()
		instance_ress = Instance.objects.filter(repertoire=repert)
		ctx = {'check_user' : check_user,
				'instance_ress' : instance_ress}
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
		return render(request, 'enseignant_images.html', ctx)
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
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
		ctx = {'check_user' : check_user,
				'msgs_result' : msgs_result,
				'form' : form}
		return render(request, 'enseignant_mail.html', ctx)
	except:
		return HttpResponse('login required')

def enseignant_mail_sent(request):   #sent
	try:
		user = request.session['ens']
		check_user_f = Enseignant.objects.filter(username_ens=user)
		check_user = check_user_f.first()
		msgs_result = Message.objects.filter(type=1)
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
		ctx = {'check_user' : check_user,
				'msgs_result' : msgs_result,
				'form' : form}
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
	try:
		user = request.session['admin']
		check_user_f = Admin.objects.filter(username_admin=user)
		print(check_user_f)
		check_user = check_user_f.first()
		print(check_user)
		eleve_result = Eleve.objects.all()
		enseignants_result = Enseignant.objects.all()
		score_result = Score.objects.all()
		ctx = {'eleve_result' : eleve_result,
				'enseignants_result': enseignants_result,
				"score_result":score_result,
				'check_user':check_user}
		return render(request,'admin.html',ctx)
	except:
		return HttpResponse('login required')

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

def logout_admin(request):
	try:
		print("deleting session : " + request.session['admin'])
		del request.session['admin']
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