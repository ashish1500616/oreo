from django import forms
# from .models import UserProfileInfo
# from django.contrib.auth.models import User


from .models import Image



# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = User  # connected to already defined mode in django.
#         fields = ('username', 'email', 'password')


# # class UserProfileForm(forms.ModelForm):

# #     class Meta():
# #         model = UserProfileInfo
# #         fields = ('portfolio_site', 'profile_pic')

class ImageForm(forms.ModelForm):

	class Meta:
		model =Image
		fields=("__all__")