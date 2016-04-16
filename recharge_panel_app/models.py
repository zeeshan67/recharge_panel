
# Create your models here.
from django.db import models
from uuid import uuid4

from uuid import UUID
import uuid
from django_extensions.db.fields import UUIDField


class AddUser(models.Model):

	firstname =models.CharField(max_length=500, null=True, blank=True)

	lastname = models.CharField(max_length=500, null=True, blank=True)
	company = models.CharField(max_length=500, null=True, blank=True)

	username = models.CharField(max_length=500, null=True, blank=True)

	email_id = models.CharField(max_length=500, null=True, blank=True)

	phonenumber = models.CharField(max_length=12, null=True, blank=True)

	# role = models.ChoiceField(
	# 	widget=models.Select(attrs={'class': 'form-control', 'title': 'Select Role'}), required=True)


	address = models.CharField(max_length=1000, null=True, blank=True)

	pin_code = models.CharField(max_length=500, null=True, blank=True)

	city = models.CharField(max_length=500, null=True, blank=True)
	state = models.CharField(max_length=500, null=True, blank=True)
	country = models.CharField(max_length=500, null=True, blank=True)

	passkey = models.CharField(max_length=256, null=True, blank=True)
	cpasskey =models.CharField(max_length=256, null=True, blank=True)

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

