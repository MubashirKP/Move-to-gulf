import json
from django.shortcuts import render
from models import *
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def createJson():
  jsonData = {}
  Cities = Job_Location.objects.all()
  Locations = []
  for city in Cities:
    cityData = city.get_json()
    Locations.append(cityData)
  jsonData['locations'] = Locations

  Types = Job_Type.objects.all()
  Type = []
  for type in Types:
    TypeData = type.get_json()
    Type.append(TypeData)
  jsonData["types"] = Type

  Categorys = Job_Category.objects.all()
  Category = []
  for category in Categorys:
    CategoryData = category.get_json()
    Category.append(CategoryData)

  jsonData["category"] = Category
  jsonData = json.dumps(jsonData)
  return jsonData


def postjob(request):

  jsonData = createJson()
  return render(request, 'post-job.html',{'autofillData':jsonData})

def index(request):

  posted_data =[]
  Posts = Posted_Jobs.objects.filter(verified=True)[0:10]
  for post in Posts:
    posted_data.append(post.get_json());

  posted_data = json.dumps(posted_data)
  jsonData = createJson()

  return render(request,"index.html" ,{"posts":posted_data,"autofill":jsonData})

def listing(request):

  jobs_data =[]
  Jobs_list = Posted_Jobs.objects.filter(verified=True)
  for Jobs in Jobs_list :
    jobs_data.append(Jobs.get_json());
  paginator = Paginator(jobs_data, 10)  # Show 10 contacts per page

  page = request.GET.get('page')
  try:
    jobs = paginator.page(page)

  except PageNotAnInteger:
        # If page is not an integer, deliver first page.
    jobs = paginator.page(1)
  except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    jobs = paginator.page(paginator.num_pages)

  return render(request, 'listing.html', {"jobs": jobs,"autofill":createJson()})

def search(request):
  location = Job_Location.objects.get(id=request.POST['location'])
  category = Job_Category.objects.get(id=request.POST['category'])
  Jobs_list = Posted_Jobs.objects.filter(verified=True,job_location=location,job_category = category)
  search_results = []
  jsonData = {}
  for job in Jobs_list:
    job.get_json();
    search_results.append(job.get_json())

  paginator = Paginator(search_results, 10)  # Show 10 contacts per page

  page = request.GET.get('page')
  try:
    jobs = paginator.page(page)

  except PageNotAnInteger:
        # If page is not an integer, deliver first page.
    jobs = paginator.page(1)
  except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    jobs = paginator.page(paginator.num_pages)
  return render(request, 'listing.html', {"jobs": jobs,"autofill":createJson()})

def jobdetail(request,jobid):
  job_list = Posted_Jobs.objects.get(id=jobid)
  job_list = job_list.get_json()
  return render(request,'job-detail.html',{"joblist": job_list})

def aboutus(request):
  return render(request,'about.html')

def contact(request):
  return render(request,'contact.html')