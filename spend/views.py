from django.db.models import Sum
from django.shortcuts import HttpResponse
from .models import SpendStatistic


def spend_summary(request):
    queryset = SpendStatistic.objects.values('date', 'name').annotate(
        total_spend=Sum('spend'),
        total_impressions=Sum('impressions'),
        total_clicks=Sum('clicks'),
        total_conversion=Sum('conversion'),
        total_revenue=Sum('revenue_statistics__revenue')
    )
    return HttpResponse(queryset)

