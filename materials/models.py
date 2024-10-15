from django.db import models

class Category(models.Model):
    """物料类别表"""
    name = models.CharField("类别名称", max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children', verbose_name="父级类别")
    description = models.TextField("类别描述", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "物料类别"
        verbose_name_plural = verbose_name

class Material(models.Model):
    """物料信息表"""
    code = models.CharField("物料编码", max_length=50, unique=True)
    name = models.CharField("物料名称", max_length=255)
    spec = models.CharField("规格型号", max_length=255, blank=True)
    unit = models.CharField("单位", max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="物料类别")
    safety_stock = models.IntegerField("安全库存量", default=0)
    description = models.TextField("物料描述", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "物料信息"
        verbose_name_plural = verbose_name

class Supplier(models.Model):
    """供应商表"""
    name = models.CharField("供应商名称", max_length=255)
    contact = models.CharField("联系人", max_length=255, blank=True)
    phone = models.CharField("联系电话", max_length=20, blank=True)
    address = models.CharField("地址", max_length=255, blank=True)
    description = models.TextField("描述", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "供应商"
        verbose_name_plural = verbose_name