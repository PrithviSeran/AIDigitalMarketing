from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, EmailDispatchForm
from .forms import CampaignForm
from .models import BusinessDomains
from .models import NewCampaign as Campaign
import os
from django.contrib.auth.models import User
from PrinceScraping.PrinceScraping.llama3 import llama_wrapper, FIND_EMAIL, generate_email_using_llama
from myapp.gmail_dispath import gmail_dispath
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password, validate_username
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
# Create your views here.

class ReactView(APIView):
  
    serializer_class = ReactSerializer

    """
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=10, choices=CAMPAIGN_USE_CHOICES)
    user_info = models.TextField()
    purpose = models.TextField()
    target_audience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    """

    def get(self, request):

        campaign = [ {"name": campaign.name,"use": campaign.use, "user_info": campaign.user_info, "purpose": campaign.purpose,"target_audience": campaign.target_audience, "created_at": campaign.created_at}  for campaign in NewCampaign.objects.all()]
        return Response(campaign)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)


class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
        

class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)


def home(request, *args, **kwargs):

    return render(request, "main.html")


class UserLogin(APIView):
     permission_classes = (permissions.AllowAny,)
     authentication_classes = (SessionAuthentication,)

     def get(self, request):
          if request.user.is_authenticated:
             
             user = request.user
             
             campaigns = Campaign.objects.filter(user = user)

             serializer = NewCampaignSerializer(campaigns, many=True)
             
             return Response({"message": True, "campaigns": serializer.data}, status=status.HTTP_200_OK)
          

     def post(self, request):

        data = request.data

        username_val = validate_username(data)
        password_val = validate_password(data)

        if not username_val or not password_val:
             return Response({"message": "Please enter your username and password"}, status=status.HTTP_200_OK)

        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
             user = serializer.check_user(data)

             if not user:
                return Response({"message": "Sorry, either password or username is inccorect, or you have not yet registered."}, status=status.HTTP_200_OK)

             login(request, user)

             campaigns = Campaign.objects.filter(user = user)

             serializer = NewCampaignSerializer(campaigns, many=True)

             return Response({"message": True, "campaigns": serializer.data}, status=status.HTTP_200_OK)          


class MainPage(APIView):
     
     #permission_classes = (permissions.IsAuthenticated,)
     #authentication_classes = (SessionAuthentication,)

     def get(self, request):
            user = request.user

            campaigns = Campaign.objects.filter(user = user)
            
            return Response({"message": True, "campaigns": campaigns}, status=status.HTTP_200_OK)
     
     def post(self, request):
           
           print(request.user)
           
           serializer = CampaignSerializer(data = request.data)
           
           if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response({"message": "Is this WHY?"}, status=status.HTTP_200_OK)


class CreateCampaign(APIView):
     
     permission_classes = (permissions.IsAuthenticated,)
     authentication_classes = (SessionAuthentication,)

     def get(self, request):
           
            print(request.GET)

            form = CampaignForm(request.GET)

            if form.is_valid():
                campaign = form.save(commit=False)
                campaign.user = request.user
                campaign.save()

                campaigns = Campaign.objects.filter(user = request.user)

                serializer = NewCampaignSerializer(campaigns, many=True)

                return Response({"campaigns": serializer.data}, status=status.HTTP_200_OK)
           

class CampaignBusinesses(APIView):
     
     def get(self, request):

        campaign_id = request.GET.get("id")
          
        domains = BusinessDomains.objects.filter(campaign_id = campaign_id)

        serializer = DomainsSerializer(domains, many=True)

        return Response({"domains": serializer.data}, status=status.HTTP_200_OK)

           
class UserLogout(APIView):
     permission_classes = (permissions.AllowAny,)
     authentication_classes = ()
     def post(self, request):
          logout(request)

          return Response(status=status.HTTP_200_OK)


class GetEmailContent(APIView):
    
    def get(self, request):
         
         about_myself = request.GET.get("user_info")
         purpose = request.GET.get("purpose")
         scraped_info = request.GET.get("content")
         
         llama_generated_email = generate_email_using_llama(about_myself, purpose, scraped_info)

         return Response({"email_content": llama_generated_email}, status=status.HTTP_200_OK)

     
class GetEmail(APIView):
     
     def get(self, request):
          
          content = request.GET.get("content")
          
          email = llama_wrapper(FIND_EMAIL, content)

          return Response({"email": email}, status=status.HTTP_200_OK)
          

class SendEmail(APIView):
     
     pass


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

    return render(request, 'new-campaign.html', {'campaign': campaign, 'domains': domains})


def domain(request, id, campaign_id):

    current_domain = get_object_or_404(BusinessDomains, id = id)

    lines_string = get_scraped_info(current_domain)

    email = llama_wrapper(FIND_EMAIL, lines_string)

    if request.method == 'POST':

        return redirect('generate_email', id, campaign_id, email)

    return render(request, 'domain.html', {'emailFound': email, "website_content": lines_string})


def generate_email(request, id, campaign_id, email_to):

    campaign = get_object_or_404(Campaign, id=campaign_id)#for all the records 
    current_domain = get_object_or_404(BusinessDomains, id = id)

    scraped_info = get_scraped_info(current_domain)

    llama_generated_email = generate_email_content(current_domain, campaign)

    if request.method == 'POST':

        user = request.user

        user_email = user.email

        gmail_dispath(user_email, email_to, llama_generated_email, "Test Subject")

        return HttpResponse("Sent Email")

    return render(request, 'generate_email.html', {'email_content': llama_generated_email, "website_content": scraped_info, "id": id, "campaign_id": campaign_id, "email_to": email_to})


def generate_email_content(current_domain, campaign):

    about_myself = campaign.user_info
    purpose = campaign.purpose
    scraped_info = get_scraped_info(current_domain)

    llama_generated_email = generate_email_using_llama(about_myself, purpose, scraped_info)

    return llama_generated_email


def get_scraped_info(current_domain):
    
    dir_path = "/Users/prithviseran/Documents/AIDigitalMarketingApp/ScrapedWebsites"

    domain_name = current_domain.domain

    completeName = os.path.join(dir_path, domain_name + ".txt")
                
    # Optionally, save the text to a file
    with open(completeName, 'r') as f:
        lines = f.readlines()

    lines_string = ''.join(lines)

    return lines_string