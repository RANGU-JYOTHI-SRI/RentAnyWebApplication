from django.shortcuts import render

from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm,UserLoginForm,AddItemForm,AddCartForm,CartAddProductForm,OrderCreateForm
from .models import UserRegistration,additem,cartpage1,OrderItem
from django.db.models import Q
from .cart import Cart
#from .cart.forms import CartAddProductForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage


from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
"""def logout(request):
    try:
        print(request.session['uname'])
        del request.session['uname']
    except KeyError:
        pass
    return render(request,"home.html")"""

"""def logout(request):
    try:
        print(request.session['uname'])
        del request.session['uname']
        print(request.session['uname'])
        return render(request,'home.html')
    except KeyError:
        pass
    return render(request,'home.html')"""

"""def logout(request):
    request.session.pop('uname',None)
    return render(request,'home.html')"""
def logout(request):
    if "uname" in request.session.keys():
        del request.session["uname"]
    return render(request,'home.html')

def addproductfunction(request):
    #return HttpResponse("Main Home")
    context = {}
    context['form'] = AddItemForm()
    return render(request,"add_product.html",context)
"""def userregister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/userlogin1')
            except:
                HttpResponse("registerInvalid")
    else:
        form = RegisterForm()
    return render(request,'login.html',{'form':form})"""

def userregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            uname = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('email.html')
            d = { 'name': name }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', uname
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return render(request,'login.html',{'form':form})
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})


"""def userregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            #return HttpResponse('Please confirm your email address to complete the registration.')
            return render(request, 'acc_active_sent.html')
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserRegistration.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserRegistration.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
"""
def show(request):
    employees = UserRegistration.objects.all()
    return render(request,"show.html",{'employees':employees})
def cart(request):
    uname = request.session["uname"]
    return render(request, "cart.html", {'uname': uname})

def checkout(request):
    uname = request.session["uname"]
    return render(request, "checkout.html", {'uname': uname})

def checklogin(request):
    if request.method == "POST":
        uname = request.POST["email"]
        pwd = request.POST["password"]
        #flag = uname == UserRegistration.objects.filter(email=uname) and pwd == UserRegistration.objects.filter(password=pwd)

        flag1 = uname == 'admin@gmail.com' and pwd == 'admin'
        if flag1:
            request.session['uname'] = uname
            return render(request, "adminhome.html",{'uname':uname})
        else:

            flag = UserRegistration.objects.filter(Q(email__iexact=uname) & Q(password__iexact=pwd))
            if flag:
            #return HttpResponse("Login Valid")

                request.session['uname'] = uname
                if 'uname' in request.session:
                    #print(request.session['uname']+'hi')
                    return render(request, "userhome.html",{'uname': request.session['uname']})

                else:
                    return HttpResponse("Login Invalid")
            return HttpResponse("Login Invalid")
    else:
        return render(request,"login.html")

def adminhome(request):

    # return HttpResponse("Student Login")
    return render(request, "adminhome.html")
def userlogin1(request):

        # return HttpResponse("Student Login")
    return render(request, "login.html")


def userhome(request):
    uname = request.session["uname"]
    #return HttpResponse("Main Home")
    return render(request,"userhome.html",{'uname':uname})

def about(request):
    uname = request.session["uname"]
    #return HttpResponse("Main Home")
    return render(request,"about.html",{'uname':uname})

def contact(request):
    uname = request.session["uname"]
    #return HttpResponse("Main Home")
    return render(request,"contact.html",{'uname':uname})

def about1(request):

    #return HttpResponse("Main Home")
    return render(request,"about1.html")

def contact1(request):
    uname = request.session["uname"]
    #return HttpResponse("Main Home")
    return render(request,"contact1.html")

def adminhome(request):

    #return HttpResponse("Main Home")
    return render(request,"adminhome.html")

"""def additems(request):
    uname = request.session["uname"]
    if request.method=="POST":
        form = AddItemForm(request.POST,request.FILES)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.save()
            
            return HttpResponse("product added sucessfully")
            #return render(request,'addproduct.html')
    else:
        form = AddItemForm()
    return render(request,'add_product.html',{'uname':uname})"""


def additems(request):
    uname = request.session["uname"]
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for user in UserRegistration.objects.all():
                htmly = get_template('newproductemail.html')
                uname1=user.email
                itemname = form.cleaned_data.get('itemname')
                attachment = form.cleaned_data.get('attachment')
                d = {'uname1': uname1,'itemname':itemname,'attachment':attachment.read()}
                subject, from_email, to = 'New Products Alert', 'your_email@gmail.com', uname1
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")

                msg.send()
                messages.success(request, f'New products are added ! Please check them out in RentAnt !!',
                                 {'uname1': uname1})

            return HttpResponse("product added sucessfully")
            # return render(request,'addproduct.html')
    else:
        form = AddItemForm()
    return render(request, 'add_product.html', {'uname': uname})


def viewproducts(request):
    uname = request.session["uname"]
    files=additem.objects.all() # select * from file_table
    count=additem.objects.all().count() # select count(*) from file_table
    #return HttpResponse(file,"Items are there")

    return render(request,'view_products.html',{'files':files,'count':count,'uname':uname})

def deleteproduct(request,itemname):
    uname = request.session["uname"]
    additem.objects.filter(itemname=itemname).delete()
    return redirect('viewproducts')

def edit(request, itemname):

    itemname = additem.objects.get(itemname=itemname)
    return render(request,'update_product.html', {'itemname':itemname})

def update(request,itemname):
    uname = request.session["uname"]
    itemname = additem.objects.get(itemname=itemname)
    if request.method == "POST":
        itemname = request.POST["itemname"]
        price = request.POST["price"]
        file_category = request.POST["file_category"]
        quantity = request.POST["quantity"]
        description = request.POST["description"]
        attachment=request.POST["attachment"]
        additem.objects.filter(itemname=itemname).update(itemname=itemname,price=price,file_category=file_category,quantity=quantity,description=description)
        return redirect("viewproducts")
    else:
        return redirect("viewproducts")
def viewcustomers(request):
    uname = request.session["uname"]
    files=UserRegistration.objects.all() # select * from file_table
    count=UserRegistration.objects.all().count() # select count(*) from file_table
    #return HttpResponse(file,"Items are there")

    return render(request,'viewcustomers.html',{'files':files,'count':count,'uname':uname})

def home(request):
    return render(request,'home.html')






def furnitureinsert1(request):
    #uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(37,42))
    file2 = additem.objects.filter(id__range=(25,30))
    file3 = additem.objects.filter(id__range=(31,36))

    #cart_product_form = CartAddProductForm()

    return render(request,'furniture1.html',{'files1':file1,'files2':file2,'files3':file3})


def furnitureinsert(request):
    uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(37,42))
    file2 = additem.objects.filter(id__range=(25,30))
    file3 = additem.objects.filter(id__range=(31,36))

    cart_product_form = CartAddProductForm()

    return render(request,'furniture.html',{'files1':file1,'files2':file2,'files3':file3,'cart_product_form': cart_product_form,'uname':uname})
def booksinsert1(request):
    #uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(7,12))
    file2 = additem.objects.filter(id__range=(13,19))
    file3 = additem.objects.filter(id__range=(20,24))
    #cart_product_form = CartAddProductForm()

    return render(request,'books1.html',{'files1':file1,'files2':file2,'files3':file3})

def booksinsert(request):
    uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(7,12))
    file2 = additem.objects.filter(id__range=(13,19))
    file3 = additem.objects.filter(id__range=(20,24))
    cart_product_form = CartAddProductForm()

    return render(request,'books.html',{'files1':file1,'files2':file2,'files3':file3,'cart_product_form': cart_product_form,'uname':uname})

def electronicsinsert1(request):
    #uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(49,54))
    file2 = additem.objects.filter(id__range=(43,48))
    #cart_product_form = CartAddProductForm()

    return render(request,'electronics1.html',{'files1':file1,'files2':file2})

def electronicsinsert(request):
    uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(49,54))
    file2 = additem.objects.filter(id__range=(43,48))
    cart_product_form = CartAddProductForm()

    return render(request,'electronics.html',{'files1':file1,'files2':file2,'cart_product_form': cart_product_form,'uname':uname})


def shopdetailfurniture(request):
    uname = request.session["uname"]
    file1 = additem.objects.filter(id__range=(37,42))

    cart_product_form = CartAddProductForm()

    return render(request,'shopdetail.html',{'files1':file1,'cart_product_form': cart_product_form,'uname':uname})

"""
@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = cartpage.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = cartpage.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = cartpage.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = cartpage.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'cart_detail.html')

"""








@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object
    product= get_object_or_404(additem, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    #return HttpResponse("added")
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(additem, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart.html', {'cart': cart})

"""def checkout(request):

    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            #name=form.cleaned_data.get('first_name')
            #uname = form.cleaned_data.get('email')
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                htmly = get_template('orderemail.html')
                d = {'name': name}
                subject, from_email, to = 'Order Placement', 'your_email@gmail.com', uname
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.success(request, f'Your order is placed sucessfully ! You are order will deliver soon')
            cart.clear()

        return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'form': form})
    

"""
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            name=form.cleaned_data.get('first_name')
            uname = form.cleaned_data.get('email')
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                htmly = get_template('orderemail.html')
                d = {'uname': name}

                subject, from_email, to = 'Order Placement', 'your_email@gmail.com', uname
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                messages.success(request, f'Your order is placed sucessfully ! You are order will deliver soon',{'uname': uname})
            cart.clear()
        return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'form': form})

def created(request):
    return render(request, 'created.html')


def placeorder(request):

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')
            uname = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('orderemail.html')
            d = { 'name': name }
            subject, from_email, to = 'Order Placement', 'your_email@gmail.com', uname
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your order is placed sucessfully ! You are order will deliver soon')
            return render(request,'login.html',{'form':form})
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})


def updatepassword(request,uname):
    #uname = request.session["uname"]
    uname = UserRegistration.objects.get(email=uname)
    if request.method == "POST":
        password = request.POST["password"]
        UserRegistration.objects.filter(uname=uname).update(password=password)
        return redirect("/userregister")
    else:
        return redirect("/updatepassword")
def editpassword(request, uname):

    uname = UserRegistration.objects.get(email=uname)
    return render(request,'update_password.html', {'uname':uname})