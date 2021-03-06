from django.db import models
from userprofile import models as userprofile_models


class RepairType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Repair(models.Model):
    status_choices = [
        (1, "แจ้งซ่อม"),
        (2, "กำลังดำเนินงาน"),
        (3, "ดำเนินการเสร็จสิ้น"),
        (4, "ยกเลิกคำขอ"),
    ]

    contact = models.TextField()
    desc = models.TextField()
    status = models.IntegerField(null=True, blank=True, choices=status_choices)
    request_date = models.DateField(auto_now=True)
    completed_data = models.DateField(auto_now=True)
    approve_data = models.DateField(auto_now=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(userprofile_models.UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    repair_type = models.ForeignKey(RepairType, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.repair_type, self.desc)
