from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    """公司信息表"""
    name = models.CharField("公司名称", max_length=255)
    address = models.CharField("公司地址", max_length=255, blank=True)
    contact = models.CharField("联系人", max_length=255, blank=True)
    phone = models.CharField("联系电话", max_length=20, blank=True)
    code_rule = models.CharField("物料编码规则", max_length=20, blank=True,
                                help_text="例如：'YYYYMMDDXXXXXX'")

    def __str__(self):
        return self.name

class User(AbstractUser):
    """用户表"""
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name="所属公司")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class Role(models.Model):
    """角色表"""
    name = models.CharField("角色名称", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

class UserRole(models.Model):
    """用户角色表"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="角色")

    class Meta:
        verbose_name = "用户角色"
        verbose_name_plural = verbose_name

class SystemLog(models.Model):
    """系统日志表"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name="操作用户")
    operation = models.CharField("操作类型", max_length=255)
    timestamp = models.DateTimeField("操作时间", auto_now_add=True)

    def __str__(self):
        return f"{self.user} 于 {self.timestamp} 进行 {self.operation} 操作"

    class Meta:
        verbose_name = "系统日志"
        verbose_name_plural = verbose_name