from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import Clients,Users,Orders
from firearms.models import Firearms
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from point_blank.settings import RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET
import razorpay

# Create your views here.
class Client:
    @csrf_exempt
    def success(self,request):
        if request.method == "POST":
            razorpay_payment_id = request.POST.get("razorpay_payment_id")
            razorpay_order_id = request.POST.get("razorpay_order_id")
            razorpay_signature = request.POST.get("razorpay_signature")
            amount = float(request.POST.get("amount")) / 10
            if request.session.get("user_id") is not None:
                user_id = request.session.get("user_id")
                clientInfo = Users.objects.get(id = user_id)
                email = clientInfo.user_email
                username = request.session["username"]
                if request.session.get("cart"):
                    del request.session["cart"]
                context = {"username":username,'payment_id':razorpay_payment_id,'order_id':razorpay_order_id,'signature':razorpay_signature,'email':email,'amount':amount}
                return render(request,"success.html",context)
            else:
                return HttpResponseRedirect("login")
        else:
            messages.error(request, "Only Post request is allowed!")
            return HttpResponseRedirect("404")

    @csrf_exempt
    def failure(self,request):
        if request.method == "POST":
            if request.session.get("user_id") is not None:
                amount = float(request.POST.get("amount")) / 10
                cart_ids = request.session.get("cart", [])
                cart_count = len(cart_ids)
                username = request.session["username"]
                context = {"username":username,"cart_count":cart_count,'amount':amount} 
                return render(request,"failure.html",context)
            else:
                return HttpResponseRedirect("login")
        else:
            messages.error(request, "Only Post request is allowed!")
            return HttpResponseRedirect("404")

    def contact(self,request):
        cart_ids = request.session.get("cart", [])
        cart_count = len(cart_ids)
        username = request.session.get("username", None)
        context = {"username":username,"cart_count":cart_count}
        return render(request,"contact.html",context)

    def profile(self,request):
        if request.session.get("user_id") is not None:
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            user_id = request.session["user_id"]
            username = request.session.get("username", None)
            try:
                clientInfo = Users.objects.get(id = user_id)
                request.session["username"] = username
                request.session["user_id"] = clientInfo.id
                context = {"username":username,"cart_count":cart_count,"client":clientInfo}
                return render(request,"profile.html",context)
            except Users.DoesNotExist:
                messages.error(request, "Wrong credentials!")
                return HttpResponseRedirect("404")
        else:
            return HttpResponseRedirect("login")

    def login(self,request):
        return render(request,"login.html")

    def client_login(self,request):
        if request.method == "POST":
            if request.POST.get("email") != "" and request.POST.get("email") is not None and request.POST.get("password") != "" and request.POST.get("password") is not None:
                email = request.POST["email"]
                password = request.POST["password"]
                try:
                    clientInfo = Users.objects.get(user_email = email, user_password = password)
                    username = clientInfo.user_first_name
                    request.session["username"] = username
                    request.session["user_id"] = clientInfo.id
                    return HttpResponseRedirect("/")
                except Users.DoesNotExist:
                    messages.error(request, "Wrong credentials!")
                    return HttpResponseRedirect("404")
            else:
                messages.error(request, "One or more data is not given.")
                return HttpResponseRedirect("404")
        else:
            messages.error(request, "Only Post request is allowed!")
            return HttpResponseRedirect("404")

    def register(self,request):
        return render(request,"register.html")

    def client_register(self,request):
        if request.method == "POST":
            if request.POST.get("firstName") != "" and request.POST.get("firstName") is not None and request.POST.get("lastName") != "" and request.POST.get("lastName") is not None and request.POST.get("email") != "" and request.POST.get("email") is not None and request.POST.get("phone") != "" and request.POST.get("phone") is not None and request.POST.get("password") != "" and request.POST.get("password") is not None and request.POST.get("dateOfBirth") != "" and request.POST.get("dateOfBirth") is not None:
                firstName = request.POST["firstName"]
                lastName = request.POST["lastName"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                password = request.POST["password"]
                dateOfBirth = request.POST["dateOfBirth"]
                createUser = Users.objects.create(
                    user_first_name = firstName,
                    user_last_name = lastName,
                    user_email = email,
                    user_phone_number = phone,
                    user_password = password,
                    user_date_of_birth = dateOfBirth,
                )
                send_mail(
                    "Point Blank",
                    "Dear " + firstName + ",\n\n"
                    "Thank you for registering with Point Blank. We’re pleased to welcome you to our community of responsible and informed firearms enthusiasts."
                    "Your account has been successfully created, and you can now access our platform to explore products, submit enquiries, and stay informed about updates and services we offer. Our team is committed to maintaining the highest standards of safety, transparency, and legal compliance across every interaction.\n\n"
                    "At Point Blank, we take our responsibilities seriously. All activities on our platform are conducted strictly in accordance with applicable laws and regulatory requirements. Should any verification or additional information be required, our support team will contact you directly.\n\n"
                    "If you have any questions or need assistance at any point, please don’t hesitate to reach out—we’re here to help.\n\n"
                    "Warm regards,\n"
                    "Mr. Nachiket Bankar\n"
                    "Point Blank\n",
                    'setting.EMAIL_HOST_USER',
                    [email],
                    fail_silently=False,
                )
                if createUser:
                    return HttpResponseRedirect("login")
                else:
                    messages.error(request, "Something went wrong!")
                    return HttpResponseRedirect("404")
            else:
                messages.error(request, "One or more data is not given.")
                return HttpResponseRedirect("404")
        else:
            messages.error(request, "Only Post request is allowed!")
            return HttpResponseRedirect("404")

    def logout(self,request):
        del request.session["username"]
        del request.session["user_id"]
        if request.session.get("cart"):
            del request.session["cart"]
        return HttpResponseRedirect("login")

    def error_404(self,request):
        return render(request,"404.html")

    def delete_account(self,request):
        if request.session.get("user_id") is not None:
            user_id = request.session["user_id"]
            try:
                clientInfo = Users.objects.get(id = user_id)
                send_mail(
                    "Point Blank",
                    "Dear " + clientInfo.user_first_name + ",\n\n"
                    "This email is to confirm that a request to delete your account associated with our legal firearm services platform has been successfully submitted."
                    "In accordance with our data retention and compliance policies, your account is scheduled for permanent deletion 30 days from the date of this notice. If you did not intend to delete your account or wish to cancel this request, you may do so by logging in to your account within the next 30 days. Logging in during this period will automatically cancel the deletion process.\n If no action is taken within the 30-day period, the deletion will proceed as scheduled and will be permanent. Once completed, your account data cannot be recovered.If you have any questions or believe this request was made in error, please contact our support team before the deletion period ends.\n\n"
                    "Thank you,\n"
                    "Mr. Nachiket Bankar\n"
                    "Point Blank\n",
                    'setting.EMAIL_HOST_USER',
                    [clientInfo.user_email],
                    fail_silently=False,
                )
                del request.session["username"]
                del request.session["user_id"]
                if request.session.get("cart"):
                    del request.session["cart"]
                clientInfo.delete()
                return HttpResponseRedirect("/")
            except Users.DoesNotExist:
                return HttpResponseRedirect("404")
        else:
            return HttpResponseRedirect("login")

    def contact_info(self,request):
        if request.method == "POST":
            if request.POST.get("contact_name") != "" and request.POST.get("contact_name") is not None and request.POST.get("contact_email") != "" and request.POST.get("contact_email") is not None and request.POST.get("contact_subject") != "" and request.POST.get("contact_subject") is not None and request.POST.get("contact_message") != "" and request.POST.get("contact_message") is not None:
                contact_name = request.POST["contact_name"]
                contact_email = request.POST["contact_email"]
                contact_phone = request.POST["contact_phone"]
                contact_subject = request.POST["contact_subject"]
                contact_message = request.POST["contact_message"]
                createClient = Clients.objects.create(
                    client_name = contact_name,
                    client_email = contact_email,
                    client_phone_number = contact_phone,
                    client_subject = contact_subject,
                    client_message = contact_message,
                )
                send_mail(
                    "Point Blank",
                    "Dear " + contact_name + ",\n\n"
                    "Thank you for contacting us. We confirm that your request has been successfully registered for the firearm entitled as " + contact_subject + ". An assigned support representative will contact you within 2–4 business days. In parallel, the required background verification will be initiated and handled strictly in accordance with all applicable laws and regulatory requirements.\n\n"
                    "We appreciate your patience and cooperation as we proceed to ensure a through and compliant review. Should we require any additional information, our team will reach out to you directly. If you have any general questions in the meantime, please do not hesitate to contact us.\n\n"
                    "Mr. Nachiket Bankar\n"
                    "Point Blank\n",
                    'setting.EMAIL_HOST_USER',
                    [contact_email],
                    fail_silently=False,
                )
                if createClient:
                    return HttpResponseRedirect("contact")
                else:
                    messages.error(request, "Something went wrong!")
                    return HttpResponseRedirect("404")
            else:
                messages.error(request, "One or more data is not given")
                return HttpResponseRedirect("404")
        else:
            messages.error(request, "Only Post request is allowed!")
            return HttpResponseRedirect("404")

    def add_to_cart(self,request):
        if request.session.get("user_id") is not None:
            if request.GET.get("id") != "" and request.GET.get("id") is not None:
                firearm_id = int(request.GET.get("id"))
                cart = request.session.get("cart", [])
                if firearm_id not in cart:
                    cart.append(firearm_id)

                request.session["cart"] = cart
                request.session.modified = True
                return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
            else:                
                messages.error(request, "One or more data is not given.")
                return HttpResponseRedirect("404")
        else:
            return HttpResponseRedirect("login")

    def cart(self, request):
        if request.session.get("user_id") is not None:
            username = request.session.get("username")
            cart_ids = request.session.get("cart", [])
            cart_count = len(cart_ids)
            try:
                firearms = Firearms.objects.filter(id__in=cart_ids)
                firearms_transfer_fee = 7500
                firearms_shipping = 5000
                sub_total = 0
                total = 0
                cart = []
                for firearm in firearms:
                    cart.append({
                        "id": firearm.id,
                        "firearms_name": firearm.firearms_name,
                        "firearms_caliber": firearm.firearms_caliber,
                        "firearms_image": firearm.firearms_image,
                        "firearms_price": firearm.firearms_price,
                        "firearms_total_price": firearm.firearms_price,
                    })
                    sub_total = sub_total + firearm.firearms_price
                    total = sub_total + firearms_transfer_fee + firearms_shipping
                context = {"username":username,"cart":cart,"cart_count":cart_count,"firearms_transfer_fee":firearms_transfer_fee,"firearms_shipping":firearms_shipping,"sub_total":sub_total,"total":total}
                return render(request,"cart.html",context)
            except Firearms.DoesNotExist:
                context = {"username":username,"cart":[],"cart_count":cart_count}
                return render(request,"cart.html",context)
        else:
            return HttpResponseRedirect("login")

    def remove_from_cart(self, request):
        if request.session.get("user_id") is not None:
            firearm_id = int(request.GET.get("id"))

            cart = request.session.get("cart")

            if firearm_id in cart:
                cart.remove(firearm_id)

            request.session["cart"] = cart
            request.session.modified = True
            return HttpResponseRedirect("cart")
        else:
            return HttpResponseRedirect("login")

    @csrf_exempt 
    def create_order(self,request):
        if request.method == "POST":
            if request.POST.get("firstName") != "" and request.POST.get("firstName") is not None and request.POST.get("lastName") != "" and request.POST.get("lastName") is not None and request.POST.get("email") != "" and request.POST.get("email") is not None and request.POST.get("phone") != "" and request.POST.get("phone") is not None and request.POST.get("fflDealer") != "" and request.POST.get("fflDealer") is not None and request.POST.get("address") != "" and request.POST.get("address") is not None and request.POST.get("city") != "" and request.POST.get("city") is not None and request.POST.get("state") != "" and request.POST.get("state") is not None and request.POST.get("zipCode") != "" and request.POST.get("zipCode") is not None and request.POST.get("payment_btn") != "" and request.POST.get("payment_btn") is not None:
                client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
                firstName = request.POST["firstName"]
                lastName = request.POST["lastName"]
                email = request.POST["email"]
                phone = request.POST["phone"]
                fflDealer = request.POST["fflDealer"]
                address = request.POST["address"]
                city = request.POST["city"]
                state = request.POST["state"]
                zipCode = request.POST["zipCode"]
                createOrder = Orders.objects.create(
                    buyer_first_name = firstName,
                    buyer_last_name = lastName,
                    buyer_email = email,
                    buyer_phone_number = phone,
                    buyer_dealer_name = fflDealer,
                    buyer_street_address = address,
                    buyer_city = city,
                    buyer_state = state,
                    buyer_zip_code = zipCode,
                    buyer_user_id = Users.objects.get(id = request.session["user_id"]),
                )
                send_mail(
                    "Point Blank",
                    "Dear " + firstName + ",\n\n"
                    "Thank you for choosing Point Blank. We sincerely appreciate your recent purchase and the trust you have placed in us.\n\n"
                    "Your order has been processed in full compliance with all applicable laws and regulations. Should you have any questions regarding documentation, records, or next steps related to your purchase, please do not hesitate to contact us.\n\n"
                    "We value your business and appreciate the opportunity to serve you.\n\n"
                    "Kind regards,\n" +
                    fflDealer,
                    'setting.EMAIL_HOST_USER',
                    [email],
                    fail_silently=False,
                )
                if createOrder:
                    username = request.session.get("username")
                    order_amount = int(float(request.POST.get("payment_btn"))) * 10 #Should be multiplied by 100.
                    payment_order = client.order.create(dict(amount=order_amount, currency="INR", payment_capture=1))
                    payment_order_id = payment_order['id']
                    context = {
                        'amount':order_amount,'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,'order_id':payment_order_id,'username':username,'phone':phone,'email':email,
                    }
                    return render(request,'payment.html',context)
                else:                    
                    messages.error(request, "Could not connect to Database.")
                    return HttpResponseRedirect("404")
            else:
                messages.error(request, "One or more data is not given")
                return HttpResponseRedirect("404")
        else:           
            messages.error(request, "Only POST request is allowed in payment")
            return HttpResponseRedirect("404")
