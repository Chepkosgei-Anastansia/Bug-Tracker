
from django.contrib import admin
from django.urls import path
from .views import ProjectCreate, ProjectDelete, ProjectDetail, ProjectList, ProjectUpdate, TicketCreate, TicketDetail,TicketDelete, TicketUpdate, TicketList
  
urlpatterns = [
    path('', ProjectList.as_view(), name='projects'),
    path('project/<str:pk>', ProjectDetail.as_view(), name = 'project'),
    path('project-create/', ProjectCreate.as_view(), name='project-create'),
    path('project-update/<str:pk>/', ProjectUpdate.as_view(), name='project-update'),
    path('project-delete/<str:pk>/', ProjectDelete.as_view(), name='project-delete'),

    path('', TicketDetail.as_view(), name='ticketss'),
    path('ticket/<str:pk>', TicketDetail.as_view(), name = 'ticket'),
    path('ticket-create/', TicketCreate.as_view(), name='ticket-create'),
    path('ticket-update/<str:pk>/', TicketUpdate.as_view(), name='ticket-update'),
    path('ticket-delete/<str:pk>/', TicketDelete.as_view(), name='ticket-delete'),
]