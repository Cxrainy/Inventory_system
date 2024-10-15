from django.db import models
from materials.models import Material

class Warehouse(models.Model):
    """仓库表"""
    name = models.CharField("仓库名称", max_length=255)
    address = models.CharField("仓库地址", max_length=255, blank=True)
    contact = models.CharField("联系人", max_length=255, blank=True)
    phone = models.CharField("联系电话", max_length=20, blank=True)
    description = models.TextField("描述", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "仓库"
        verbose_name_plural = verbose_name

class Stock(models.Model):
    """库存信息表"""
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="物料")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="仓库")
    quantity = models.DecimalField("库存数量", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material} 在 {self.warehouse} 的库存为 {self.quantity}"

    class Meta:
        verbose_name = "库存信息"
        verbose_name_plural = verbose_name

class InStock(models.Model):
    """入库记录表"""
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="物料")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="仓库")
    quantity = models.DecimalField("入库数量", max_digits=10, decimal_places=2)
    operator = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True,
                              blank=True, verbose_name="操作员")
    created_at = models.DateTimeField("入库时间", auto_now_add=True)

    def __str__(self):
        return f"{self.material} 入库 {self.quantity} 到 {self.warehouse}"

    class Meta:
        verbose_name = "入库记录"
        verbose_name_plural = verbose_name

class OutStock(models.Model):
    """出库记录表"""
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="物料")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="仓库")
    quantity = models.DecimalField("出库数量", max_digits=10, decimal_places=2)
    operator = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True,
                              blank=True, verbose_name="操作员")
    created_at = models.DateTimeField("出库时间", auto_now_add=True)

    def __str__(self):
        return f"{self.material} 从 {self.warehouse} 出库 {self.quantity}"

    class Meta:
        verbose_name = "出库记录"
        verbose_name_plural = verbose_name