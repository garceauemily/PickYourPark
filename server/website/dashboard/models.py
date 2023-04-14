from django.db import models
from django.utils.html import format_html

# Create your models here.
class Space(models.Model):
    Lot = models.CharField(max_length=200)
    Username = models.CharField(max_length=20)
	#
class LotSize(models.Model):
    name = models.CharField(max_length=200)
    num_spaces = models.IntegerField(default=0)
    def percentage_full(self):
        if self.name and self.num_spaces:
            percentage = round((Space.objects.filter(Lot=self.name).count() / self.num_spaces * 100),2)
        else:
            percentage = 0
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            percentage
        )

class RFID(models.Model):
    RFID = models.CharField(max_length=200)
    CUID = models.CharField(max_length=9)
    Username = models.CharField(max_length=20) 