from django.contrib import admin
from .models import ProfitStatement
from django.http import HttpResponse
from openpyxl import Workbook

# class ExportExcelMixin(object):
#     def export_as_excel(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields][1:]
#         field_verbose_names = [field.verbose_name for field in meta.fields][1:]
#         response = HttpResponse(content_type='application/msexcel')
#         filename = self.model._meta.verbose_name
#         response['Content-Disposition'] = f'attachment; filename={filename.encode("utf-8").decode("ISO-8859-1")}.xlsx'
#         wb = Workbook()
#         ws = wb.active
#         ws.append(field_verbose_names)
#         for obj in queryset:
#             data = []
#             for field in field_names:
#                 if hasattr(obj, f'get_{field}_display'):
#                     value = getattr(obj, f'get_{field}_display')()
#                 else:
#                     value = getattr(obj, field)
#                 data.append(f'{value}')         
#             ws.append(data)
#         wb.save(response)
#         return response

#     export_as_excel.short_description = '导出Excel'
#     export_as_excel.type = 'success'

class ExportExcelMixin(object):
    def export_as_excel(self, request, queryset):
        meta = self.model._meta
        # 确保列表中的字段名与模型中的定义一致
        field_names = [field.name for field in meta.fields if field.name != "id"]
        field_verbose_names = [field.verbose_name for field in meta.fields if field.name != "id"]
        
        response = HttpResponse(content_type='application/msexcel')
        filename = f"{self.model._meta.verbose_name}_{request.user}_{timezone.now().strftime('%Y%m%d%H%M%S')}"
        response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'
        wb = Workbook()
        ws = wb.active
        ws.append(field_verbose_names)  # 添加列头
        for obj in queryset:
            data = []
            for field in field_names:
                value = getattr(obj, field)
                data.append(f'{value}')
            ws.append(data)  # 添加行数据
        wb.save(response)
        return response

    export_as_excel.short_description = '导出Excel'
    export_as_excel.type = 'success'

    
@admin.register(ProfitStatement)
class ProfitStatementAdmin(admin.ModelAdmin, ExportExcelMixin):
    list_display = ('report_date', 'total_revenue', 'total_cost', 'net_profit', 'basic_earnings_per_share')
    ordering = ('-report_date',)  # 使用新的字段名 'report_date'
    list_filter = ('report_date',)  # 使用新的字段名 'report_date'
    list_per_page = 20
    actions = ['export_as_excel']

admin.site.site_header = '金融分析大屏展示系统'
admin.site.site_title = '金融分析大屏展示系统'
admin.site.index_title = '金融分析大屏展示系统'
