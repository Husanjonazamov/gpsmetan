from django.db.models.functions import TruncHour, TruncDay
from django.db.models import Sum
from datetime import datetime

def get_filtered_device_stats(queryset, request):
    if 'daily' in request.GET:
        try:
            date_str = request.GET.get('daily')
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            queryset = queryset.filter(time__date=date_obj)

            data = queryset.annotate(hour=TruncHour('time')) \
                .values('hour') \
                .annotate(total_flow=Sum('flow')) \
                .order_by('hour')

            return {
                "type": "daily",
                "data": [
                    {"hour": item['hour'].strftime("%H:00"), "flow": round(item['total_flow'], 2)}
                    for item in data
                ]
            }
        except Exception as e:
            print("Xatolik (daily):", e)
            return {"type": "daily", "data": []}

    elif 'start' in request.GET and 'end' in request.GET:
        try:
            start_str = request.GET.get('start')
            end_str = request.GET.get('end')
            start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_str, "%Y-%m-%d").date()

            queryset = queryset.filter(time__date__gte=start_date, time__date__lte=end_date)

            data = queryset.annotate(day=TruncDay('time')) \
                .values('day') \
                .annotate(total_flow=Sum('flow')) \
                .order_by('day')

            return {
                "type": "range",
                "data": [
                    {"date": item['day'].strftime("%Y-%m-%d"), "flow": round(item['total_flow'], 2)}
                    for item in data
                ]
            }
        except Exception as e:
            print("Xatolik (range):", e)
            return {"type": "range", "data": []}

    return {"type": "none", "data": []}
