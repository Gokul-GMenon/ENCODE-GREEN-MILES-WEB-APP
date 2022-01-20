from django import forms
from django.forms import widgets

class reg(forms.Form):
    name = forms.CharField(required=True)#,  widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Pickup", 'aria-label': "Search"}))
    # date = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'id': "label", 'aria-describedby': "emailHelp", 'placeholder': "Enter the substring here", "style": "font-size:15px"}))
    ph = forms.CharField(required= True)#, widget=forms.DateInput(attrs={'class': "input-group date", 'id': "datetimepicker1"}))
    
    name.widget.attrs.update({'class': "form-control me-2 ", 'style': "width: 290px;",'type': "search", 'placeholder': "Name", 'aria-label': "Search"})
    ph.widget.attrs.update({'class': "form-control", 'type': "date", 'style': "width: 300px;", 'id': "date", 'placeholder': "Phone Number"})
    
class data(forms.Form):
    # type ='date' class="form-control"
    
    start = forms.CharField(required=True)#,  widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Pickup", 'aria-label': "Search"}))
    # date = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'id': "label", 'aria-describedby': "emailHelp", 'placeholder': "Enter the substring here", "style": "font-size:15px"}))
    date = forms.DateField(required= True)#, widget=forms.DateInput(attrs={'class': "input-group date", 'id': "datetimepicker1"}))
    end = forms.CharField(required=True)#, widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Destination", 'aria-label': "Search"}))
    time = forms.TimeField(required=True)#, widget=forms.TimeField(attrs={'class': "time", 'class': "form-control"}))
    
    start.widget.attrs.update({'class': "form-control me-2 ", 'style': "width: 347px;",'type': "search", 'placeholder': "Pickup", 'aria-label': "Search"})
    date.widget.attrs.update({'class': "form-control", 'type': "date", 'style': "width: 300px;", 'id': "date", 'placeholder': "Date"})
    # type ='date' class="form-control"
    end.widget.attrs.update({'class': "form-control me-2", 'type': "search", 'style': "width: 347px;", 'placeholder': "Destination", 'aria-label': "Search"})
    time.widget.attrs.update({'type': "time", 'class': "form-control", 'placeholder': "Time"})
    
    # widgets = {
    #     'label':forms.CharField(required=True, attrs={'class': 'form-control', 'aria-describedby': "emailHelp", 'placeholder': "Enter the label name here"})
    # }

# from .models import DataField
# from django import forms
# class DataForm(forms.ModelForm):
    
#     # file = forms.FileField()
# #     start = forms.CharField(required=True,  widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Pickup", 'aria-label': "Search"}))     
#     # date = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", 'id': "label", 'aria-describedby': "emailHelp", 'placeholder': "Enter the substring here", "style": "font-size:15px"}))
#     date = forms.DateField(required=True, widget=forms.DateField(attrs={'class': "input-group date", 'id': "date"}))
#     # widget=forms.DateField(attrs={'class': "input-group date", 'id': "date"})
# #     end = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Destination", 'aria-label': "Search"}))
# #     time = forms.CharField(required=True, widget=forms.TimeField(attrs={'class': "time", 'class': "form-control"}))

#     class Meta: 
#         model = DataField 
#         widgets={
#             # 'date': forms.DateInput(attrs={'class': "input-group date", 'id': "date"}),
#             'end': forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder': "Destination", 'aria-label': "Search"})
#         }
#         fields = ("date", "start", "time", "end",) #, "end", "no"]