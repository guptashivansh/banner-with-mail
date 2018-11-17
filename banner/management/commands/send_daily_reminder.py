from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from banner.models import banner, installment

class Command(BaseCommand):
	def handle(self, **options):
		today = timezone.now().date()
		for obj in banner.objects.filter(
									end_date__day=today.day,
									end_date__month=today.month,
									end_date__year=today.year):

			subject="Reminder booking end date"
			from_email = "gupta.shivansh98@gmail.com"
			message="Yeh toh chal rahi hai"
			to_email = [from_email,"guptashivansh007@gmail.com"]
			send_mail(subject,
					message,
					from_email,
					to_email,
					fail_silently=False,)

		for obj in banner.objects.filter(
									installation_date__day=today.day,
									installation_date__month=today.month,
									installation_date__year=today.year):

			subject="Reminder installation date"
			from_email = "gupta.shivansh98@gmail.com"
			message="Yeh toh chal rahi hai"
			to_email = [from_email,"guptashivansh007@gmail.com"]
			send_mail(subject,
					message,
					from_email,
					to_email,
					fail_silently=False,)

		for obj in banner.objects.filter(
									removal_date__day=today.day,
									removal_date__month=today.month,
									removal_date__year=today.year):

			subject="Reminder removal date "
			from_email = "gupta.shivansh98@gmail.com"
			message="Yeh toh chal rahi hai"
			to_email = [from_email,"guptashivansh007@gmail.com"]
			send_mail(subject,
					message,
					from_email,
					to_email,
					fail_silently=False,)

		for obj in installment.objects.filter(
									receiving_date__day=today.day,
									receiving_date__month=today.month,
									receiving_date__year=today.year):

			subject="Reminder"
			from_email = "gupta.shivansh98@gmail.com"
			message="Yeh toh chal rahi hai"
			to_email = [from_email,"guptashivansh007@gmail.com"]
			send_mail(subject,
					message,
					from_email,
					to_email,
					fail_silently=False,)


