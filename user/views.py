from django.shortcuts import render
from django.core.exceptions import ValidationError

from user.models import User


def userlist(request):
    users = User.objects.all()

    context = {'users': users,
               'id': id}

    return render(
        template_name='userlist.html',
        request=request,
        context=context
    )
def get_userid(request, id):
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

def delete_userid(request, id):
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
def add_user(request):
    if request.method == 'POST':
        user = User(
        username=request.POST['username'],
        email=request.POST['email'],
        )

        if len(user.username) == 0 or len(user.email) == 0:
            raise ValidationError('''Please don't leave empty field''')


        user.save()

        context = {'username': user.username,
        'email': user.email}

        return render(
            template_name='added_user.html',
            request=request,
            context=context
        )

    elif request.method == 'GET':
        return render(
            template_name='add_user.html',
            request=request,
            context={},
        )
def edit_userid(request, id):
    try:
        if request.method == 'POST':
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

        elif request.method == 'GET':
            user = User.objects.get(id=id)

            context = {'username': user.username,
                       'email': user.email,
                       'id': id}
            return render(
                template_name='edit_userid.html',
                request=request,
                context=context,
            )
    except Exception as exception:
        context = {'id': id}
        return render(
            template_name='id_does_not_exist.html',
            request=request,
            context=context
        )
