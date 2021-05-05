from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, FormView, DetailView
from django.core.exceptions import ValidationError

from user.models import User
from user.forms import AdduserForm


class Userlist(ListView):
    model = User
    template_name = 'userlist.html'

class Getuser(View):
    def get(self, request, id):
        try:
            xxx = User.objects.get(id=id)
            context = {'username': xxx.username,
                       'email': xxx.email}

            return render(
                template_name='added_user.html',
                request=request,
                context=context
            )
        except Exception as exception:
            context = {'id': id}
            return render(
                template_name='id_does_not_exist.html',
                request=request,
                context=context
            )

class Deleteuser(View):
    def get(self, request, id):
        try:
            xxx = User.objects.get(id=id)
            xxx.delete()
            context = {'username': xxx.username,
                       }

            return render(
                template_name='delete_userid.html',
                request=request,
                context=context
            )
        except Exception as exception:
            context = {'id': id}
            return render(
                template_name='id_does_not_exist.html',
                request=request,
                context=context
            )




class Adduser(FormView):
    form_class = AdduserForm
    template_name = 'add_user.html'
    success_url = reverse_lazy('user-list')


    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response



class Edituser(View):
    def post(self, request, id):


            user = User(
                username=request.POST['username'],
                email=request.POST['email'],
                id=id
            )

            user.save()

            context = {'username': user.username,
            'email': user.email,
                       'id': id}

            return render(
                template_name='added_user.html',
                request=request,
                context=context
            )

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)

            context = {'username': user.username,
                       'email': user.email,
                       'id': id}
            return render(
                template_name='edit_userid.html',
                request=request,
                context=context,
            )
        except Exception as  exception:
            context = {'id': id}
            return render(
                template_name='id_does_not_exist.html',
                request=request,
                context=context
            )
