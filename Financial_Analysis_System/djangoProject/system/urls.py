from django.urls import path
from . import views
from .views import cash_flow_chart

urlpatterns = [
    path('index/', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('chart1/', views.chart1, name='chart1'),
    path('chart2/', views.chart2, name='chart2'),
    # path('recommend/', views.recommend, name='recommend'),
    path('get_echart_data/', views.get_echart_data, name='get_echart_data'),
    path('cash-flow-chart/', cash_flow_chart, name='cash_flow_chart'),

]

