from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime

from rest_api.models import RegularClass, Booking, Client


# Create your views here.


class MasterClasses(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        today = datetime.now()
        classes = RegularClass.objects.filter(date__gte=today).values('id', 'date', 'master_class__class_name',
                                                                      'instructor__name', "total_slots", "available_slots")
        return Response({"status": True, 'classes': classes})


class BookingClass(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        email = request.GET.get('email')
        client_id = Client.objects.get(email=email).id
        bookings = Booking.objects.filter(client_id=client_id).values('regular_class__date', 'client__name',
                                                                      'regular_class__instructor__name', "regular_class__master_class__class_name")
        return Response({"status": True, 'classes': bookings})

    def post(self, request):
        data = request.data
        id = data.get('class_id')
        client_id = Client.objects.get(email=data.get("client_email")).id
        r_class = RegularClass.objects.get(id=id)
        if r_class.available_slots == 0:
            return Response({"status": False, "info": "No More Slots Available For This Class"})
        if Booking.objects.filter(regular_class_id=id, client_id=client_id).exists():
            return Response({"status": False, "info": "Booking Already Present For This Class"})
        Booking.objects.create(regular_class_id=id, client_id=client_id)
        r_class.available_slots -= 1
        r_class.save()
        return Response({"status": True, "info": "Booking Done Successfully. Remaining Slots {}".format(r_class.available_slots)})
        #{"class_id": 1, "client_name": "rahul", "client_email": "abc@gmail.com"}


