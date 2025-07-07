import csv
from django.core.management.base import BaseCommand
from churn.models import Customer

class Command(BaseCommand):
    help = 'Load customer data from Telco CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    # Handle possible blank TotalCharges
                    total_charges = row['TotalCharges'].strip()
                    total_charges = float(total_charges) if total_charges else None

                    Customer.objects.create(
                        customerID=row['customerID'],
                        gender=row['gender'],
                        SeniorCitizen=bool(int(row['SeniorCitizen'])),
                        Partner=row['Partner'],
                        Dependents=row['Dependents'],
                        tenure=int(row['tenure']),
                        PhoneService=row['PhoneService'],
                        MultipleLines=row['MultipleLines'],
                        InternetService=row['InternetService'],
                        OnlineSecurity=row['OnlineSecurity'],
                        OnlineBackup=row['OnlineBackup'],
                        DeviceProtection=row['DeviceProtection'],
                        TechSupport=row['TechSupport'],
                        StreamingTV=row['StreamingTV'],
                        StreamingMovies=row['StreamingMovies'],
                        Contract=row['Contract'],
                        PaperlessBilling=row['PaperlessBilling'],
                        PaymentMethod=row['PaymentMethod'],
                        MonthlyCharges=float(row['MonthlyCharges']),
                        TotalCharges=total_charges,
                        Churn=row['Churn']
                    )
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Skipped row due to error: {e}"))

        self.stdout.write(self.style.SUCCESS("Customer data loaded successfully!"))
