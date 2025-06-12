from django.urls import path, include
from .views import *

urlpatterns = [
    path('info/', info_view, name='info_view'),
    path('', info_view),

    path('corals/', CoralsListView.as_view(), name='corals_list'),
    path('corals/<int:pk>/', CoralsDetailView.as_view(), name='corals_detail'),
    path('corals/create/', CoralsCreateView.as_view(), name='corals_create'),
    path('corals/<int:pk>/update/',
         CoralsUpdateView.as_view(), name='corals_update'),
    path('corals/<int:pk>/delete/',
         CoralsDeleteView.as_view(), name='corals_delete'),

    path('accounts/', AccountsListView.as_view(), name='accounts_list'),
    path('accounts/<int:pk>/', AccountsDetailView.as_view(), name='accounts_detail'),
    path('accounts/create/', AccountsCreateView.as_view(), name='accounts_create'),
    path('accounts/<int:pk>/update/',
         AccountsUpdateView.as_view(), name='accounts_update'),
    path('accounts/<int:pk>/delete/',
         AccountsDeleteView.as_view(), name='accounts_delete'),

    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UsersDetailView.as_view(), name='users_detail'),
    path('users/create/', UsersCreateView.as_view(), name='users_create'),
    path('users/<int:pk>/update/', UsersUpdateView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UsersDeleteView.as_view(), name='users_delete'),

    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrdersDetailView.as_view(), name='orders_detail'),
    path('orders/create/', OrdersCreateView.as_view(), name='orders_create'),
    path('orders/<int:pk>/update/',
         OrdersUpdateView.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete/',
         OrdersDeleteView.as_view(), name='orders_delete'),

    path('certificates/', CertificatesListView.as_view(), name='certificates_list'),
    path('certificates/<int:pk>/', CertificatesDetailView.as_view(),
         name='certificates_detail'),
    path('certificates/create/', CertificatesCreateView.as_view(),
         name='certificates_create'),
    path('certificates/<int:pk>/update/',
         CertificatesUpdateView.as_view(), name='certificates_update'),
    path('certificates/<int:pk>/delete/',
         CertificatesDeleteView.as_view(), name='certificates_delete'),

    path('reviews/', ReviewsListView.as_view(), name='reviews_list'),
    path('reviews/<int:pk>/', ReviewsDetailView.as_view(), name='reviews_detail'),
    path('reviews/create/', ReviewsCreateView.as_view(), name='reviews_create'),
    path('reviews/<int:pk>/update/',
         ReviewsUpdateView.as_view(), name='reviews_update'),
    path('reviews/<int:pk>/delete/',
         ReviewsDeleteView.as_view(), name='reviews_delete'),
]
