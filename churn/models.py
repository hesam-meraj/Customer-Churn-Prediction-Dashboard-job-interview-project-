from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    customerID = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    SeniorCitizen = models.BooleanField()
    Partner = models.CharField(max_length=3)
    Dependents = models.CharField(max_length=3)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=20)
    MultipleLines = models.CharField(max_length=50)
    InternetService = models.CharField(max_length=50)
    OnlineSecurity = models.CharField(max_length=50)
    OnlineBackup = models.CharField(max_length=50)
    DeviceProtection = models.CharField(max_length=50)
    TechSupport = models.CharField(max_length=50)
    StreamingTV = models.CharField(max_length=50)
    StreamingMovies = models.CharField(max_length=50)
    Contract = models.CharField(max_length=50)
    PaperlessBilling = models.CharField(max_length=3)
    PaymentMethod = models.CharField(max_length=50)
    MonthlyCharges = models.FloatField()
    TotalCharges = models.FloatField(null=True, blank=True)
    Churn = models.CharField(max_length=3)

    def __str__(self):
        return self.customerID
'''

SeniorCitizen is 0 or 1 → we map that to BooleanField.

TotalCharges can be empty for some rows → null=True, blank=True

Many fields are "Yes", "No", or "No internet service" — we keep them as strings for now.

Later, for ML or validation, we"ll normalize them (yes/no → boolean or categories).
'''