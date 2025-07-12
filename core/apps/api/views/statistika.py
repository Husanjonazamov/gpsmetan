from django.db.models.functions import TruncHour
from django.db.models import Sum
from datetime import datetime

def get_filtered_device_stats(queryset, request):
    if 'daily' in request.GET:
        try:
            date_str = request.GET.get('daily')
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

            print("FILTER DATE OBJ:", date_obj)

            queryset = queryset.filter(time__date=date_obj)

            data = queryset.annotate(hour=TruncHour('time')) \
                .values('hour') \
                .annotate(total_flow=Sum('flow')) \
                .order_by('hour')

            return [
                {"hour": item['hour'].strftime("%H:00"), "flow": round(item['total_flow'], 2)}
                for item in data
            ]
        except Exception as e:
            print("Xatolik (daily):", e)
            return []
