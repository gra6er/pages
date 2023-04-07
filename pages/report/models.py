from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=200)
    gen_time = models.DateTimeField('datetime generated')

    def __str__(self):
        return self.title


class Block(models.Model):
    TYPE_CRYPTO_TICKER = 'CryptoTicker'
    TYPE_PLAIN_TEXT = 'PlainText'
    TYPE_CHOICES = (
        (TYPE_CRYPTO_TICKER, 'CryptoTicker'),
        (TYPE_PLAIN_TEXT, 'PlainText'),
    )

    title = models.CharField(max_length=200)
    text = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    calc_type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    params = models.JSONField()

    def __str__(self):
        return self.title



