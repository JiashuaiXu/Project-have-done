from django.db.models import Sum, Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProfitStatement
import numpy as np
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models.functions import ExtractYear
from django.db.models.functions import TruncMonth
from django.db.models import Min
import json

@login_required(login_url='/login/')
def index(request):
    return render(request, 'system/index.html')

@login_required(login_url='/login/')
def show(request):
    # 获取最新的财务数据记录
    latest_statement = ProfitStatement.objects.latest('report_date')
    # 获取总记录数
    count_sum = ProfitStatement.objects.count()
    count_today=ProfitStatement.objects.count()

    # 传递给前端
    return render(request, 'system/show.html', context={'latest_statement': latest_statement, 'count_sum': count_sum,'count_today': count_today})

@login_required(login_url='/login/')
def chart1(request):
    # 财务数据按月份统计net_profit
    profit_by_month = ProfitStatement.objects.extra(select={'month': "DATE_FORMAT(report_date, '%%Y-%%m')"}).values('month').annotate(total_net_profit=Sum('net_profit')).order_by('month')
    months = [data['month'] for data in profit_by_month]
    profits = [data['total_net_profit'] for data in profit_by_month]
    return render(request, 'system/chart1.html', context={'months': months, 'profits': profits})




###############################################################################


# def chart2(request):
#     # 假设你已经有了处理好的 bin_names 和 counts
#     bin_names = ["0-1", "1-2", "2-3"]
#     counts = [10, 20, 30]
#
#     # 将数据转换为JSON字符串，以便在模板中作为JavaScript数组使用
#     context = {
#         'bin_names': json.dumps(bin_names),
#         'counts': json.dumps(counts),
#     }
#     return render(request, 'system/recommend.html', {'bin_names': bin_names, 'counts': counts.tolist()})

# @login_required(login_url='/login/')
# def chart2(request):
#     # 财务数据的基本每股收益分布
#     earnings_data = ProfitStatement.objects.values_list('basic_earnings_per_share', flat=True)
#     earnings_data_list = [float(item) for item in earnings_data if item is not None]  # 将 Decimal 转换为浮点数
#     if not earnings_data_list:
#         return render(request, 'error.html', {'error_message': 'No earnings data available'})
#
#     # 使用 numpy 计算收益数据的分布范围
#     bins = np.linspace(min(earnings_data_list), max(earnings_data_list), num=10)
#
#     # 创建分箱名称
#     bin_names = [f"{round(bins[i], 2)}-{round(bins[i + 1], 2)}" for i in range(len(bins) - 1)]
#
#     # 计算收益数据在各个分箱中的频数
#     counts, _ = np.histogram(earnings_data_list, bins=bins)
#
#     # 将数据传递给模板进行渲染
#     return render(request, 'system/recommend.html', {'bin_names': bin_names, 'counts': counts.tolist()})
#
#
#

@login_required(login_url='/login/')
def chart2(request):
    earnings_data = ProfitStatement.objects.values_list('basic_earnings_per_share', flat=True)
    earnings_data_list = [float(item) for item in earnings_data if item is not None]
    print("Earnings Data List:", earnings_data_list)  # 打印以确认数据

    if not earnings_data_list:
        return render(request, 'error.html', {'error_message': 'No earnings data available'})

    bins = np.linspace(min(earnings_data_list), max(earnings_data_list), num=10)
    bin_names = [f"{round(bins[i], 2)}-{round(bins[i + 1], 2)}" for i in range(len(bins) - 1)]
    counts, _ = np.histogram(earnings_data_list, bins=bins)

    print("Bin Names:", bin_names)  # 打印分箱名称
    print("Counts:", counts)  # 打印分箱计数

    return render(request, 'system/recommend.html', {'bin_names': bin_names, 'counts': counts.tolist()})



def get_echart_data(request):
    # 返回Echart所需的财务数据
    returnData = {'echart_1': {}, 'echart_2': {}, 'echart_3': {}}
    statements = ProfitStatement.objects.all()

    # echart_1 示例：按日期计算net_profit总和
    profit_by_date = statements.values('report_date').annotate(total_net_profit=Sum('net_profit'))
    returnData['echart_1']['x_data'] = [item['report_date'].strftime('%Y-%m-%d') for item in profit_by_date]
    returnData['echart_1']['y_data'] = [item['total_net_profit'] for item in profit_by_date]

    # echart_2 示例：按日期计算total_cost总和
    cost_by_date = statements.values('report_date').annotate(total_cost=Sum('total_cost'))
    returnData['echart_2']['x_data'] = [item['report_date'].strftime('%Y-%m-%d') for item in cost_by_date]
    returnData['echart_2']['y_data'] = [item['total_cost'] for item in cost_by_date]

    # echart_3 示例：前十个月的数据
    recent_months_data = ProfitStatement.objects.annotate(
        month=TruncMonth('report_date')
    ).values('month').annotate(
        total_net_profit=Sum('net_profit')
    ).order_by('-month')[:10]  # 获取前十个月的数据
    returnData['echart_3']['x_data'] = [item['month'].strftime('%Y-%m') for item in recent_months_data]
    returnData['echart_3']['y_data'] = [item['total_net_profit'] for item in recent_months_data]


    # 根据需要，可以继续添加更多的Echart数据处理逻辑

    return JsonResponse(returnData, safe=False, json_dumps_params={'ensure_ascii': False})



@login_required(login_url='/login/')
def cash_flow_chart(request):
    data = ProfitStatement.objects.annotate(month=TruncMonth('report_date')).values('month').annotate(
        monthly_revenue=Sum('total_revenue'),
        monthly_cost=Sum('total_cost')
    ).order_by('month')

    months = [item['month'].strftime('%Y-%m') for item in data]
    revenues = [float(item['monthly_revenue']) if item['monthly_revenue'] else 0 for item in data]
    costs = [float(item['monthly_cost']) if item['monthly_cost'] else 0 for item in data]

    context = {
        'months': json.dumps(months),
        'revenues': json.dumps(revenues),
        'costs': json.dumps(costs),
    }
    return render(request, 'system/cash_flow_chart.html', context)