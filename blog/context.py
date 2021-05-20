from blog.models import Category
from django.contrib.auth.models import User

def getCategorys(request):
    categorys = Category.objects.values_list('id', 'name')
    
    return {
        'categorys': categorys
    }


def getUsers(request):
    users = User.objects.values_list('id', 'username')

    return {
        'users': users
    }