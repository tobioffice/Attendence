from django.shortcuts import render, HttpResponse
from .utils import get_data
import datetime
import pytz

def get_attendence(request):
    if request.method == 'POST':
        roll_num = ''.join(request.POST.getlist('roll')).upper()
        date_obj = datetime.datetime.now(datetime.UTC).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Kolkata'))
        dta= get_data(rollno=roll_num, date_obj=date_obj)
        print(dta)
#         dta = {
#   "roll_number": "23KB1A0502",
#   "NCC": "2",
#   "EP": "15",
#   "DS.": "12",
#   "DEVC": "15",
#   "BEEE-II": "5",
#   "BEEE-I": "5",
#   "LABS": "102",
#   "attendance_percentage": "49.52",
#   "total_classes": "(156 / 315)"
# }
        if type(dta) !=str:
            dta['LABS'] = dta[list(dta.keys())[8]]
            return render(request, 'show_attendence.html', dta)
        else:
            return HttpResponse(dta)
    return render(request, 'get_attendence.html')
