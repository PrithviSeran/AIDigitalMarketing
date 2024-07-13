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
from .models import Campaign, BusinessDomains
from scrapy.exceptions import CloseSpider


# Create your views here.

def home(request):

    return render(request, "index.html")


@login_required
def main(request):

    campaigns = Campaign.objects.all()

    if request.method == 'POST':
        form = Campaign()

        '''
        user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
        name = models.CharField(max_length=100)
        use = models.CharField(max_length=10, choices=CAMPAIGN_USE_CHOICES)
        user_info = models.TextField()
        purpose = models.TextField()
        target_audience = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        '''

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

        print(email)
        print(password)

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
            #print(form)
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
        print(form.is_valid())
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            print("here?????")
            return redirect('campaign')  # Replace 'success_page' with your desired redirect URL
    else:
        form = CampaignForm()

    return render(request, 'create_campaign.html', {'form': form})


def campaign(request, pk):

    campaign = get_object_or_404(Campaign, pk=1) #for all the records 


    domains_for_campaign = BusinessDomains.objects.filter(campaign=campaign)

    domains = set()

    for business in domains_for_campaign:
            domains.add(business.name)

    form = PagesWanted()

    return render(request, 'new-campaign.html', {'campaign': campaign, 'form': form, 'domains': domains})


def get_businesses(request, pk, count):

    campaign = get_object_or_404(Campaign, pk=pk)

    process = CrawlerProcess(get_project_settings())
    process.crawl(GetBusinessWebsites, campaign = campaign, count = count)
    #process.start()
    

    domains_for_campaign = BusinessDomains.objects.filter(campaign=campaign)
    #print(stored_data_set)

    visited_domains = set()

    for business in domains_for_campaign:
            visited_domains.add(business.name)


    return visited_domains


def testAPI(request):
    print("API WORKS!!!!")

    return HttpResponse("Please")

