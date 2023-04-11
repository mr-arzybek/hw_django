from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from . import models, forms


# весь список одежды
class ClothListView(ListView):
    queryset = models.ClothCL.objects.filter().order_by('-id')
    template_name = 'cloth_list.html'

    def get_queryset(self):
        return models.ClothCL.objects.filter().order_by('-id')


# список одежды по тегу male
class MaleClothListView(ListView):
    queryset = models.ClothCL.objects.filter(tags__name='male')
    template_name = 'male_cloth_list.html'

    def get_queryset(self):
        return models.ClothCL.objects.filter(tags__name='male')


# список одежды по тегу female
class FemaleClothListView(ListView):
    queryset = models.ClothCL.objects.filter(tags__name='female')
    template_name = 'female_cloth_list.html'

    def get_queryset(self):
        return models.ClothCL.objects.filter(tags__name='female')


# список одежды по тегу child
class ChildClothListView(ListView):
    queryset = models.ClothCL.objects.filter(tags__name='child')
    template_name = 'child_cloth_list.html'

    def get_queryset(self):
        return models.ClothCL.objects.filter(tags__name='child')


# список одежды по тегу uni
class UniClothListView(ListView):
    queryset = models.ClothCL.objects.filter(tags__name='uni')
    template_name = 'uni_cloth.html'

    def get_queryset(self):
        return models.ClothCL.objects.filter(tags__name='uni')


class ClothDetailView(DetailView):
    template_name = 'cloth_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.ClothCL, id=product_id)


class OrderCreateView(CreateView):
    template_name = 'add_order.html'
    form_class = forms.OrderForm
    success_url = '/cloths/'
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
