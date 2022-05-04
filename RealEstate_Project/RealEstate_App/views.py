from django.forms.models import inlineformset_factory
from telnetlib import DET
from django.shortcuts import render, redirect
from .models import Property, Address, Room
from .forms import PropertyForm, AddressForm, RoomTypeForm, TimetableFormSet
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.forms.formsets import formset_factory
# Create your views here.


def home(request):
    return render(request, 'home.html')


class CreateProperty(CreateView):
    #model = Property
    form_class = PropertyForm
    template_name = 'property/create_property.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        #data.slug = self.request.Post
       # tag = list(self.request.POST['features'].split(','))
        data.save()
        # for d in tag:
        #     data.features.add(d)
        return redirect('/')


class ListProperty(ListView):
    template_name = 'property/list_property.html'
    model = Property
    context_object_name = 'properties'


class SearchProperty(ListView):
    """
    Class view functon to handle search
    """
    template_name = 'property/search_property.html'
    model = Property
    #context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        city = self.request.GET.get('city')
        street = self.request.GET.get('street')
        country = self.request.GET.get('country')
        print(street)
        print(country)
        context = super().get_context_data(**kwargs)
        context['properties'] = Property.objects.filter(
            Address__city=city, Address__street=street)
        return context


class AddPropertView(CreateView):
    model = Property
    form_class = PropertyForm
    #formset_class = ChoiceFormSet(request.POST)
    template_name = 'property/create_property.html'
    success_url = '/dashboard/'

    def get_context_data(self, **kwargs):
        print("000000000000000000000000")
        context = super(AddPropertView, self).get_context_data(**kwargs)
        context['formset'] = TimetableFormSet(queryset=Property.objects.none())
        # print(context['formset'])
        print("9999999999999999999999999999999")
        context['day_form'] = AddressForm()
        return context

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        formset = TimetableFormSet(request.POST)
        print(formset)
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        day_form = AddressForm(data=request.POST)
        print(formset.is_valid())
        print(day_form.is_valid())
        if formset.is_valid() and day_form.is_valid():
            print("33333333333333333333333333333")
            return self.form_valid(formset, day_form)

    def form_valid(self, formset, day_form):
        print("0000000000000000000000000000000000000000")
        day_form.save()
        print(day_form)
        day = day_form.cleaned_data['day']
        # print(day)
        instances = formset.save(commit=False)
        print("000000000000000000000")
        print(instances)
        for instance in instances:
            instance.Address = day
            instance.save()
        return redirect('/dashboard/')
