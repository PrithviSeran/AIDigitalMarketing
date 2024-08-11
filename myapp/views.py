from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from PrinceScraping.PrinceScraping.spiders.get_businesses import GetBusinessWebsites
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import MyForm, CustomUserCreationForm, PagesWanted
from django.contrib.auth import views as auth_views
from .forms import CampaignForm
from .models import BusinessDomains
from .models import NewCampaign as Campaign
from scrapy.exceptions import CloseSpider
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


#CURRENT USER


def home(request):

    return render(request, "index.html")


@login_required
def main(request):

    user =  User.objects.get(username=request.user)

    campaigns = Campaign.objects.filter(user = user)

    if request.method == 'POST':
        form = Campaign()

        form.user = user
        form.name = request.POST.get('campaign-name')
        form.use = request.POST.get('campaign-use')
        form.user_info = request.POST.get('user-info')
        form.purpose = request.POST.get('campaign-purpose')
        form.target_audience = request.POST.get('target-audience')

        form.save()

        return render(request, "new-main.html", {"campaigns": campaigns})


    return render(request, "new-main.html", {"campaigns": campaigns})


def login_custom(request, *args, **kwargs):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or do something else
            return redirect('main')  # Assuming 'dashboard' is a URL name
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
        
    else:
        if request.user.is_authenticated:

            return redirect('main')
        else:
            return auth_views.LoginView.as_view(template_name='login.html')(request, *args, **kwargs)

    #return render(request, "login.html")


def register(request):

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        else:
            return render(request, "register.html", {"form": form})

    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_custom')


def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)

        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect('campaign')  # Replace 'success_page' with your desired redirect URL
    else:
        form = CampaignForm()

    return render(request, 'create_campaign.html', {'form': form})


def campaign(request, id):

    campaign = get_object_or_404(Campaign, id=id)#for all the records 

    domains = BusinessDomains.objects.filter(campaign_id = id)

    #for business in domains_for_campaign:
    #        domains.append(business.name)

    return render(request, 'new-campaign.html', {'campaign': campaign, 'domains': domains})


def domain(request, id):

    return HttpResponse(str(id))