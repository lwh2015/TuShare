"""TuShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url
from .view.k_data import k_data
from .view.today_all import today_all
from .view.tick_data import tick_data
from .view.realtime_quotes import realtime_quotes,socket_realtime_quotes
from .view.today_ticks import today_ticks
from .view.index_data import index_data
from .view.sina_dd import sina_dd
from .view.profit_data import profit_data
from .view.forecast_data import forecast_data
from .view.xsg_data import xsg_data
from .view.fund_holdings import fund_holdings
from .view.new_stocks import new_stocks
from .view.sh_margins import sh_margins
from .view.sh_margin_details import sh_margin_details
from .view.sz_margins import sz_margins
from .view.sz_margin_details import sz_margin_details
from .view.industry_classified import industry_classified
from .view.concept_classified import concept_classified
from .view.area_classified import area_classified
from .view.sme_classified import sme_classified
from .view.gme_classified import gme_classified
from .view.st_classified import st_classified
from .view.stock_basics import stock_basics
from .views import echo
urlpatterns = [
    # url(r'^admin/',admin.site.urls),
    url(r'^socket_realtime_quotes',socket_realtime_quotes),
    url(r'^echo/(?P<userid>[0-9]+)$',echo),
    url(r'^k_data', k_data),
    url(r'^today_all', today_all),
    url(r'^tick_data',tick_data),
    url(r'^realtime_quotes',realtime_quotes),
    url(r'^today_ticks', today_ticks),
    url(r'^index_data', index_data),
    url(r'^sina_dd', sina_dd),
    url(r'^profit_data', profit_data),
    url(r'^forecast_data', forecast_data),
    url(r'^xsg_data', xsg_data),
    url(r'^fund_holdings', fund_holdings),
    url(r'^new_stocks', new_stocks),
    url(r'^sh_margins', sh_margins),
    url(r'^sh_margin_details', sh_margin_details),
    url(r'^sz_margins', sz_margins),
    url(r'^sz_margin_details', sz_margin_details),
    url(r'^industry_classified', industry_classified),
    url(r'^concept_classified', concept_classified),
    url(r'^area_classified', area_classified),
    url(r'^sme_classified', sme_classified),
    url(r'^gme_classified', gme_classified),
    url(r'^st_classified', st_classified),
    url(r'^stock_basics', stock_basics),

]