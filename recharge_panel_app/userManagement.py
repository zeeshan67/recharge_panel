__author__ = 'zeeshan'

from django.db import models


class AddUser(models.Model):
	firstname = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), max_length=30,
								 regex='[A-z]+$', error_message='Invalid Name', required=True)

	lastname = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), max_length=30,
								regex='[A-z]+$', error_message='Invalid Last Name', required=False)

	company = models.CharField(widget=models.TextInput(attrs={'class': 'form-control'}), max_length=256,
							  required=False)

	username = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), max_length=60,
								regex='[A-z0-9_]+$', error_message='Invalid Username', required=True)

	email_id = models.EmailField(widget=models.TextInput(attrs={'class': 'form-control'}), max_length=256,
								required=True)

	phonenumber = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}),
								   regex='[0-9]{10}$', max_length=10, min_length=10, required=False)

	role = models.ChoiceField(
		widget=models.Select(attrs={'class': 'form-control', 'title': 'Select Role'}), required=True)


	address = models.CharField(widget=models.Textarea(attrs={'class': 'form-control'}), max_length=256,
							  required=False)

	pin_code = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), regex='[0-9]{6}$',
								error_message='Invalid', min_length=6, max_length=6, required=False)

	city = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), regex='[A-z]+$',
							error_message='Invalid', max_length=50, required=False,
							min_length=3)
	state = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), regex='[A-z]+$',
							 error_message='Invalid', max_length=50, required=False,
							 min_length=3)

	country = models.RegexField(widget=models.TextInput(attrs={'class': 'form-control'}), regex='[A-z]+$',
							   error_message='Invalid', max_length=50,
							   required=False, min_length=3)

	passkey = models.CharField(widget=models.PasswordInput(attrs={'class': 'form-control'}), max_length=256,
							  required=True)

	cpasskey = models.CharField(widget=models.PasswordInput(attrs={'class': 'form-control'}), max_length=256,
							   required=True)

	def __init__(self, *args, **kwargs):
		user_id = kwargs.pop('user_id')
		super(AddUser, self).__init__(*args, **kwargs)

		# search_dict = {"user_id": int(user_id)}
		# login_user_role = search_by_id(search_dict, {'_id': 0, 'role': 1})
		# if login_user_role == "reseller":
		# 	role_data = ["reseller", "user"]
		# else:
		# 	role_data = get_roles({'_id': 0, 'role_type': 1})
		# for each_role in role_data:
		# 	role_tuple += ((str(each_role['role_type']), (str(each_role['role_type']))),)
        #
		# self.fields['role'].choices = role_tuple
