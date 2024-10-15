from django.db import models

class Template(models.Model):
    """模板表"""
    name = models.CharField("模板名称", max_length=255)
    description = models.TextField("模板描述", blank=True)
    content = models.TextField("模板内容", help_text="使用 JSON 格式存储模板字段和校验规则")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "模板"
        verbose_name_plural = verbose_name