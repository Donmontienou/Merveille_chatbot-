from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email




def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())



def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())



def accueil(request):
    template = loader.get_template('accueilt.html')
    return HttpResponse(template.render())



def form(request):
    template = loader.get_template('formulaire.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        tel = request.POST['tel']
        email = request.POST['email']
        matricule = request.POST['email']
        password = request.POST['password']
        passe = request.POST['passe']

        if User.objects.filter(username=username):
            messages.error(request, "Ce nom d'utilisateur existe déjà")
            return redirect('login')

        if User.objects.filter(email=email):
            messages.error(request, "Cet email a déjà un compte")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit être alphanumérique")
            return redirect('register')


        if not firstname.isalnum():
            messages.error(request, "Le nom doit être alphanumérique")
            return redirect('register')



        if not username.isalnum():
            messages.error(request, "Le prénom doit être alphanumérique")
            return redirect('register')

        if password != passe:
            messages.error(request, "Les deux mots de passes doivent être identiques")
            return redirect('register')

        user = User.objects.create_user(username, email, password)   
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        messages.success(request, 'Votre compte a été crée avec succès')
        return redirect('login')

    return render(request, 'registerform.html')
"""try:
            validate_email(email)
        except:
            error = True
            message = "L'email n'est pas valide"
        if error == False:
            if password != cpassword:
                error = True
                message = "Les mots de passes doivent être identiques"
        
        user = User.objects.filter(email=email).first()
        if user:
            error = True
            message = f"Un utilisateur avec existe déjà avec ce email {email}"
        
        if error == False:
            print("username, firstname, lastname, telephone, email, matricule, password, cpassword")

    context = {
        'error':error,
        'message':message
    }

    return render(request, 'registerform.html', context)
"""




def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username , password=password)

        if user is not None:
            login(request, user)
            return redirect('accueil')
            #firstname = user.first_name
            #return render(request, 'accueil.html', {'firstname': firstname} )
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrecte")
            return redirect('login')

    return render(request, 'loginform.html')
"""
        if user:
            user = authenticate(username=user.username , password=password)
            if user:
                login(request, user)
                return redirect('accueil')
            else:
                print("Nom d'utilisateur ou mot de passe incorrecte")
        else:
            print("L'utilisateur n'existe pas")
    return render(request, 'loginform.html', {})
@login_required
"""



def accueil(request):
    return render(request, 'accueil.html')



def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecter')
    return redirect('accueil')



def chatroom(request):
    template = loader.get_template('chatroom.html')
    return HttpResponse(template.render())




