from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
			path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),
			path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
			path("FarmerLogin.html", views.FarmerLogin, name="FarmerLogin"),
			path("FarmerLoginAction", views.FarmerLoginAction, name="FarmerLoginAction"),
			path("Signup.html", views.Signup, name="Signup"),
			path("SignupAction", views.SignupAction, name="SignupAction"),	    	
			path("UserLogin.html", views.UserLogin, name="UserLogin"),
			path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
			path("AddDetails.html", views.AddDetails, name="AddDetails"),
			path("AddDetailsAction", views.AddDetailsAction, name="AddDetailsAction"),
			path("UpdatePrice", views.UpdatePrice, name="UpdatePrice"),
			path("PriceUpdateScreen", views.PriceUpdateScreen, name="PriceUpdateScreen"),
			path("PriceUpdateAction", views.PriceUpdateAction, name="PriceUpdateAction"),
			path("ViewFruitDetails", views.ViewFruitDetails, name="ViewFruitDetails"),
			path("ViewFarmer", views.ViewFarmer, name="ViewFarmer"),
			path("ViewUser", views.ViewUser, name="ViewUser"),
			path("ViewFruits", views.ViewFruits, name="ViewFruits"),
]