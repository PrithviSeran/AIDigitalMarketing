from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from scrapy.crawler import CrawlerProcess
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EmailDispatchForm
from .forms import CampaignForm
from .models import BusinessDomains
from .models import NewCampaign as Campaign
import os
from django.contrib.auth.models import User
from PrinceScraping.PrinceScraping.llama3 import llama_wrapper, FIND_EMAIL, generate_email_using_llama
from myapp.gmail_dispath import gmail_dispath
from django.http import HttpResponse


def home(request):

    return render(request, "index.html")


@login_required
def main(request):

    print(request.user)

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

    return render(request, 'login.html')



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


def domain(request, id, campaign_id):

    current_domain = get_object_or_404(BusinessDomains, id = id)

    lines_string = get_scraped_info(current_domain)

    email = llama_wrapper(FIND_EMAIL, lines_string)

    if request.method == 'POST':

        return redirect('generate_email', id, campaign_id)

    return render(request, 'domain.html', {'emailFound': email, "website_content": lines_string})


def generate_email(request, id, campaign_id):

    campaign = get_object_or_404(Campaign, id=campaign_id)#for all the records 
    current_domain = get_object_or_404(BusinessDomains, id = id)

    about_myself = campaign.user_info
    purpose = campaign.purpose
    scraped_info = get_scraped_info(current_domain)

    llama_generated_email = generate_email_using_llama(about_myself, purpose, scraped_info)

    return render(request, 'generate_email.html', {'email_content': llama_generated_email, "website_content": scraped_info, "id": id})


def send_email(request, id):

    user = request.user

    user_email = user.email

    current_domain = get_object_or_404(BusinessDomains, id = id)

    lines_string = get_scraped_info(current_domain)

    email_to = llama_wrapper(FIND_EMAIL, lines_string)

    #email_from, email_to, email_content, email_subject

    gmail_dispath(user_email, email_to, lines_string, "Test Subject")

    return HttpResponse("Sent Email")


def get_scraped_info(current_domain):
    dir_path = "/Users/prithviseran/Documents/AIDigitalMarketingApp/ScrapedWebsites"

    domain_name = current_domain.domain

    completeName = os.path.join(dir_path, domain_name + ".txt")
                
    # Optionally, save the text to a file
    with open(completeName, 'r') as f:
        lines = f.readlines()

    lines_string = ''.join(lines)

    return lines_string