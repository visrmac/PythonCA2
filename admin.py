from django.contrib import admin
from .models import Customer, Product, Orders, Feedback, Company, Employee


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
