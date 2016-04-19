from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import hashlib
from django.conf import settings
from .util import generate_hash
import models
import requests
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# from recharge_panel.config import logging
import traceback
# Create your views here.

# script_log = logging('recharge_panel')

def index(request):
    request.session.set_expiry(3600)
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html',"aUrl":"/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })
    request.session['role'] = 'user'
    template = loader.get_template('commons/index.html')
    return HttpResponse(template.render(context_data))


@csrf_exempt
def login(request):

    format = "%a %b %d %H:%M:%S %Y"
    today = datetime.datetime.now()
    login_date = today.strftime(format)
    try:
        if request.method == 'POST':
                # script_log.debug("Post Request "+str(request.get_host()))
                # script_log.debug("Post Request for User "+request.POST['username'])
                username = request.POST['username']
                password = request.POST['password']
                request.session.set_expiry(2000)
                if username == 'admin' and password == 'admin' :
                        #cache.set('get_data',None)
                        request.session['username']= username
                        request.session['last_login'] =  login_date
                        main_data = [] #get_data.data({'query':'summary_data'},script_log)
                        #request.session['detail_data'] = main_data
                        context_data = {'modal_url':'/view_details/','main_content':'summary.html','key':'summary'}
                        context = RequestContext(request,context_data)
                        template = loader.get_template("commons/index.html")

                        return HttpResponse(template.render(context))
                else:

                    request.session.flush()
                    return render(request,'commons/login.html',context={'error':"true"})
        else:

            if (request.session.__contains__('username')):
                    request.session.set_expiry(2000)

                    main_data = [] #get_data.data({'query':'summary_data'},script_log)

                    context_data = {'modal_url':'/view_details/','main_content':'summary.html','key':'summary'}

                    context = RequestContext(request,context_data)


                    template = loader.get_template("commons/index.html")
                    return HttpResponse(template.render(context))

        return render(request,'commons/login.html')
    except Exception as exc:
        print exc
        # script_log.warn("Error "+str(exc.message))
        # script_log.error("Error"+str(traceback.format_exc()))
        return render(request,'commons/login.html')

def logout(request):

    request.session.flush()
    return render(request,'commons/login.html')

def view_plan(request):
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html',"aUrl":"/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })
    template = loader.get_template('commons/single.html')
    return HttpResponse(template.render(context_data))


def initiate_recharge(request):
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html', "aUrl": "/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })


    if (request.session.__contains__('username')) and request.method == 'POST':
        request.session['role'] = 'user'

        post_url = "http://localhost:8003/api/user_recharge"
        post_params = {
                       "username":request.POST.get('username'),
                       "user_id":request.POST.get('user_id'),
                       "mobile_number":request.POST.get('mobile_number'),
                       "operator_code":request.POST.get('operator_code'),
                       "circle":request.POST.get('circle'),
                       "amount":request.POST.get('amount')
                       }
        print post_params
        response = requests.post(post_url,json=post_params)
        context_data.update({'recharge_status': response.text()})
        template = loader.get_template('commons/index.html')
    else:
        template = loader.get_template('commons/login.html')
    return HttpResponse(template.render(context_data))




def payments(request):
    context_data = RequestContext(request,
                                  {'body_template': 'campaign/create_campaign.html',"aUrl":"/recharge_view_plan",
                                   'session_data': request.session, "success": "false", "error": "error",
                                   })
    template = loader.get_template('commons/payment.html')
    return HttpResponse(template.render(context_data))

@login_required
def buy_order(request):
    """ funtion for save all orders and genarate order id"""
    items = None
    orderitem = None
    extra = False
    if request.user.is_authenticated() and not request.user.is_staff:
        user = Buyer.objects.get(id=request.user.id)
        try:
            cart = Cart.objects.get(buyer=request.user)
        except ObjectDoesNotExist:
            extra = "You dont have any item in your cart"
            variables = RequestContext(request, {'extra': extra})
            return render('home.html', variables)
            total_amount = OrderItem.objects.filter(buyer=request.user)
            item_list = []
            rg = request.POST.get
            if cart:
                if request.POST:
                    if rg('shippingnme')and rg('shippingaddress') and rg('shippingemail') and rg('shippingpostel') and rg('shippingcity') and rg('shippingcountry') and rg('shippingcountry') and rg('shippingphone'):
                        try:
                            """store all products to myorder model and genarate order id for the order"""
                            myorder = MyOrder(buyer=user)
                            # billing User
                            myorder.buyer = user
                            # myorder of Billing  Address
                            myorder.billing_name = request.POST.get('billingname')
                            myorder.billing_street_address = request.POST.get('billingaddress')
                            myorder.billing_pincode = request.POST.get('billingpostel')
                            myorder.billing_city = request.POST.get('billingcity')
                            myorder.billing_country = request.POST.get('billingcountry')
                            myorder.billing_state = request.POST.get('billingstate')
                            myorder.billing_mobile = request.POST.get('billingphone')
                            myorder.billing_email = request.POST.get('billingemail')
                            # myorder of shipping Address
                            myorder.shipping_pincode = request.POST.get('shippingpostel')
                            myorder.shipping_name = request.POST.get('shippingnme')
                            myorder.shipping_street_address = request.POST.get('shippingaddress')
                            myorder.shipping_city = request.POST.get('shippingcity')
                            myorder.shipping_state = request.POST.get('shippingstate')
                            myorder.shipping_mobile = request.POST.get('shippingphone')
                            myorder.shipping_country = request.POST.get('shippingcountry')
                            myorder.shipping_email = request.POST.get('shippingemail')
                            if request.POST.get('paymentmethod'):
                                myorder.payment_method = request.POST.get('paymentmethod')
                            else:
                                myorder.payment_method = 'ON'
                            myorder.comment =  request.POST.get('prodcutmessage')

                            print "my messages "
                            print myorder.comment

                          # payment_method
                          # comment
                            myorder.txnid = str(uuid.uuid1().int >> 64)
                            myorder.save()
                            """genarate an oredr id, the below loop will add all orderd product to the                                               order"""

                            for order in cart.items.all():
                                orderitem = OrderItem()
                                orderitem.buyer = order.buyer
                                orderitem.product_id = order.product.id
                                orderitem.product_title = order.product.name
                                orderitem.weight = order.product.weight
                                orderitem.product_price = order.product.gross_pay()[0]
                                orderitem.total_amount = order.total
                                orderitem.quantity = order.quantity
                                orderitem.save()
                                myorder.items.add(orderitem)
                            total_details = total_price_fu(myorder)

                            """ After adding products to order assigning a
                            transaction amount and shipping charge to the order"""
                            myorder = MyOrder.objects.get(pk=myorder.txnid)

                            myorder.amount = total_details['grand_total']
                            myorder.shipping_rate = total_details['shipping_rate']

                            """Assigning all values for hash funtion for payu"""

                            cleaned_data = {'key': settings.PAYU_INFO['merchant_key'],'txnid':myorder.txnid, 'amount': myorder.amount, 'productinfo':orderitem.product_title,'firstname': myorder.billing_name, 'email':myorder.billing_email,'udf1': '', 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '','udf7': '',  'udf8': '', 'udf9': '', 'udf10': ''}
                            """ the generate_hash funtion is use for genarating hash
                             value from cleaned_data"""
                            hash_o = generate_hash(cleaned_data)
                            myorder.hash =hash_o
                            myorder.save()

                            return HttpResponse(
                             """
                                  <html>
                                      <head><title>Redirecting...</title></head>
                                      <body>
                                      <form action='%s' method='post' name="payu">
                                          <input type="hidden" name="firstname" value="%s" />
                                          <input type="hidden" name="surl" value="%s" />
                                          <input type="hidden" name="phone" value="%s" />
                                          <input type="hidden" name="key" value="%s" />
                                          <input type="hidden" name="hash" value =
                                          "%s" />
                                          <input type="hidden" name="curl" value="%s" />
                                          <input type="hidden" name="furl" value="%s" />
                                          <input type="hidden" name="txnid" value="%s" />
                                          <input type="hidden" name="productinfo" value="%s" />
                                          <input type="hidden" name="amount" value="%s" />
                                          <input type="hidden" name="email" value="%s" />
                                          <input type="hidden" value="submit">
                                      </form>
                                      </body>
                                      <script language='javascript'>
                                      window.onload = function(){
                                       document.forms['payu'].submit()
                                      }
                                      </script>
                                  </html>

                              """ % (settings.PAYU_INFO['payment_url'],
                                   myorder.billing_name, settings.PAYU_INFO['surl'],
                                   myorder.billing_mobile,
                                   settings.PAYU_INFO['merchant_key'],
                                   hash_o,
                                   settings.PAYU_INFO['curl'],
                                   settings.PAYU_INFO['furl'],
                                   myorder.txnid,
                                   orderitem.product_title,
                                   myorder.amount,
                                   myorder.billing_email
                                   )
                            )
                        except Exception as Err:
                            return HttpResponse('Internal Server Error')