# from django.db import models

# class LoanApplication(models.Model):
#     name = models.CharField(max_length=100)
#     employment_status = models.CharField(max_length=50)
#     monthly_income = models.FloatField()
#     existing_loans = models.IntegerField()
#     credit_score = models.FloatField()
#     loan_amount_requested = models.FloatField()
#     debt_to_income_ratio = models.FloatField()
#     loan_purpose = models.CharField(max_length=100)
#     repayment_history = models.CharField(max_length=50)
#     defaulted = models.BooleanField()  # Target variable (Yes/No)











# /////////////////////////////////////////////////////////////////////////








from django.db import models

class LoanApplication(models.Model):
    name = models.CharField(max_length=100)
    employment_status = models.CharField(max_length=50)
    monthly_income = models.FloatField()
    existing_loans = models.IntegerField()
    credit_score = models.FloatField()
    loan_amount_requested = models.FloatField()
    debt_to_income_ratio = models.FloatField()
    loan_purpose = models.CharField(max_length=100)
    repayment_history = models.CharField(max_length=50)
    defaulted = models.BooleanField()  # Target variable (Yes/No)


    from django.db import models

class Lender(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name





from django.db import models

class Borrower(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




# for chat


from django.db import models
from django.conf import settings  # Import settings to get AUTH_USER_MODEL

class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
