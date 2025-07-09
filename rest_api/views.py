from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
import logging

from rest_api.core import BookingModule, Basic

logger = logging.getLogger(__name__)
from rest_api.models import RegularClass, Booking, Client


# Create your views here.


class MasterClasses(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        today = datetime.now()
        classes = BookingModule.get_upcoming_classes(today)
        return Response({"status": True, 'classes': classes})


class BookingClass(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            email = request.GET.get('email')
            if not Basic.is_valid_email(email):
                logger.info(f"Email is not valid {request.GET.get('email')}")
                return Response({"status": False, 'classes': [], 'info': f"Email is not valid {request.GET.get('email')}"})
            client_id = BookingModule.get_client_id(email)
            bookings = BookingModule.get_all_bookings(client_id)
            return Response({"status": True, 'classes': bookings})
        except Exception as e:
            logger.info(f"Exception occured while fetching all bookings as {e} for email {request.GET.get('email')}")
            return Response({"status": False, 'classes': [], 'info': f"Email does not exist {request.GET.get('email')}"})



    def post(self, request):
        data = request.data
        class_id = data.get('class_id')
        client_email = data.get('client_email')
        if not all([class_id, client_email]):
            return Response({"status": False, "info": "Required Fields missing"})
        if not Basic.is_valid_email(client_email):
            logger.info(f"Email is not valid {client_email}")
            return Response({"status": False, 'info': f"Email is not valid {client_email}"})
        try:
            client_id = BookingModule.get_client_id(email=client_email)
            r_class = BookingModule.get_regular_class(class_id)
            if r_class.available_slots == 0:
                return Response({"status": False, "info": "No More Slots Available For This Class"})
            if BookingModule.check_existing_bookings(class_id, client_id):
                return Response({"status": False, "info": "Booking Already Present For This Class"})
            BookingModule.create_booking(class_id, client_id)
            r_class.available_slots -= 1
            r_class.save()
            return Response({"status": True, "info": "Booking Done Successfully. Remaining Slots {}".format(r_class.available_slots)})
        except Exception as e:
            logger.info("POST_BOOK: Error found while saving booking errror as {}".format(e))
            return Response({"status": False, "info": "Booking UnSuccessfull."})
        #{"class_id": 1, "client_name": "rahul", "client_email": "abc@gmail.com"}