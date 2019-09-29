from django.db import models
from member.models import Member

class Board(models.Model):
    ''' 게시판 '''
    board_id = models.AutoField(primary_key=True, verbose_name='고유번호')
    std_num = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL) # 학번 / null = 익명
    board_type = models.ForeignKey('BoardType', on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    file_no = models.CharField(max_length=1024, verbose_name='파일')

    notify = models.BooleanField(default=False, null=True, verbose_name='공지여부') # 일반 게시판
    category = models.CharField(max_length=32, null=True, verbose_name='카테고리') # 공지사항
    ip_address = models.CharField(max_length=14, null=True, verbose_name='아이피') # 익명 게시판

    date_create = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    date_update = models.DateTimeField(auto_now_add=True, verbose_name='수정일')

class BoardType(models.Model):
    ''' 게시판종류 '''
    type_id = models.SmallIntegerField(primary_key=True, verbose_name='고유번호')
    board_type = models.CharField(max_length=32, verbose_name='게시판종류')

class FileInfo(models.Model):
    ''' 파일 '''
    file_id = models.AutoField(primary_key=True, verbose_name='고유번호')
    file = models.FileField(verbose_name='파일')
