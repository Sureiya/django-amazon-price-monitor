from django.conf.urls import patterns, url

from price_monitor.views import ProductListAndCreateView, ProductCRUDView

urlpatterns = patterns(
    '',
    url(r'^page/(?P<page>\d+)/$', ProductListAndCreateView.as_view(), name='monitor_view'),
    url(r'^$', ProductListAndCreateView.as_view(), name='monitor_view'),
    url(r'^subscription/delete/(?P<public_id>[a-z0-9\-]{36})/$', 'price_monitor.views.delete_subscription_view', name='delete_subscription_view'),
    # url(r'^api/', include('price_monitor.api.urls')),
    url(r'^charts-demo/$', 'price_monitor.views.charts_demo_view', name='charts_demo_view'),
    url(r'^product-crud/$', ProductCRUDView.as_view()),
)
