from django.db import models

class ApiLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status_code = models.IntegerField()
    duration = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'core_apilog'

    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code}"
