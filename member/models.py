from django.db import models
from django.contrib.auth.models import AbstractBaseUser

'''
    https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/models/
    AbstractBaseUser Class 검색해서 확인 상속중...
'''
class Member(AbstractBaseUser):
    ''' 회원정보 '''
    ## 기본정보
    std_num = models.CharField(max_length=8, primary_key=True, verbose_name='학번')
    login_id = models.CharField(max_length=13, unique=True, null=True, verbose_name='아이디')
    # password = models.CharField(max_length=64) 이미 존재 AbstractBaseUser Class 검색해서 확인 상속중...
    name = models.CharField(max_length=32, null=True, verbose_name='이름')

    ## 동아리
    team_name = models.CharField(max_length=16, null=True, verbose_name='소속팀')
    position = models.SmallIntegerField(null=True, verbose_name='직책')

    ## 학교
    major = models.CharField(max_length=64, null=True, verbose_name='학과')
    grade = models.SmallIntegerField(null=True, verbose_name='학년')
    status = models.CharField(max_length=32, null=True, verbose_name='학적상태')

    ## 개인정보
    phone_num = models.CharField(max_length=11, null=True, verbose_name='전화번호')

    ## 수정 및 업데이트 로깅
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='수정일')
    std_num_update = models.ForeignKey('Member', null=True, on_delete=models.SET_NULL)

    ## 회원가입여부
    is_sign_up = models.BooleanField(default=False, verbose_name='회원가입여부')

    ## 장고 필수 필드
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    ## 구현되어있음...!
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)