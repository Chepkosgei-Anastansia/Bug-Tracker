from django.shortcuts import render
from .models import Ticket,Project
from .serializers import ProjectSerializer, TicketSerializer

from django.views.generic.list import ListView 


class ProjectList(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreate(CreateView):
    model = Project
    fields = ['title','description','lead_developer_id', 'owner']
    success_url = reverse_lazy('projects')  

class ProjectUpdate(UpdateView):
    model = Project 
    fields = ['title','description','lead_developer_id', 'owner']
    success_url = reverse_lazy('projects')

class ProjectDelete(DeleteView):
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('projects')
    

class TicketList(ListView):
    model = Ticket
    template_name = 'projects/tickets.html'
    context_object_name = 'tickets'

class TicketDetail(DetailView):
    model = Ticket
    template_name = 'projects/ticket_detail.html'
    context_object_name = 'ticket'

class TicketCreate(CreateView):
    model = Ticket
    fields = ['title','description','project_id','lead_developer_id', 'priority', 'status','category']
    success_url = reverse_lazy('tickets')  

class TicketUpdate(UpdateView):
    model = Ticket 
    fields = ['title','description','lead_developer_id', 'priority','status','category']
    success_url = reverse_lazy('tickets')

class TicketDelete(DeleteView):
    model = Ticket
    context_object_name = 'tickets'
    success_url = reverse_lazy('tickets') 



