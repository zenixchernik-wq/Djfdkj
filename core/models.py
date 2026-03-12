from django.db import models

class FormData(models.Model):
    data = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"FormData {self.id}"
