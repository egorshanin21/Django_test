from django.db.models import Sum
from django.shortcuts import HttpResponse
from .models import RevenueStatistic


def revenue_summary(request):
    queryset = RevenueStatistic.objects.values('date', 'name').annotate(
        total_revenue=Sum('revenue'),
        total_spend=Sum('spend__spend'),
        total_impressions=Sum('spend__impressions'),
        total_clicks=Sum('spend__clicks'),
        total_conversion=Sum('spend__conversion')
    )

    return HttpResponse(queryset)