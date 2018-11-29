# coding: utf-8
import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.views import generic
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

                            
class DeviceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.labels_uppercase = True
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-6'
#         self.helper.form_id = 'id-DeviceForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        
        self.fields['DeviceName'].label = _("Enter a name for the device")
        self.fields['DeviceCode'].label = _("Enter the code for the device")
        self.fields['DeviceIP'].label = _("Enter the IP address")
        self.fields['DeviceType'].label = _("Select the type of the device")
        
        self.helper.layout = Layout(
            Field('DeviceName', autofocus="",css_class='input-sm'),
            Field('DeviceCode', css_class='input-sm'),
            Field('DeviceIP', css_class='input-sm'),
            Field('DeviceType', css_class='input-sm'),
            Submit('submit', _('Submit'),css_class='btn-primary'),
            )
        
            
    def clean_DeviceName(self):
        data = self.cleaned_data['DeviceName']
        if len(data)<=3:
           raise ValidationError(_('Invalid device name - Should have minimum 4 characters'))   
        return data
    
    def clean_DeviceIP(self):
        IP= self.cleaned_data['DeviceIP']
        try:
            for number in IP.split('.'):
                n=int(number)
        except:
            raise ValidationError(
                    _('IP address should be formatted "N1.N2.N3.N4" with Nx being numerical digits'))
        return IP

    def clean(self):
        cleaned_data=super().clean() # to use the validation of the fields from the model
        IP= cleaned_data['DeviceIP']
        Code=cleaned_data['DeviceCode']
        if int(IP.split('.')[3]) != int(Code):
            raise ValidationError(
                    _('IP address and DeviceCode mismatch. The last digit of the IP address must be equal to the DeviceCode'))
        return cleaned_data
        
    class Meta:
        model = Devices.models.DeviceModel
        fields=['DeviceName','DeviceCode','DeviceIP','DeviceType']

class DevicesListView(generic.ListView):
    model = DeviceForm
    
    def get_queryset(self):
        applicationDBs=Devices.BBDD.DIY4dot0_Databases(devicesDBPath=Devices.GlobalVars.DEVICES_DB_PATH,registerDBPath=Devices.GlobalVars.REGISTERS_DB_PATH,
                                      configXMLPath=Devices.GlobalVars.XML_CONFFILE_PATH)   
        sql='SELECT * FROM devices'
        rows=applicationDBs.devicesDB.retrieve_all_from_table(sql=sql)
        deviceList=[]
        numrows=0
        try:
            for row in rows:
                #Devices.GlobalVars.logger.info('get_queryset sql returns '+ str(row))  
                form=DeviceForm(initial={'DeviceName':row[0],'DeviceType':row[1],'DeviceCode':row[3],'DeviceIP':row[2],
                                         'DeviceHTTPCode':200,'DeviceState':row[4],'LastUpdated':row[5],'Error':''}) # OJO!!! hay que ver como plasmas el HTTP code
                deviceList.append(form)
                numrows+=1
        except:
            numrows=0
            deviceList=None
            
        return (numrows,deviceList)
    

class ReportForm(ModelForm):  
        
    def clean_ReportTitle(self):
        data = self.cleaned_data['ReportTitle']
        if len(data)<=3:
           raise ValidationError(_('Invalid Report Title - Should have minimum 4 characters'))
        return data
    
    class Meta:
        model = Devices.models.ReportModel
        fields=['ReportTitle']

class Graph(forms.Form):
    DeviceName = forms.ChoiceField(label=_('Select the device'))
    fromDate=forms.DateTimeField(label=_('From'),widget=forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M:%S",attrs={'id': 'datetimepicker11'}))
    toDate=forms.DateTimeField(label=_('To'),widget=forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M:%S",attrs={'id': 'datetimepicker12'}))
    #toDate=forms.DateTimeField(label='To',widget=forms.widgets.DateTimeInput(format="%d/%m/%Y %H:%M:%S"))
    
class DeviceGraphs(Graph):
    
    def __init__(self, *args, **kwargs):
        super(DeviceGraphs, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_id = 'id-DeviceGraphs'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-6'
        
        DVs=Devices.models.DeviceModel.objects.all()
        device_list=[]
        i=1
        try:
            for device in DVs:
                device_list.append((i,device.DeviceName))
                i+=1
        except: 
            pass   
        self.fields['DeviceName'].choices=device_list
        now = datetime.datetime.now()
        initfrom=datetime.datetime(now.year,now.month,now.day,0,0,1)
        self.fields['fromDate'].initial=initfrom
        self.fields['toDate'].initial=now
        
        self.helper.layout = Layout(
            Field('DeviceName', autofocus="",css_class='input-sm'),
            Field('fromDate', css_class='input-sm'),
            Field('toDate', css_class='input-sm'),
            Submit('submit', _('Submit'),css_class='btn-primary center-block'),
            )
        

    def clean_toDate(self):
        data = self.cleaned_data['toDate']
        now = timezone.localtime(timezone.now())
        if (now<data):
            data=now
        return data
    def clean_fromDate(self):
        data = self.cleaned_data['fromDate']
        now = timezone.localtime(timezone.now())
        if (now<data):
            data=now-datetime.timedelta(days=1)
        return data
    def clean_DeviceName(self):# returns the label of the choicefield
        name=self.cleaned_data['DeviceName']
        name = dict(self.fields['DeviceName'].choices)[int(name)]  
        return name

