from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# imported the productForm we just created

# Create your views here.
def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})
    # created products variable, using objects.all() to get all entries
    # then using render, making request, naming file to make request to, and naming desired variable

def details(request, pk):
    # request is the request issued by user, additional info is pk
    pk = int(pk)
    # converts string value of primary key into integer, pass it into pk variable
    item = get_object_or_404(Product, pk=pk)
    # go check for item in database, if not there give 404 error
    # look at model of Product, use dictionary object pk=pk (key value pair)
    # the pk value will be whichever selection the user selected
    # that will then get stored in item
    form = ProductForm(data=request.POST or None, instance=item)
    # if they give information on form, its sent on POST method
    # try and get information from that post
    # if you can't, return none value
    # if you can, the instance will be that item value
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        # if the request.method is POST, check the form, if it is valid
        # safe form into our database and return to products_page
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})
        # this is actually the initial value that will come up, a page yet to
        # be created that allows you to make changes to selected product
        # once those changes have been made or if request.method == POST
        # comes into play

def delete(request, pk):
    # function passes in request and variable of pk
    pk = int(pk)
    # set variable to integer
    item = get_object_or_404(Product, pk=pk)
    # set item equal to our selected pk from Product
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
        # if the request came from user, delete item and return
        # to admin_console
    context = {'item': item,}
    return render(request, 'products/confirmDelete.html', context)
    # otherwise set context equal to item as a dictionary
    # and upload confirmDelete page

def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
        # if the form is valid, delete entry and return to admin_console
    else:
        return redirect('admin_console')
        # otherwise just return to admin console

def createRecord(request):
    # only paramenter is request object
    form = ProductForm(request.POST or None)
    # open ProductForm and get info from request
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ProductForm()
        # if form is valid save form and return to admin_console
        # otherwise print out errors on the form
        # send back blank form for them to fill out
    context = {
        'form': form,
    }
    return render(request, 'products/createRecord.html', context)

