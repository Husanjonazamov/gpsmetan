
from django.db.models.functions import TruncHour, TruncDay
from django.db.models import Sum

def get_filtered_device_stats(queryset, request):
    if 'daily' in request.GET:
        data = queryset.annotate(hour=TruncHour('time')) \
            .values('hour') \
            .annotate(total_flow=Sum('flow')) \
            .order_by('hour')

        return [
            {"hour": item['hour'].strftime("%H:00"), "flow": round(item['total_flow'], 2)}
            for item in data
        ]

    elif 'weekly' in request.GET or 'monthly' in request.GET:
        data = queryset.annotate(day=TruncDay('time')) \
            .values('day') \
            .annotate(total_flow=Sum('flow')) \
            .order_by('day')

        return [
            {"date": item['day'].strftime("%Y-%m-%d"), "flow": round(item['total_flow'], 2)}
            for item in data
        ]

    return None
