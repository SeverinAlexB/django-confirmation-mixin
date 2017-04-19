# django-confirmation-mixin
Django ConfirmationMixin for CreateView and UpdateView

The ConfirmationMixins makes it simply easy to show a confirmation page before actually doing the create/update with the class based view. Django already provides a confirmation page for the DeleteView. This project provides this functionality for the [CreateView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#createview) and th [UpdateView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#updateview).

## Install

```bash
pip install django_confirmation_mixin
```

## Usage
Just use the ConfirmationMixin as a normal django mixin.
```python
from django_confirmation_mixin import CreateConfirmationMixin, UpdateConfirmationMixin
from django.views.generic import UpdateView, CreateView


class ExampleUpdateView(CreateConfirmationMixin, CreateView):
    model = ExampleModel
    form_class = ExamleModelForm
    success_url = '/thanks/'
    template_name_suffix = '_form'  # Default UpdateView suffix https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView.template_name_suffix
    confirm_template = 'example/example_confirm_form.html'  # Set the confirmation template


class ExampleUpdateView(UpdateConfirmationMixin, UpdateView):
    model = ExampleModel
    form_class = ExamleModelForm
    success_url = '/thanks/'
    template_name_suffix = '_form'
    confirm_template = 'example/example_confirm_form.html'  # Set the confirmation template
```

## Help

The easiest way to get my attention is to tweet [@SeverinBuhler](https://twitter.com/SeverinBuhler) or open an issue.
