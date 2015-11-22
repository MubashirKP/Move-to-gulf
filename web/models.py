from django.db import models

# Create your models here.
class Job_Location(models.Model):
  location = models.CharField(max_length = 128)
  country = models.CharField(max_length = 128)

  def get_json(self):
    return {"id": self.id,
            "title": self.location}

  def __str__(self):
    return self.location

class Job_Type(models.Model):
  type = models.CharField(max_length = 128)

  def get_json(self):
    return {"id": self.id,
            "type": self.type}

  def __str__(self):
    return self.type

class Job_Category(models.Model):
  category_name = models.CharField(max_length = 128)

  def get_json(self):
    return {"id": self.id,
            "name": self.category_name}

  def __str__(self):
    return self.category_name

class Posted_Jobs(models.Model):
  job_email = models.EmailField(max_length=70)
  job_title = models.CharField(max_length = 256)
  job_location = models.ForeignKey(Job_Location)
  job_type = models.ForeignKey(Job_Type)
  job_category = models.ForeignKey(Job_Category)
  job_desc = models.TextField()
  job_url = models.CharField(max_length = 256, null = True)
  job_expiring = models.DateField()
  job_company_name = models.CharField(max_length = 256)
  company_logo = models.ImageField(upload_to = "/static/uploads/companylogo/",null=True,blank=True )
  verified = models.BooleanField(default=False)
  def __str__(self):
     return self.job_title
  def get_json(self):
    return{
      "email" : self.job_email,
      "title": self.job_title,
      "location": self.job_location.location,
      "type": self.job_type.type,
      "category":self.job_category.category_name,
      "description":self.job_desc,
      "url": self.job_url
    }