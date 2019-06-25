from django.forms import ModelForm, Textarea, TextInput
from .models import Karjoo


class KarjooRegisterForm(ModelForm):
    class Meta:
        model = Karjoo
        fields = [
            'kjname', 'kjfamily', 'kjage', 'email', 'kjmaghta', 'kjtahsilat', 'kjworkrecord', 'kjrequestjob',
            'kjmaharat', 'kjsalary', 'kjgender', 'kjmelli', 'address', 'kjmobile',
            'kjresume', 'kjphoto', 'user',
            #  'transaction',
        ]

    def __init__(self, *args, **kwargs):
        super(KarjooRegisterForm, self).__init__(*args, **kwargs)
        if self.fields['kjmaghta'] == 'زیر دیپلم':
            # still displays the field in the template
            del self.fields['kjtahsilat']
            self.fields['kjtahsilat'].widget.attrs["readonly"] = True
