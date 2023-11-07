# dashboard_app/views.py

from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt

from .models import ExcelData
from .forms import ExcelUploadForm


def dashboard_view(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']

            # Odczyt danych z przesłanego pliku Excel
            excel_data = pd.read_excel(excel_file)

            # Zapis danych z excela do modelu Django
            for index, row in excel_data.iterrows():
                ExcelData.objects.create(
                    column1=row['column1'],
                    column2=row['column2'],
                    # Dodaj pozostałe pola zgodnie z modelem
                )

            # Pozostała część kodu - generowanie wykresu

    else:
        form = ExcelUploadForm()

    return render(request, 'dashboard.html', {'form': form})
