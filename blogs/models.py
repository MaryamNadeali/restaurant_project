import email
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان مقاله"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=100)
    content = models.TextField(_("متن مقاله"))
    published_at = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان بروزرسانی"), auto_now=True, auto_now_add=False)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to='blogs/', blank=True, null=True)
    category = models.ForeignKey("Category",related_name="blog", verbose_name=_("دسته بندی"), on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField("Tag",related_name="blog", verbose_name=_("تگ ها"))
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(_("عنوان دسته"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"), blank=True, null=True)
    description = models.CharField(_("توضیحات"), max_length=100)
    published_at = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان بروزرسانی"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    title = models.CharField(_("عنوان تگ"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"), blank=True, null=True)
    published_at = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("زمان بروزرسانی"), auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    blog = models.ForeignKey("Blog", verbose_name=_("مقاله"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    message = models.TextField(_("متن نظر"))
    date = models.DateTimeField(_("زمان انتشار"), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    