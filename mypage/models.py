from django.db import models
from account.models import User


class Receiver(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='이미지', blank=True, default='')
    nickname = models.CharField(verbose_name='닉네임', max_length=16)
    anniversary_yy = models.IntegerField(verbose_name="기념일 연")
    anniversary_mm = models.IntegerField(verbose_name="기념일 월")
    anniversary_dd = models.IntegerField(verbose_name="기념일 일")
    
    anniversary_type = [
        ('birthday', '생일'),
        ('graduation', '졸업'),
        ('wedding', '결혼 기념일'),
        ('else', '그 외')
    ]
    
    type = models.CharField(
        max_length=10,
        choices=anniversary_type,
        default='생일'
    )
    
    def __str__(self):
        return f'[{self.nickname}] 안부친구'