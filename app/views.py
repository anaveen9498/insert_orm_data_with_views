from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.



def Topic_details(request):
    t_name=input('Enter topic name')
    t_obj=Topic.objects.get_or_create(topic_name=t_name)[0]
    t_obj.save()
    return HttpResponse('Data inserted successfully')


def web_details(request):
    t_name=input('Enter Tname')
    t_obj=Topic.objects.get_or_create(topic_name=t_name)[0]
    t_obj.save()


    p_name=input('Enter p_name')
    url=input('Enter url')
    w_obj=Webpage.objects.get_or_create(topic_name=t_obj,player_name=p_name,url=url)[0]
    w_obj.save()
    return HttpResponse('Successfully Data Added')


def loc_details(request):
    t_name=input('Enter T_Name')
    p_name=input('Enter p_name')
    url_name=input('Enter url_name')
    age=input('Enter Age')
    place_name=('Enter place_name')

    
    t_obj=Topic.objects.get_or_create(topic_name=t_name)[0]
    t_obj.save()


    
    web_obj=Webpage.objects.get_or_create(topic_name=t_obj,player_name=p_name,url=url_name)[0]
    web_obj.save()

    
    loc_obj=Location.objects.get_or_create(player_name=web_obj,age=age,place=place_name)[0]
    loc_obj.save()


    return HttpResponse('Successfully Data Inserted')




