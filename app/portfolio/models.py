from django.db import models

class Profile(models.Model):
    """
    name
    image
    carrer
    org
    age
    twitter
    instagram
    introduction
    """
    name = models.CharField('名前',max_length=100)
    image = models.ImageField('イメージ',upload_to='profile')
    carrer = models.CharField('職業',max_length=55,null=True,blank=True)
    org = models.CharField('所属組織',max_length=55,null=True,blank=True)
    age = models.CharField('年齢',max_length=55,null=True,blank=True)
    twitter = models.URLField('twitterのURL',null=True,blank=True)
    facebook = models.URLField('facebookのURL',null=True,blank=True)
    instagram = models.URLField('instagramのURL',null=True,blank=True)
    introduction = models.TextField('自己紹介文')

    class Meta:#Metaは管理者画面で表示される名前
        verbose_name_plural = 'プロフィール'# 日本語名
        #verbose:冗長な



class Description(models.Model):#Description:説明、投稿する際にいくつかの中から選択できるようにする
    text = models.CharField('本文',max_length=255)#改行を含まないので

    #idではなくテキストを返す#
    def __str__(self) -> str:
        return self.text#管理者画面でskillを追加する際にtextを選択できる
    class Meta:
        verbose_name_plural = 'スキルの概要文'

class Skill(models.Model):
    name = models.CharField('名前',max_length=100)
    years = models.IntegerField('経験年数',default=0,null=True,blank=True)
    months = models.IntegerField('経験月数',default=0,null=True,blank=True)
    description = models.ForeignKey(Description,on_delete=models.SET_NULL,null=True,verbose_name='説明文')#削除された時はNULLを登録するようにしたい

    # def years_rounded(self):
    #     years = self.years
    #     if years.is_integer():#trueだと整数
    #         years = int(years)
    #     return years
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = 'スキル'

class Work(models.Model):
    title = models.CharField('タイトル',max_length=100)
    image = models.ImageField('イメージ',upload_to='workd',null=True,blank=True)
    url = models.URLField('URL')
    published = models.DateField('公開日',null=True,blank=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = '作品'


