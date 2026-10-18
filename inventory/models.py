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