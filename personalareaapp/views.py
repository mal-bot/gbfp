from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required
def personal_area(request):
    user = {'name': 'minkika'}
    title = 'Личный кабинет'
    # if request.user.role = 'company':
    pa_favourites = [1, 2, 3]
        # .objects.filter(user=request.user)

    content = {
        'user': user,
        'title': title,
        'pa_favourites': pa_favourites,
    }

    return render(request, 'personalareaapp/pa_content.html', content)
