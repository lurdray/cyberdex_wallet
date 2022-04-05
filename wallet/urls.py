from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("sign-up/", views.SignUpView, name="sign_up"),
	path("sign-in/", views.SignInView, name="sign_in"),
	path("referral/", views.ReferralView, name="referral"),
	path("generate/", views.GenerateSeedView, name="generate"),
	path("seedphrase/", views.SeedPhraseView, name="seedphrase"),
	path("send/", views.SendView, name="send"),
	path("receive/", views.ReceiveView, name="receive"),
	path("transaction/", views.TransactionView, name="transaction"),
]