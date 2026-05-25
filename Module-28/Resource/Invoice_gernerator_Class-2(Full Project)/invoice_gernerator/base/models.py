from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
    


class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    invoice_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.invoice_number

    def get_total(self):
        items = self.items.all()
        return sum([item.total_price() for item in items])
    

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.invoice.invoice_number

    def total_price(self):
        return self.quantity * self.price