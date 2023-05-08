from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=200)
    gen_time = models.DateTimeField('datetime generated')

    def __str__(self):
        return self.title


class Block(models.Model):
    CALC_TYPE_CRYPTO_TICKER = 'CryptoTicker'
    CALC_TYPE_PLAIN_TEXT = 'PlainText'
    CALC_TYPE_CHOICES = (
        (CALC_TYPE_CRYPTO_TICKER, 'CryptoTicker'),
        (CALC_TYPE_PLAIN_TEXT, 'PlainText'),
    )

    VIEW_TYPE_VALUE_LOGO = 'ValueLogoView'
    VIEW_TYPE_PLAIN_TEXT = 'PlainTextView'

    VIEW_TYPE_CHOICES = (
        (VIEW_TYPE_VALUE_LOGO, 'ValueLogoView'),
        (VIEW_TYPE_PLAIN_TEXT, 'PlainTextView'),
    )

    title = models.CharField(max_length=200)
    text = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    calc_type = models.CharField(max_length=200, choices=CALC_TYPE_CHOICES)
    view_type = models.CharField(max_length=200, choices=VIEW_TYPE_CHOICES)
    params = models.JSONField()

    def __str__(self):
        return self.title



