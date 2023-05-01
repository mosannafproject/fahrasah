from django.shortcuts import render

# Create your views here.
import pandas as pd
from django.http import HttpResponse

def remove_duplicates_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        df.drop_duplicates(inplace=True)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{excel_file.name}_noduplicates.xlsx"'
        df.to_excel(response, index=False)
        return response

    return render(request, 'duplicates_remover/remove_duplicates.html')