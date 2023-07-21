from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

from managers.models import Manager, Category, Size, Product
from customers.models import Customer, Order
from managers.forms import Productform, Categoryform, Sizeform


@login_required(login_url='login/')
def index(request):

    orders=Order.objects.all().count()
    products=Product.objects.all().count()
    categories=Category.objects.all().count()
    customers=Customer.objects.all().count()

    context = {
        'title' : "maniverse Home",
        'orders' : orders,
        'products' : products,
        'categories' : categories,
        'customers' : customers,
    }
    return render(request, 'manager/index.html', context=context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_manager:
                auth_login(request, user)

                return HttpResponseRedirect(reverse("managers:index"))
            else:
                context = {
                    'title' : 'Manager Login',
                    'error' : True,
                    'message' : 'Invalid credinals or not allowed user'
                }
                return render(request, 'manager/login.html', context)
        else:
            context ={
                'title' : 'Manager Login',
                'error' : True,
                'message' : 'Invalid credinals or not allowed user'
            }
            return render(request, 'manager/login.html', context)
    else:
        context = {
            'title' : 'Manager Login'
        }
        return render(request, 'manager/login.html', context)
    
@login_required(login_url='login/')
def logout(request):
    auth_logout(request)
   

    return HttpResponseRedirect(reverse("managers:login"))
    

###########################################################################
#####################  CATEGORY  ##########################################
###########################################################################

@login_required(login_url='login/')
def category(request):
    instances=Category.objects.all()
    context = {
        'title' : "maniverse Categories",
        'instances' : instances,

    }
    return render(request, 'manager/categories.html', context=context)



@login_required(login_url='login/')
def category_add(request):
    if request.method == 'POST':
        form = Categoryform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("managers:category"))

        else:
             form = Categoryform()
             context = {
            'title' : 'maniverse Add Categories',
            'error' : True,
            'message' : 'Something went wrong',
            'form' : form,
        

        }
        return render(request, 'manager/add-category.html', context=context)
    else:
        form = Categoryform()
        context = {
            'title' : 'maniverse Add Categories',
            'form' : form,
        

    }
    return render(request, 'manager/add-category.html', context=context)



@login_required(login_url='login/')
def category_edit(request, id):
    pass




@login_required(login_url='login/')
def category_delete(request, id):
    category=Category.objects.get(id=id)
    category.delete()

    return HttpResponseRedirect(reverse("managers:category"))



###########################################################################
#####################  SIZE  #############################################
###########################################################################

@login_required(login_url='login/')
def size(request):
    instances=Size.objects.all()
    context = {
        'title' : "maniverse Size",
        'instances' : instances,

    }
    return render(request, 'manager/sizes.html', context=context)

@login_required(login_url='login/')
def size_add(request):
    pass

@login_required(login_url='login/')
def size_edit(request, id):
    pass


@login_required(login_url='login/')
def size_delete(request, id):
        size=Size.objects.get(id=id)
        size.delete()

        return HttpResponseRedirect(reverse("managers:size"))


###########################################################################
#####################  PRODUCT  ###########################################
###########################################################################

@login_required(login_url='login/')
def products(request):
    instances=Product.objects.all()
    context = {
        'title' : "maniverse Product",
        'instances' : instances,

    }
    return render(request, 'manager/products.html', context=context)

@login_required(login_url='login/')
def products_add(request):
    pass

@login_required(login_url='login/')
def products_edit(request, id):
    pass


@login_required(login_url='login/')
def products_delete(request, id):
        product=Product.objects.get(id=id)
        product.delete()

        return HttpResponseRedirect(reverse("managers:product"))

@login_required(login_url='login/')
def products_stock(request, id):
        product=Product.objects.get(id=id)
        product.is_stock=True
        product.save()

        return HttpResponseRedirect(reverse("managers:size"))

@login_required(login_url='login/')
def products_out(request, id):
        product=Product.objects.get(id=id)
        product.is_stock=False
        product.save()

        return HttpResponseRedirect(reverse("managers:size"))


###########################################################################
#####################  CUSTOMER AND ORDERS  ###############################
###########################################################################


@login_required(login_url='login/')
def customers(request):
    instances=Customer.objects.all()
    context = {
        'title' : "maniverse Customer",
        'instances' : instances,

    }
    return render(request, 'manager/customers.html', context=context)


@login_required(login_url='login/')
def orders(request):
    instances=Order.objects.all()
    context = {
        'title' : "maniverse Order",
        'instances' : instances,

    }
    return render(request, 'manager/orders.html', context=context)


@login_required(login_url='login/')
def orders_packed(request, id):
    pass



@login_required(login_url='login/')
def orders_shipped(request, id):
    pass



@login_required(login_url='login/')
def orders_delivered(request, id):
    pass