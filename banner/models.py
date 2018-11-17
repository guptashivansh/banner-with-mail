from django.db import models

# Create your models here.



class banner(models.Model):
	name 					= models.CharField(max_length=120, default="banner")	
	start_date				= models.DateField(null=True, blank=True)
	end_date				= models.DateField(null=True, blank=True)
	total_price				= models.IntegerField(null=True, blank=True)
	installation_date		= models.DateField(null=True, blank=True)
	removal_date			= models.DateField(null=True, blank=True)
	number_of_installments	= models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

class installment(models.Model):
	installment_price	= models.IntegerField(null=True, blank=True)
	receiving_date		= models.DateField(null=True, blank=True)
	banner_linked_to	= models.ForeignKey(banner, 
							on_delete= models.CASCADE, 
							related_name='installmentnumber')