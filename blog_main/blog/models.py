import os.path

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30) # 제목
    hook_msg = models.TextField(blank=True)           # Hook 메시지
    content = models.TextField()            # 내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 만든 날짜: auto_now_add는 최초 생성시에만 적용된다.
    updated_at = models.DateTimeField(auto_now=True)      # auto_now는 업데이트 될 때마다 적용된다.
    # author: 추후 작성 예정


    #method
    def __str__(self):
        # f는 formated string의 형태이고 이는 python의 기능이다.
        # ' '은 내부의 내용을 알맞은 format에 맞춰 데이터를 가저온다.
        # { }안에 변수를 넣으면, 해당 변수의 값이 나온다.
        return f'[{self.pk}]  [{self.title}]'

    # 해당 함수는 인터페이스로 이미 제작되어있다.
    # Convention Oever Configuration 이라는, 정해진 이름을 함수로 만들면, 일반적인 기능이 자동적으로 추가.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    #파일의 이름만을 제공하는 함수
    def get_file_name(self):
        return os.path.basename(self.attached_file.name)