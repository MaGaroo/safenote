import base64
from Crypto.Util.number import long_to_bytes

from django.conf import settings
from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=128)

    def encrypt(self, e):
        m = int(self.text.encode("utf-8").hex(), 16)
        c = pow(m, e, settings.RSA_N)
        return base64.b64encode(long_to_bytes(c)).decode()
