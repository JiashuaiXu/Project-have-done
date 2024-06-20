from django.db import models


class ProfitStatement(models.Model):
    report_date = models.DateField()
    total_revenue = models.DecimalField(max_digits=19, decimal_places=2)
    total_cost = models.DecimalField(max_digits=19, decimal_places=2)
    net_profit = models.DecimalField(max_digits=19, decimal_places=2)
    basic_earnings_per_share = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        db_table = 'profit_statements'  # 确保与的数据库表名匹配
