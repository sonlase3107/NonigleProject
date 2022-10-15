from datetime import datetime

from django.db import models




class Unity(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    created = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "unity"
