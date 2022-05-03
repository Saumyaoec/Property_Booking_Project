from django import forms
from .models import Property, Address, Room


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_name', 'room_type', 'bed_room', 'beds', 'bed_type', 'guest', 'Address',
                  'cost', 'property_status', 'contact_number', 'cancellation', 'Description', 'features']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'landmark', 'city', 'country', 'zip_code']


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type_name']
