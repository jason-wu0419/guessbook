from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Message


class MessageList(ListView):
    model = Message

class MessageDetail(DetailView):
    model = Message


class MessageCreate(CreateView):
    model = Message
    fields = '__all__'    
    success_url = reverse_lazy('msg_list')


class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')  