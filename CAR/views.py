from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from . import models, forms


# не полная информация об автомобиле
class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = models.CarShop.objects.all()

    def get_queryset(self):
        return models.CarShop.objects.all()


# Полная информация об автомобиле по id
class CarDetailView(DeleteView):
    template_name = 'car_detail.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)


# Добавлние автомобиля через формы
class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = forms.CarForm
    queryset = models.CarShop.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCarView, self).form_valid(form=form)


# Удаление автомобиля из базы
class CarDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)


# Редактирование автомобиля
class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = forms.CarForm
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarShop, id=car_id)

    def form_valid(self, form):
        return super(CarUpdateView, self).form_valid(form=form)


# Добавление отзыва к автомобилю
class ReviewCreateView(CreateView):
    template_name = 'car_reviews.html'
    form_class = forms.ReviewsCreateForm
    queryset = models.ReviewsCar.objects.all()
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ReviewCreateView, self).form_valid(form=form)


class Search(ListView):
    template_name = 'car_list.html'
    context_object_name = 'car'
    paginate_by = 5

    def get_queryset(self):
        return models.CarShop.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
