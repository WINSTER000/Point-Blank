from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Firearms

# Create your views here.
class Firearm:
    def home(self,request):
        # if request.session.get("user_id") is not None:
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            fetchFirearms = Firearms.objects.order_by('-id')[:4]
            username = request.session.get("username", None)
            total_Firearms = len(fetchFirearms)
            all_firearms = []
            if fetchFirearms:
                for i in fetchFirearms:
                    all_firearms.append({"id":i.id,"firearms_name":i.firearms_name,"firearms_image":i.firearms_image,"firearms_price":i.firearms_price,"firearms_description":i.firearms_description})
                    context = {"firearms":fetchFirearms,"total_Firearms":total_Firearms,"username":username,"cart_count":cart_count}
                return render(request,"index.html",context)
            else:
                return JsonResponse({"firearms":[]})
        # else:
        #     return HttpResponseRedirect("login")

    def about(self,request):
        # if request.session.get("user_id") is not None:
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            username = request.session.get("username", None)
            context = {"username":username,"cart_count":cart_count}
            return render(request,"about.html",context)
        # else:
        #     return HttpResponseRedirect("login")
        
    def fetch_all_firearms(self,request):
        # if request.session.get("user_id") is not None:
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            username = request.session.get("username", None)
            fetchFirearms = Firearms.objects.order_by('-id')
            total_Firearms = len(fetchFirearms)
            all_firearms = []
            if fetchFirearms:
                for i in fetchFirearms:
                    all_firearms.append({"id":i.id,"firearms_name":i.firearms_name,"firearms_image":i.firearms_image,"firearms_price":i.firearms_price,"firearms_description":i.firearms_description})
                    context = {"firearms":fetchFirearms,"total_Firearms":total_Firearms,"username":username,"cart_count":cart_count}
                return render(request,"arsenal.html",context)
                # return JsonResponse({"firearms":all_firearms})
            else:
                return JsonResponse({"firearms":[]})
        # else:
        #     return HttpResponseRedirect("login")

    def firearm_details(self,request):
        if request.session.get("user_id") is not None:
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            username = request.session.get("username", None)
            if request.GET.get("id") is not None and request.GET.get("id") != "":
                try:
                    fetchFirearms = Firearms.objects.get(pk = request.GET["id"])
                    context = {
                        "firearm_id":fetchFirearms.id,
                        "firearm_name":fetchFirearms.firearms_name,
                        "firearm_image":fetchFirearms.firearms_image,
                        "firearm_price":fetchFirearms.firearms_price,
                        "firearm_description":fetchFirearms.firearms_description,
                        "firearm_ammo":fetchFirearms.firearms_ammo,
                        "firearm_ammo_capacity":fetchFirearms.firearms_ammo_capacity,
                        "firearm_caliber":fetchFirearms.firearms_caliber,
                        "firearm_barrel_length":fetchFirearms.firearms_barrel_length,
                        "firearm_overall_length":fetchFirearms.firearms_overall_length,
                        "firearm_weight":fetchFirearms.firearms_weight,
                        "firearm_finish":fetchFirearms.firearms_finish,
                        "firearm_action":fetchFirearms.firearms_action,
                        "username":username,
                        "cart_count":cart_count,
                    }
                    return render(request,"firearm-details.html",context)
                except Firearms.DoesNotExist:
                    return HttpResponseRedirect("arsenal")
            else:
                return HttpResponseRedirect("arsenal")
        else:
            return HttpResponseRedirect("login")
        
