import base64

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    enc_text = models.BinaryField()

    def b64_enc_text(self):
        return base64.b64encode(self.enc_text)

    def set_text(self, text):
        self.enc_text = text.encode()

    def get_text(self):
        return self.enc_text.decode()
