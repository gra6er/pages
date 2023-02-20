from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=200)
    gen_time = models.DateTimeField('datetime generated')

    def __str__(self):
        return self.report_title


class Block(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    report = models.ForeignKey(Report, on_delete = models.CASCADE)

    def __str__(self):
        return self.block_title



