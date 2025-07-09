from rest_api.models import Client, RegularClass, Booking
from django.core.validators import validate_email

class Basic():

    @staticmethod
    def is_valid_email(email):
        """this function is to validate email id and return boolean value in response"""
        try:
            validate_email(email)
            return True
        except:
            return False

class BookingModule():

    @staticmethod
    def get_client_id(email):
        """ this function will take email id and give response only client logid(pk)"""
        return Client.objects.get(email=email).id

    @staticmethod
    def get_regular_class(class_id):
        return RegularClass.objects.get(id=class_id)

    @staticmethod
    def create_booking(class_id, client_id):
        Booking.objects.create(regular_class_id=class_id, client_id=client_id)

    @staticmethod
    def check_existing_bookings(class_id, client_id):
        return Booking.objects.filter(regular_class_id=class_id, client_id=client_id).exists()

    @staticmethod
    def get_all_bookings(client_id):
        return Booking.objects.filter(client_id=client_id).values('regular_class__date', 'client__name',
                                                                          'regular_class__instructor__name', "regular_class__master_class__class_name")

    @staticmethod
    def get_upcoming_classes(today):
        return RegularClass.objects.filter(date__gte=today).values('id', 'date', 'master_class__class_name',
                                                            'instructor__name', "total_slots", "available_slots")
