import json

from django.contrib.auth import get_user_model, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.users.forms import LoginForm


class LoginView(View):

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        user = self.authenticate(
            email=data.get('email'), password=data.get('password'),
        )

        if user is None:
            return JsonResponse({'message': 'error'}, status=400)

        login(self.request, user)

        return JsonResponse({'success_url': reverse('index_page')}, status=200)

    def authenticate(self, email, password):
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)

        return HttpResponseRedirect(reverse('index_page'))


class RegisterView(TemplateView):
    template_name = 'pages/authentication.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['login_form'] = LoginForm()
        context['register_form'] = LoginForm()

        return context