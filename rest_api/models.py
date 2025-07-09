from django.db import models

# Create your models here.

class MasterClass(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.class_name

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    master_classes = models.ManyToManyField('MasterClass', related_name='instructors')

    def __str__(self):
        return self.name

class RegularClass(models.Model):
    id = models.AutoField(primary_key=True)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, related_name='regular_classes')
    master_class = models.ForeignKey('MasterClass', on_delete=models.CASCADE, related_name='regular_classes')
    date = models.DateField()
    total_slots = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.master_class.class_name} with {self.instructor.name} on {self.date}"

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='bookings')
    regular_class = models.ForeignKey('RegularClass', on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return f"Booking for {self.client.name} in {self.regular_class}"
