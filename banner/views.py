from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from banner.models import banner, installment
from banner.forms import bannerForm, installmentForm



# Create your views here.
class BannerListView(ListView):
	queryset = banner.objects.all()

class BannerDetailView(DetailView):
	queryset = banner.objects.all()
	slug_field = 'name'

class BannerCreateView(CreateView):
	form_class = bannerForm
	template_name ="forms.html"
	success_url = "/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		return super(BannerCreateView,self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(BannerCreateView,self).get_context_data(*args, **kwargs)
		return context

class BannerUpdateView(UpdateView):
	form_class = bannerForm
	template_name ="forms.html"
	slug_field = 'name'
	success_url = "/"
	model= banner
	def form_valid(self, form):
		instance = form.save(commit=False)
		if bannerForm.has_changed:
			print(bannerForm.changed_data)
			# subject="Update Banner"
			# from_email = settings.EMAIL_HOST_USER
			# message="Yeh toh chal rahi hai"
			# to_email = [from_email,"guptashivansh007@gmail.com"]
			# send_mail(subject,
			# 		message,
			# 		from_email,
			# 		to_email,
			# 		fail_silently=False,)		
		return super(BannerUpdateView,self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(BannerUpdateView,self).get_context_data(*args, **kwargs)
		field_qs = self.get_object().name
		return context

class InstallmentCreateView(CreateView):
	form_class = installmentForm
	template_name ="forms.html"
	success_url = "/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		return super(InstallmentCreateView,self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(InstallmentCreateView,self).get_context_data(*args, **kwargs)
		return context

class InstallmentUpdateView(UpdateView):
	form_class = installmentForm
	template_name = "forms.html"
	success_url = "/"
	model = installment

	def form_valid(self, form):
		instance = form.save(commit=False)
		changed_fields = installmentForm.changed_data
		if 'receiving_date' in changed_fields:
			print("yeh nahi chalne waala")
		
			# subject="Update Installment"
			# from_email = settings.EMAIL_HOST_USER
			# message="Yeh toh chal rahi hai"
			# to_email = [from_email,"guptashivansh007@gmail.com"]
			# send_mail(subject,
			# 		message,
			# 		from_email,
			# 		to_email,
			# 		fail_silently=False,)		
		return super(InstallmentUpdateView,self).form_valid(form)

class BannerDeleteView(DeleteView):
	model = banner
	slug_field = 'name'
	success_url = '/'
