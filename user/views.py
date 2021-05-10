from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, View, FormView, DetailView


from user.models import User
from user.forms import AdduserForm


class Userlist(ListView):
    model = User
    template_name = 'userlist.html'

class Getuser(DetailView):

        model = User

        template_name = 'get_user.html'





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
#    success_url = ('adduser')
    def form_valid(self, form):
        form.save()
        item = form.save()
        self.pk = item.pk

        response = super().form_valid(form=form )
#
        return response
#
    def get_success_url(self):

        return reverse('added-user', kwargs={'pk': self.pk})

class Addeduser(DetailView):
    model = User
    template_name = 'added_user.html'

class Edituser(View):
    def post(self, request, id):


            user = User(
                username=request.POST['username'],
                email=request.POST['email'],
                id=id
            )

            user.save()
            return HttpResponse(f'<strong>Edited <br> {user.username} <br>{user.email}')


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
