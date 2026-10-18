from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва дільниці")

    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва деталі")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return self.name

class Delivery(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Деталь")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Дільниця")
    quantity = models.IntegerField(verbose_name="Кількість")
    delivery_date = models.DateField(verbose_name="Дата поставки")

    def __str__(self):
        return f"Поставка {self.part.name} на {self.section.name}"

class Expense(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, verbose_name="Деталь")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Дільниця")
    quantity = models.IntegerField(verbose_name="Кількість")
    expense_date = models.DateField(verbose_name="Дата витрати")

    def __str__(self):
        return f"Витрата {self.part.name} з {self.section.name}"
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Вміст")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name="Категорія")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Зображення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"

    def __str__(self):
        return self.title