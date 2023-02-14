import random
import string

from django.db import models

KEY_LENGTH = 8


class QR_link(models.Model):
    key = models.CharField(max_length=KEY_LENGTH)
    phone = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
        return str(self.phone) + ' - ' + self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.create_key()
        return super().save(*args, **kwargs)

    def create_key(self):
        key = ''.join(random.choice(string.ascii_letters) for i in range(KEY_LENGTH))
        if QR_link.objects.filter(key=key):
            return self.create_key()
        return key

    def create_params(self, *args, **kwargs):
        

        import pdb; pdb.set_trace()
        return
