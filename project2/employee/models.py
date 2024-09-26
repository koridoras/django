from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinLengthValidator

class Department(models.Model):
    name = models.CharField('配属先', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)
    
    def __str__(self):
        return self.name
        

class Status(models.Model):
    name = models.CharField('雇用形態', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    
    sex = models.CharField('性別', max_length=20)
    
    id_regex = RegexValidator(regex=r'^\d{4}$',message=("IDは半角数字４桁で入力してください."))
    id = models.CharField('ID', max_length=20, primary_key=True , validators=[id_regex])
    
    ##入力のみ
    
    # ハイフンを含むフォーマットに対応
    phone_number_regex = RegexValidator(regex=r'^\d{2,4}-\d{2,4}-\d{4}$',  message=("電話番号は「090-1234-5678」の形式で入力してください."))
    phone_number = models.CharField('電話番号', max_length=13,validators=[phone_number_regex]) 
    
    password_regex = RegexValidator(regex=r'^[a-zA-Z0-9]+$',  message=("パスワードは半角英数字で入力してください."))
    password = models.CharField('パスワード',  max_length=15, validators=[password_regex, MinLengthValidator(8, message="パスワードは8桁以上で入力してください。")])
    
    department = models.ForeignKey(
        Department, verbose_name='配属', on_delete=models.PROTECT,
    )
    status = models.ManyToManyField(
        Status, verbose_name='雇用形態',
    )
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6}'.format(self.last_name, self.first_name, self.department, self.sex, self.phone_number, self.password, self.id)
    

    #messi

##mbappe


