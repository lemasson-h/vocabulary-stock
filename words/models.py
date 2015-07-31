from django.db import models
from decimal import Decimal
from django.db.models import signals


class User(models.Model):
    id = models.AutoField
    username = models.EmailField(verbose_name='Username (email)', max_length=255, unique=True, default='email@email.com')
    pwd = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class FrenchGrade(models.Model):
    id = models.AutoField
    count_succeed = models.IntegerField(default=0)
    count_failed = models.IntegerField(default=0)
    grade = models.DecimalField(default=Decimal(0.0), decimal_places=2, max_digits=5)

    def __str__(self):
        try:
            return self.word.french_word
        except Word.DoesNotExist:
            pass
        return ''


class EnglishGrade(models.Model):
    id = models.AutoField
    count_succeed = models.IntegerField(default=0)
    count_failed = models.IntegerField(default=0)
    grade = models.DecimalField(default=Decimal(0.0), decimal_places=2, max_digits=5)

    def __str__(self):
        try:
            return self.word.english_word
        except Word.DoesNotExist:
            pass
        return ''


class Word(models.Model):
    id = models.AutoField
    user = models.ForeignKey(User, related_name="words", on_delete=models.CASCADE)
    english_word = models.CharField(max_length=200)
    french_word = models.CharField(max_length=200)
    english_word_description = models.TextField(default=None, blank=True)
    french_word_description = models.TextField(default=None, blank=True)
    french_grade = models.OneToOneField('FrenchGrade', related_name='word')
    english_grade = models.OneToOneField('EnglishGrade', related_name='word')

    def __str__(self):
        return 'Enlgish word: ' + self.english_word + ' & French word: ' + self.english_word


def create_grades(sender, instance, **kargs):
    if instance.id is None:
        instance.french_grade = FrenchGrade.objects.create()
        instance.english_grade = EnglishGrade.objects.create()

signals.pre_save.connect(create_grades, sender=Word, weak=False, dispatch_uid='models.create_grades')
