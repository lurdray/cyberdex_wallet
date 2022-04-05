from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

from .forms import *
from wallet.ray import *
from wallet.models import AppUser



def IndexView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/wallet.html", context)

def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)

				print("11111111111111111111111111111111")
				messages.success(request, "Welcome Onboard")
				return HttpResponseRedirect(reverse("wallet:index"))

			else:
				print("22222222222222222222222222222222")
				messages.warning(request, "Sorry, Invalid Login Details")
				return HttpResponseRedirect(reverse("wallet:sign_in"))

		else:
			print("33333333333333333333333333333333333333")
			messages.warning(request, "Sorry, Invalid Login Details")
			return HttpResponseRedirect(reverse("wallet:sign_in"))


	else:
		context = {}

		return render(request, "wallet/sign-in.html", context )




def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)
		email = request.POST.get("username")
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")

		app_users = AppUser.objects.filter(user__username=request.POST.get("username"))

		if request.POST.get("password2") != request.POST.get("password1"):
			messages.warning(request, "Make sure both passwords match")
			print("passwords didn't match")
			return HttpResponseRedirect(reverse("wallet:sign_up"))

		elif len(app_users) > 0:
			messages.warning(request, "Email Address already taken, try another one!")
			print("email address already taken")
			return HttpResponseRedirect(reverse("wallet:sign_up"))
			
		else:
			user = form.save()
			user.set_password(request.POST.get("password1"))
			user.save()

			app_user = AppUser.objects.create(user=user)
			app_user.save()

			user = app_user.user
			user.email = email
			user.save()

			wallet = CreateWallet(user.email)
			wallet_address = wallet["address"]
			wallet_key = wallet["private_key"]
			wallet_phrase0 = wallet["passphrase0"]
			wallet_phrase1 = wallet["passphrase1"]
			wallet_phrase2 = wallet["passphrase2"]
			wallet_phrase3 = wallet["passphrase3"]
			wallet_phrase4 = wallet["passphrase4"]
			wallet_phrase5 = wallet["passphrase5"]
			wallet_phrase6 = wallet["passphrase6"]
			wallet_phrase7 = wallet["passphrase7"]
			wallet_phrase8 = wallet["passphrase8"]
			wallet_phrase9 = wallet["passphrase9"]
			wallet_phrase10 = wallet["passphrase10"]
			wallet_phrase11 = wallet["passphrase11"]

			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key

			app_user.passphrase0 = str(wallet_phrase0)
			app_user.passphrase1 = wallet_phrase1
			app_user.passphrase2 = wallet_phrase2
			app_user.passphrase3 = wallet_phrase3
			app_user.passphrase4 = wallet_phrase4
			app_user.passphrase5 = wallet_phrase5
			app_user.passphrase6 = wallet_phrase6
			app_user.passphrase7 = wallet_phrase7
			app_user.passphrase8 = wallet_phrase8
			app_user.passphrase9 = wallet_phrase9
			app_user.passphrase10 = wallet_phrase10
			app_user.passphrase11 = wallet_phrase11

			app_user.save()

			if user:
				if user.is_active:
					login(request, user)

					app_user = AppUser.objects.get(user__pk=request.user.id)

					messages.warning(request, "Save your passphrase")
					return HttpResponseRedirect(reverse("wallet:generate"))


	else:
		form = UserForm()
		context = {"form": form}

		return render(request, "wallet/sign-up.html", context )




def GenerateSeedView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":

		pass



	else:
		context = {"app_user": app_user}


		return render(request, "wallet/generate-seed.html", context )



def SeedPhraseView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":

		passphrase0 = request.POST.get("passphrase0")
		passphrase1 = request.POST.get("passphrase1")
		passphrase2 = request.POST.get("passphrase2")
		passphrase3 = request.POST.get("passphrase3")
		passphrase4 = request.POST.get("passphrase4")
		passphrase5 = request.POST.get("passphrase5")
		passphrase6 = request.POST.get("passphrase6")
		passphrase7 = request.POST.get("passphrase7")
		passphrase8 = request.POST.get("passphrase8")
		passphrase9 = request.POST.get("passphrase9")
		passphrase10 = request.POST.get("passphrase10")
		passphrase11 = request.POST.get("passphrase11")

		if str(app_user.passphrase0) == str(passphrase0) and str(app_user.passphrase1) == str(passphrase1) and str(app_user.passphrase2) == str(passphrase2) and str(app_user.passphrase3) == str(passphrase3) and str(app_user.passphrase4) == str(passphrase4) and str(app_user.passphrase5) == str(passphrase5) and str(app_user.passphrase6) == str(passphrase6) and str(app_user.passphrase7) == str(passphrase7) and str(app_user.passphrase8) == str(passphrase8) and str(app_user.passphrase9) == str(passphrase9) and str(app_user.passphrase10) == str(passphrase10) and str(app_user.passphrase11) == str(passphrase11):
			app_user.status = True
			app_user.save()

			messages.warning(request, "Successful!")
			return HttpResponseRedirect(reverse("wallet:index"))

		else:
			messages.warning(request, "Not Successful!")
			return HttpResponseRedirect(reverse("wallet:seedphrase"))




	else:
		context = {"app_user": app_user}

		return render(request, "wallet/seedphrase.html", context )








def SendView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		address = request.POST.get("address")
		amount = request.POST.get("amount")

		resp = SendCoin(app_user.wallet_address, app_user.wallet_key, address, amount)

		print(resp)

		messages.warning(request, "Successful!")
		return HttpResponseRedirect(reverse("wallet:index"))



	else:
		context = {}

		return render(request, "wallet/send.html", context )

def ReceiveView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/receive.html", context )


def TransactionView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/transaction.html", context )


def ReferralView(request):
	if request.method == "POST":
		pass


	else:
		context = {}

		return render(request, "wallet/referral.html", context )
