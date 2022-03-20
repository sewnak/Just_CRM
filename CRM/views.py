from django.db.models import ProtectedError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse
from django.views import View, generic
from CRM.models import Customer, Offer, Contract, Invest, Apartment
from .forms import CustomUserCreate


class SignupView(generic.CreateView):
    template_name = 'registration/user_signup.html'
    form_class = CustomUserCreate

    def get_success_url(self):
        return reverse('index')


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class CustomerView(View):
    def get(self, request):
        c = Customer.objects.all()
        return render(request, 'customers.html', {'customers': c})


class DeleteCustomerView(LoginRequiredMixin, View):
    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        try:
            customer.delete()
        except ProtectedError:
            return HttpResponse('nie można usunąć klienta z ofertą')
        return redirect("/customers/")


class EditCustomerView(LoginRequiredMixin, View):
    def get(self, request, customer_id):
        c = Customer.objects.get(id=customer_id)
        return render(request, 'edit_customer.html', {'customer': c})

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street = request.POST['street']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        customer.first_name = first_name
        customer.last_name = last_name
        customer.street = street
        customer.city = city
        customer.phone = phone
        customer.email = email
        customer.save()
        return redirect('customers')


class AddCustomer(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_customer.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street = request.POST['street']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        Customer.objects.create(first_name=first_name, last_name=last_name, street=street, city=city, phone=phone, email=email)
        return redirect('/customers/')


class OfferView(View):
    def get(self, request):
        o = Offer.objects.all()
        return render(request, 'offers.html', {'offers': o})


class DeleteOfferView(LoginRequiredMixin, View):
    def get(self, request, offer_id):
        offer = Offer.objects.get(id=offer_id)
        offer.delete()
        return redirect("/offers/")


class AddOffer(LoginRequiredMixin, View):
    def get(self, request):
        clients = Customer.objects.all()
        invests = Invest.objects.all()
        apartments = Apartment.objects.all()
        return render(request, 'add_offer.html', {'clients': clients, 'invests': invests, 'apartments': apartments})

    def post(self, request):
        client_id = request.POST.get('Klient')
        client = Customer.objects.get(pk=client_id)
        invest_id = request.POST.get('Inwestycja')
        invest = Invest.objects.get(pk=invest_id)
        apartment_id = request.POST.get('Apartament')
        apartment = Apartment.objects.get(pk=apartment_id)
        Offer.objects.create(client=client, invest=invest, apartment=apartment)
        return render(request, 'add_apartments.html')


class ContractView(View):
    def get(self, request):
        c = Contract.objects.all()
        return render(request, 'contracts.html', {'contracts': c})


class AddContract(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_contracts.html')


class InvestView(View):
    def get(self, request):
        i = Invest.objects.all()
        return render(request, 'invests.html', {'invests': i})


class AddInvest(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_invests.html')

    def post(self, request):
        name = request.POST['name']
        adress = request.POST['adress']
        nr_of_apartments = request.POST['nr_of_ap']
        www = request.POST['www']
        Invest.objects.create(invest_name=name, adress=adress, no_of_apartments=nr_of_apartments, www=www)
        return render(request, 'add_invests.html')


class ApartmentView(View):
    def get(self, request):
        a = Apartment.objects.all()
        return render(request, 'apartments.html', {'apartments': a})


class AddApartment(LoginRequiredMixin, View):
    def get(self, request):
        invests = Invest.objects.all()
        return render(request, 'add_apartments.html', {'invests': invests})

    def post(self, request):
        nr = request.POST['nr']
        m2 = request.POST['m2']
        invest_id = request.POST.get('Inwestycja')
        invest = Invest.objects.get(pk=invest_id)
        Apartment.objects.create(nr=nr, m2=m2, invest=invest)
        return render(request, 'add_apartments.html')

