from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


def info_view(request):
    return render(request, 'info.html')


class CountriesListView(ListView):
    model = Countries
    template_name = 'countries/countries_list.html'
    context_object_name = 'countries'


class CountriesDetailView(DetailView):
    model = Countries
    template_name = 'countries/countries_detail.html'
    context_object_name = 'country'


class CountriesCreateView(CreateView):
    model = Countries
    form_class = CountriesForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list')


class CountriesUpdateView(UpdateView):
    model = Countries
    form_class = CountriesForm
    template_name = 'countries/countries_form.html'
    success_url = reverse_lazy('countries_list')


class CountriesDeleteView(DeleteView):
    model = Countries
    template_name = 'countries/countries_confirm_delete.html'
    success_url = reverse_lazy('countries_list')


class SeasListView(ListView):
    model = Seas
    template_name = 'seas/seas_list.html'
    context_object_name = 'seas'


class SeasDetailView(DetailView):
    model = Seas
    template_name = 'seas/seas_detail.html'
    context_object_name = 'sea'


class SeasCreateView(CreateView):
    model = Seas
    form_class = SeasForm
    template_name = 'seas/seas_form.html'
    success_url = reverse_lazy('seas_list')


class SeasUpdateView(UpdateView):
    model = Seas
    form_class = SeasForm
    template_name = 'seas/seas_form.html'
    success_url = reverse_lazy('seas_list')


class SeasDeleteView(DeleteView):
    model = Seas
    template_name = 'seas/seas_confirm_delete.html'
    success_url = reverse_lazy('seas_list')


class ReefsListView(ListView):
    model = Reefs
    template_name = 'reefs/reefs_list.html'
    context_object_name = 'reefs'


class ReefsDetailView(DetailView):
    model = Reefs
    template_name = 'reefs/reefs_detail.html'
    context_object_name = 'reef'


class ReefsCreateView(CreateView):
    model = Reefs
    form_class = ReefsForm
    template_name = 'reefs/reefs_form.html'
    success_url = reverse_lazy('reefs_list')


class ReefsUpdateView(UpdateView):
    model = Reefs
    form_class = ReefsForm
    template_name = 'reefs/reefs_form.html'
    success_url = reverse_lazy('reefs_list')


class ReefsDeleteView(DeleteView):
    model = Reefs
    template_name = 'reefs/reefs_confirm_delete.html'
    success_url = reverse_lazy('reefs_list')


class CategoriesListView(ListView):
    model = Categories
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'categories/categories_detail.html'
    context_object_name = 'category'


class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list')


class CategoriesUpdateView(UpdateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list')


class CategoriesDeleteView(DeleteView):
    model = Categories
    template_name = 'categories/categories_confirm_delete.html'
    success_url = reverse_lazy('categories_list')


class CoralsListView(ListView):
    model = Corals
    template_name = 'corals/corals_list.html'
    context_object_name = 'corals'


class CoralsDetailView(DetailView):
    model = Corals
    template_name = 'corals/corals_detail.html'
    context_object_name = 'coral'


class CoralsCreateView(CreateView):
    model = Corals
    form_class = CoralsForm
    template_name = 'corals/corals_form.html'
    success_url = reverse_lazy('corals_list')


class CoralsUpdateView(UpdateView):
    model = Corals
    form_class = CoralsForm
    template_name = 'corals/corals_form.html'
    success_url = reverse_lazy('corals_list')


class CoralsDeleteView(DeleteView):
    model = Corals
    template_name = 'corals/corals_confirm_delete.html'
    success_url = reverse_lazy('corals_list')


class OrderStatusesListView(ListView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_list.html'
    context_object_name = 'orderstatuses'


class OrderStatusesDetailView(DetailView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_detail.html'
    context_object_name = 'orderstatus'


class OrderStatusesCreateView(CreateView):
    model = OrderStatuses
    form_class = OrderStatusesForm
    template_name = 'orderstatuses/orderstatuses_form.html'
    success_url = reverse_lazy('orderstatuses_list')


class OrderStatusesUpdateView(UpdateView):
    model = OrderStatuses
    form_class = OrderStatusesForm
    template_name = 'orderstatuses/orderstatuses_form.html'
    success_url = reverse_lazy('orderstatuses_list')


class OrderStatusesDeleteView(DeleteView):
    model = OrderStatuses
    template_name = 'orderstatuses/orderstatuses_confirm_delete.html'
    success_url = reverse_lazy('orderstatuses_list')


class AccountsListView(ListView):
    model = Accounts
    template_name = 'accounts/accounts_list.html'
    context_object_name = 'accounts'


class AccountsDetailView(DetailView):
    model = Accounts
    template_name = 'accounts/accounts_detail.html'
    context_object_name = 'account'


class AccountsCreateView(CreateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'accounts/accounts_form.html'
    success_url = reverse_lazy('accounts_list')


class AccountsUpdateView(UpdateView):
    model = Accounts
    form_class = AccountsForm
    template_name = 'accounts/accounts_form.html'
    success_url = reverse_lazy('accounts_list')


class AccountsDeleteView(DeleteView):
    model = Accounts
    template_name = 'accounts/accounts_confirm_delete.html'
    success_url = reverse_lazy('accounts_list')


class RolesListView(ListView):
    model = Roles
    template_name = 'roles/roles_list.html'
    context_object_name = 'roles'


class RolesDetailView(DetailView):
    model = Roles
    template_name = 'roles/roles_detail.html'
    context_object_name = 'role'


class RolesCreateView(CreateView):
    model = Roles
    form_class = RolesForm
    template_name = 'roles/roles_form.html'
    success_url = reverse_lazy('roles_list')


class RolesUpdateView(UpdateView):
    model = Roles
    form_class = RolesForm
    template_name = 'roles/roles_form.html'
    success_url = reverse_lazy('roles_list')


class RolesDeleteView(DeleteView):
    model = Roles
    template_name = 'roles/roles_confirm_delete.html'
    success_url = reverse_lazy('roles_list')


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UsersDetailView(DetailView):
    model = Users
    template_name = 'users/users_detail.html'
    context_object_name = 'user'


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersForm
    template_name = 'users/users_form.html'
    success_url = reverse_lazy('users_list')


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersForm
    template_name = 'users/users_form.html'
    success_url = reverse_lazy('users_list')


class UsersDeleteView(DeleteView):
    model = Users
    template_name = 'users/users_confirm_delete.html'
    success_url = reverse_lazy('users_list')


class OrdersListView(ListView):
    model = Orders
    template_name = 'orders/orders_list.html'
    context_object_name = 'orders'


class OrdersDetailView(DetailView):
    model = Orders
    template_name = 'orders/orders_detail.html'
    context_object_name = 'order'


class OrdersCreateView(CreateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/orders_form.html'
    success_url = reverse_lazy('orders_list')


class OrdersUpdateView(UpdateView):
    model = Orders
    form_class = OrdersForm
    template_name = 'orders/orders_form.html'
    success_url = reverse_lazy('orders_list')


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'orders/orders_confirm_delete.html'
    success_url = reverse_lazy('orders_list')


class OrderItemsListView(ListView):
    model = OrderItems
    template_name = 'orderitems/orderitems_list.html'
    context_object_name = 'orderitems'


class OrderItemsDetailView(DetailView):
    model = OrderItems
    template_name = 'orderitems/orderitems_detail.html'
    context_object_name = 'orderitem'


class OrderItemsCreateView(CreateView):
    model = OrderItems
    form_class = OrderItemsForm
    template_name = 'orderitems/orderitems_form.html'
    success_url = reverse_lazy('orderitems_list')


class OrderItemsUpdateView(UpdateView):
    model = OrderItems
    form_class = OrderItemsForm
    template_name = 'orderitems/orderitems_form.html'
    success_url = reverse_lazy('orderitems_list')


class OrderItemsDeleteView(DeleteView):
    model = OrderItems
    template_name = 'orderitems/orderitems_confirm_delete.html'
    success_url = reverse_lazy('orderitems_list')


class CertificateStatusesListView(ListView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_list.html'
    context_object_name = 'certificatestatuses'


class CertificateStatusesDetailView(DetailView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_detail.html'
    context_object_name = 'certificatestatus'


class CertificateStatusesCreateView(CreateView):
    model = CertificateStatuses
    form_class = CertificateStatusesForm
    template_name = 'certificatestatuses/certificatestatuses_form.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateStatusesUpdateView(UpdateView):
    model = CertificateStatuses
    form_class = CertificateStatusesForm
    template_name = 'certificatestatuses/certificatestatuses_form.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateStatusesDeleteView(DeleteView):
    model = CertificateStatuses
    template_name = 'certificatestatuses/certificatestatuses_confirm_delete.html'
    success_url = reverse_lazy('certificatestatuses_list')


class CertificateTypesListView(ListView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_list.html'
    context_object_name = 'certificatetypes'


class CertificateTypesDetailView(DetailView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_detail.html'
    context_object_name = 'certificatetype'


class CertificateTypesCreateView(CreateView):
    model = CertificateTypes
    form_class = CertificateTypesForm
    template_name = 'certificatetypes/certificatetypes_form.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificateTypesUpdateView(UpdateView):
    model = CertificateTypes
    form_class = CertificateTypesForm
    template_name = 'certificatetypes/certificatetypes_form.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificateTypesDeleteView(DeleteView):
    model = CertificateTypes
    template_name = 'certificatetypes/certificatetypes_confirm_delete.html'
    success_url = reverse_lazy('certificatetypes_list')


class CertificatesListView(ListView):
    model = Certificates
    template_name = 'certificates/certificates_list.html'
    context_object_name = 'certificates'


class CertificatesDetailView(DetailView):
    model = Certificates
    template_name = 'certificates/certificates_detail.html'
    context_object_name = 'certificate'


class CertificatesCreateView(CreateView):
    model = Certificates
    form_class = CertificatesForm
    template_name = 'certificates/certificates_form.html'
    success_url = reverse_lazy('certificates_list')


class CertificatesUpdateView(UpdateView):
    model = Certificates
    form_class = CertificatesForm
    template_name = 'certificates/certificates_form.html'
    success_url = reverse_lazy('certificates_list')


class CertificatesDeleteView(DeleteView):
    model = Certificates
    template_name = 'certificates/certificates_confirm_delete.html'
    success_url = reverse_lazy('certificates_list')


class ReviewsListView(ListView):
    model = Reviews
    template_name = 'reviews/reviews_list.html'
    context_object_name = 'reviews'


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'reviews/reviews_detail.html'
    context_object_name = 'review'


class ReviewsCreateView(CreateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/reviews_form.html'
    success_url = reverse_lazy('reviews_list')


class ReviewsUpdateView(UpdateView):
    model = Reviews
    form_class = ReviewsForm
    template_name = 'reviews/reviews_form.html'
    success_url = reverse_lazy('reviews_list')


class ReviewsDeleteView(DeleteView):
    model = Reviews
    template_name = 'reviews/reviews_confirm_delete.html'
    success_url = reverse_lazy('reviews_list')

# Account views


def account_list(request):
    accounts = Accounts.objects.all()
    return render(request, 'accounts/account_list.html', {'accounts': accounts})


def account_create(request):
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountsForm()
    return render(request, 'accounts/account_form.html', {'form': form})


def account_update(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    if request.method == 'POST':
        form = AccountsForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountsForm(instance=account)
    return render(request, 'accounts/account_form.html', {'form': form})


def account_delete(request, pk):
    account = get_object_or_404(Accounts, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'accounts/account_confirm_delete.html', {'object': account})


def certificates_list(request):
    certificates = Certificates.objects.all()
    return render(request, 'certificates/certificates_list.html', {'certificates': certificates})


def certificates_create(request):
    if request.method == 'POST':
        form = CertificatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificates_list')
    else:
        form = CertificatesForm()
    return render(request, 'certificates/certificates_form.html', {'form': form})


def certificates_update(request, pk):
    certificate = get_object_or_404(Certificates, pk=pk)
    if request.method == 'POST':
        form = CertificatesForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificates_list')
    else:
        form = CertificatesForm(instance=certificate)
    return render(request, 'certificates/certificates_form.html', {'form': form})


def certificates_delete(request, pk):
    certificate = get_object_or_404(Certificates, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificates_list')
    return render(request, 'certificates/certificates_confirm_delete.html', {'object': certificate})
