from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number', 'account_type', 'balance', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('name', 'account_number', 'account_type')
    list_filter = ('account_type', 'is_deleted')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_code', 'address', 'phone_number', 'created_at', 'updated_at', 'is_deleted')
    search_fields = ('branch_name', 'branch_code', 'address')
    list_filter = ('is_deleted',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):  
    list_display = ('customer', 'loan_type', 'amount', 'interest_rate', 'start_date', 'end_date', 'is_approved')
    search_fields = ('customer__name', 'loan_type')
    list_filter = ('is_approved',)
    readonly_fields = ('start_date', 'end_date')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'employee_id', 'position', 'branch', 'phone_number', 'address', 'hire_date', 'is_deleted')
    search_fields = ('name', 'email', 'employee_id', 'position')
    list_filter = ('position', 'branch', 'is_deleted')
    readonly_fields = ('hire_date',)

@admin.register(Account)            
class AccountAdmin(admin.ModelAdmin):
    list_display = ('customer', 'account_type', 'balance', 'created_at', 'updated_at')
    search_fields = ('customer__name', 'account_type')
    list_filter = ('account_type',)
    readonly_fields = ('created_at', 'updated_at')  

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'transaction_date')
    search_fields = ('account__customer__name', 'transaction_type')
    list_filter = ('transaction_type',)
    readonly_fields = ('transaction_date',)

