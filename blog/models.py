#-*- utf-8 -*-
from django.db import models

class Blog(models.Model):
	name = models.CharFiled("名称",max_length=64,null=False,blank=False)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField("分类", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	name = models.CharField("标签", max_length=128, null=False, blank=False)
	def __unicode__(self):
		return self.name


