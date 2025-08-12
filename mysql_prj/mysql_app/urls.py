from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('userregister/', views.userregister,name="userregister"),
    path('userlogin1/', views.userlogin1),
path("addproductfunction/",views.addproductfunction,name="addproductfunction"),
    path('show/',views.show),

path("cart/", views.cart, name="cart"),
    path("checklogin/", views.checklogin, name="checklogin"),
    path("userhome",views.userhome,name='userhome'),
path("about/",views.about,name='about'),
path("about1/",views.about1,name='about1'),
path("contact/",views.contact,name='contact'),
path("contact1/",views.contact1,name='contact1'),
path("adminhome/",views.adminhome,name="adminhome"),
    path("addproduct",views.additems,name="addproduct"),
path("checkout",views.checkout,name="checkout"),
    path("deleteproduct/<str:itemname>", views.deleteproduct, name="deleteproduct"),
    path('edit/<str:itemname>', views.edit),
    path('update/<str:itemname>', views.update),
    path('editpassword/<str:uname>', views.editpassword),
    path('updatepassword/<str:uname>', views.updatepassword),
    path("viewproducts/", views.viewproducts, name="viewproducts"),
    path("viewcustomers/", views.viewcustomers, name="viewcustomers"),
path("logout/",views.logout,name="logout"),
path("furniture1/",views.furnitureinsert1,name="furniture"),
path("books1/",views.booksinsert1,name="books"),
path("furniture/",views.furnitureinsert,name="furniture"),
path("shopdetail/",views.shopdetailfurniture,name="shopdetail"),
path("books/",views.booksinsert,name="books"),
path("electronics/",views.electronicsinsert,name="electronics"),
path("electronics1/",views.electronicsinsert1,name="electronics1"),
path('cart_detail/', views.cart_detail, name='cart_detail'),
path('cart_add/<int:product_id>', views.cart_add,name='cart_add'),
path('cart_remove/<int:product_id>', views.cart_remove,name='cart_remove'),
path('create/', views.order_create, name='order_create'),
path('created', views.created, name='created'),
#path('checkout/', views.checkout, name='checkout'),
    #url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    #url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

    #path('add/<int:id>/', views.cart_add, name='cart_add'),
    #path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    #path('item_increment/<int:id>/',views.item_increment, name='item_increment'),
   # path('item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    #path('cart_clear/', views.cart_clear, name='cart_clear'),
    #path('cart-detail/',views.cart_detail,name='cart_detail'),

    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)