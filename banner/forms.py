from django import forms

from banner.models import banner, installment

# class bannerForm(forms.ModelForm):
# 	name 					= forms.CharField(max_length=120)	
# 	start_date				= forms.DateField()
# 	end_date				= forms.DateField()
# 	total_price				= forms.IntegerField()
# 	installation_date		= forms.DateField()
# 	removal_date			= forms.DateField()
# 	number_of_installments	= forms.IntegerField()

# 	def __init__(self, *args, **kwargs):
# 		super(bannerForm,self).__init__(*args,**kwargs)
# 		installment_field = installment.objects.filter(
# 			banner_linked_to=self.instance
# 			) 
# 		n=self.cleaned_data.get('number_of_installments')
# 		for i in range(n):
# 			field_name_1 = 'Installment_%s_in_rupees' %(i,)
# 			field_name_2 = 'Receiving date'
# 			self.fields[field_name_1] = forms.IntegerField(required=False)
# 			self.fields[field_name_2] = forms.DateField(required=False)
# 			try:
# 				self.initial[field_name_1] = installment_field[i].installment_price
# 				self.initial[field_name_2] = installment_field[i].receiving_date
# 			except IndexError:
# 				self.initial[field_name_1] = ""
# 				self.initial[field_name_2] = ""

# 		field_name_1 = 'installment_%s' % (i + 1,)
# 		field_name_2 = 'date' % (i + 1,)
# 		self.fields[field_name_1] = forms.CharField(required=False)
# 		self.fields[field_name_1] = ""
# 		self.fields[field_name_2] = forms.DateField(required=False)
# 		self.fields[field_name_2] = ""

# 	def clean(self):
# 		installment_field=set()
# 		i=0
# 		field_name_1 = 'Installment_%s_in_rupees' %(i,)
# 		field_name_2 = 'Receiving date'
# 		while self.cleaned_data.get(field_name_1):
# 			installment_price = self.cleaned_data.get('field_name_1')
# 			receiving_date	  = self.cleaned_data.get('field_name_2')
# 			i+=1
# 			field_name_1 = 'Installment_%s_in_rupees' %(i,)
# 			field_name_2 = 'Receiving date'
# 		self.cleaned_data["installment_field"] = installment_field

# 	def save(self):
# 		banner = self.instance
# 		banner.name = self.cleaned_data["name"]
# 		banner.start_date = self.cleaned_data["start_date"]
# 		banner.end_date = self.cleaned_data["end_date"]
# 		banner.total_price = self.cleaned_data["total_price"]
# 		banner.installation_date = self.cleaned_data["installation_date"]
# 		banner.removal_date = self.cleaned_data["removal_date"]
# 		banner.number_of_installments = self.cleaned_data["number_of_installments"]


# 		banner.installmentnumber.all().delete()
# 		for interest in self.cleaned_data["installment_field"]:
# 			installment.objects.create(
# 				installment_price=installment_price,
# 				receiving_date=receiving_date,
# 				banner_linked_to=banner_linked_to,
# 			)

# 	class Meta:
# 		model = banner



class bannerForm(forms.ModelForm):
	class Meta:
		model = banner
		fields=[
		'name',	
		'start_date',
		'end_date',
		'total_price',
		'installation_date',
		'removal_date',
		'number_of_installments',
		]

	def clean(self):
		start_date 			= self.cleaned_data.get("start_date")
		end_date   			= self.cleaned_data.get("end_date")
		installation_date	= self.cleaned_data.get("installation_date")
		removal_date		= self.cleaned_data.get("removal_date")
		if end_date <= start_date:
			msg = u"End date cannot be before or same as start date."
			self._errors["end_date"] = self.error_class([msg])

		if removal_date <= installation_date:
			msg = u"Removal date cannot be before or same as Installment date"
			self._errors["removal_date"] = self.error_class([msg])


class installmentForm(forms.ModelForm):
	class Meta:
		model = installment
		fields = [
		'installment_price',
		'receiving_date',
		'banner_linked_to',
		]