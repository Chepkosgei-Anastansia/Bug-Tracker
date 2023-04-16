from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email





class Project(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # project_manager_id = models.ForeignKey(User, on_delete= models.CASCADE)
    lead_developer_id = models.ForeignKey(User, on_delete= models.CASCADE)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Ticket (models.Model):
    PRIORITY_OPTIONS=(
        ('High', 'High'),
        ('Moderate', 'Moderate'),
        ('Low','Low'),
    )
    STATUS_OPTIONS =(
        ('Incomplete', 'Incomplete'),
        ('Complete', 'Complete'),
    )
  
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    lead_developer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length= 30, choices=PRIORITY_OPTIONS)
    status = models.CharField(max_length = 30, choices=STATUS_OPTIONS)
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title



    





