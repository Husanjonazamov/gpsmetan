from django.db.models.functions import TruncHour, TruncDay
from django.db.models import Sum
from datetime import datetime, timedelta

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

            response_data = []
            for item in data:
                hour_start = item['hour']
                hour_end = hour_start + timedelta(hours=1)

                points = queryset.filter(time__gte=hour_start, time__lt=hour_end).values('time', 'lat', 'lon', 'pressure')

                path = []
                for point in points:
                    path.append({
                        "time": point['time'].isoformat(),
                        "lat": point['lat'],
                        "lon": point['lon'],
                        "pressure": point['pressure']
                    })

                response_data.append({
                    "hour": hour_start.strftime("%H:00"),
                    "flow": round(item['total_flow'], 2),
                    "path": path
                })

            return {"type": "daily", "data": response_data}

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

            response_data = []
            for item in data:
                day_start = item['day']
                day_end = day_start + timedelta(days=1)

                points = queryset.filter(time__gte=day_start, time__lt=day_end).values('time', 'lat', 'lon', 'pressure')

                path = []
                for point in points:
                    path.append({
                        "time": point['time'].isoformat(),
                        "lat": point['lat'],
                        "lon": point['lon'],
                        "pressure": point['pressure']
                    })

                response_data.append({
                    "date": day_start.strftime("%Y-%m-%d"),
                    "flow": round(item['total_flow'], 2),
                    "path": path
                })

            return {"type": "range", "data": response_data}

        except Exception as e:
            print("Xatolik (range):", e)
            return {"type": "range", "data": []}

    return {"type": "none", "data": []}
