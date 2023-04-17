from django import forms

PROJECT_MANAGER = [
    ('Akunga Jeremiah','Akunga jeremiah'),
    ('Cynthia Toroitich', 'Cynthia Toroitich')
]

LEAD_DEVELOPER =[
    ('Irene', 'Irene'),
    ('Anastansia', 'Anastansia')
]
ROLE = [
    ('backend developer', 'Backend developer'),
    ('frontend developer', 'frontend developer'),
    ('Graphic Designer', 'Graphic designer')
]
PRIORITY =[
    ('High','High'),
    ('Moderate', 'Moderate'),
    ('Low','Low')
]
STATUS=[
    ('Open','Open'),
    ('Inprogress', 'Inprogress'),
    ('Closed','Closed')
]
CATEGORY =[
    ('FronctEnd','Frontend'),
    ('Backend', 'Backend'),
    ('API','API'),
    ('Database','Database'),
]
class ProjectForm(forms.Form):
    title = forms.CharField(label='Project Title', max_length=100)
    description = forms.CharField(label='Project Description', max_length=200)
    owner = forms.CharField(label='Project Owner', max_length=100)
    project_manager = forms.CharField(label='Project Manager', widget=forms.Select(choices= PROJECT_MANAGER))
    lead_developer = forms.CharField(label='Lead Developer', widget=forms.Select(choices= LEAD_DEVELOPER))

class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email Address', max_length=100)
    role = forms.CharField(label='User Role', widget=forms.Select(choices= ROLE))

class TicketForm(forms.Form):
    title = forms.CharField(label='Bug Name', max_length=50)
    description = forms.CharField(label='Bug Description ', max_length=50)
    priority = forms.CharField(label='Priority', widget=forms.Select(choices= PRIORITY))
    status = forms.CharField(label='Status', widget=forms.Select(choices= STATUS))
    category = forms.CharField(label='Category', widget=forms.Select(choices= CATEGORY))
    
    

