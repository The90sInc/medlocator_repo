from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from .forms import PharmacyForm

from .models import Pharmacy


# Create your views here.

#class become_pharmacy(View):
    #def post(self, request):
        # view logic
        #return redirect('frontpage')

def become_pharmacy(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)

        if form.is_valid():
            user = form.save('self')

            login(request, user)

            #pharmacy = Pharmacy.objects.create(name=user.username, created_by=user)
            newpharmacy = Pharmacy()
            newpharmacy.name = user.username
            newpharmacy.created_by = user
            #newItem.quantity = 1
            newpharmacy.save()

            return  redirect('frontpage')
    else:
        form = PharmacyForm()

    return render(request, 'pharmacy/become_pharmacy.html', {'form': form})
