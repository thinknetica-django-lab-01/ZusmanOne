# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.http import HttpResponse
# from django.dispatch import receiver
#
# def send_mail(request):
#     html_content = get_template('edit/mail.html')
#     msg = EmailMultiAlternatives(subject='test',body=html_content,from_email='zusmanone1@gmail.com',to=[user.email,])
#     msg.attach_alternative(html_content,'text/html')
#     msg.send()
#
# @receiver()
