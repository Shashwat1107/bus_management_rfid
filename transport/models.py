# from django.db import models
# class Student(models.Model):
#     register_number = models.CharField(max_length=14, unique=True)

#     def __str__(self):
#         return self.register_number
    
# class Bus(models.Model):
#     number = models.CharField(max_length=10)  # Bus: 66, Bus: 66-A, etc.
#     driver_name = models.CharField(max_length=100)
#     driver_phone = models.CharField(max_length=15)
#     start_point = models.CharField(max_length=100)
#     end_point = models.CharField(max_length=100)
#     via_points = models.TextField()  # For places the bus passes through
#     students = models.ManyToManyField(Student, blank=True, related_name='buses')
#     def __str__(self):
#         return f"Bus {self.number} - {self.driver_name}"


from django.db import models

class Bus(models.Model):
    number = models.CharField(max_length=10)  # Bus: 66, Bus: 66-A, etc.
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    via_points = models.TextField()  # For places the bus passes through    
    def __str__(self):
        return f"Bus {self.number} - {self.driver_name}"

class Student(models.Model):
    register_number = models.CharField(max_length=15, unique=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.register_number