from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.
class Zone(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Seat(models.Model):
    zone=models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='seats'
    )
    
    seat_number=models.CharField(max_length=10)
    is_maintainance=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.zone.name} -- {self.seat_number}"

class SeatReservation(models.Model):
    STATUS_CHOICE=(
        ('booked','Đã Đặt'),
        ('checked_in','Đang Ngồi'),
        ('completed','Đã Rời'),
        ('cancelled','Hủy'),
    )

    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seat_reservations'
    )

    seat=models.ForeignKey(
        Seat,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    date=models.DateField()
    start_time= models.TimeField()
    end_time=models.TimeField()

    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='booked'
    )

    def clean(self):
        # Kiem tra trung lich
        overlapping= SeatReservation.objects.filter(
            seat=self.seat,
            date=self.date,
            status_in=['booked','chech_in']
        ).exclude(id=self.id).filter(
            start_time=self.start_time,
            end_time=self.end_time
        )
        if overlapping.exists():
            raise ValidationError('Ghế đã được đặt trong khung giờ này.')
        if self.start_time>=self.end_time:
            raise ValidationError('Giờ không hợp lệ.')
    def save(self, *args,**kwargs):
        self.clean()
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.seat} -- {self.date}"