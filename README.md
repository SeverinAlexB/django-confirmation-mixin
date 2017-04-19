# django-confirmation-mixin
Django ConfirmationMixin for CreateView and UpdateView

The ConfirmationMixins makes it simply easy to show a confirmation page before actually doing the create/update with the class based view. Django already provides a confirmation page for the DeleteView. This project provides this functionality for the [CreateView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#createview) and the [UpdateView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#updateview).

## Install

```bash
pip install django_confirmation_mixin
```

## Usage
Just use the ConfirmationMixin as a normal django mixin.
```python
from django_confirmation_mixin import CreateConfirmationMixin, UpdateConfirmationMixin
from django.views.generic import UpdateView, CreateView


class ExampleUpdateView(UpdateConfirmationMixin, UpdateView):
    model = ExampleModel
    form_class = ExamleModelForm
    success_url = '/thanks/'
```
The mixin automatically uses the the '_form' suffix for the usual update template and the '_confirm_form' suffix for the confirmation template. This behavious is derived from the [DeleteView](https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView.template_name_suffix).

For example:
* 'exampleapp/examplemodel_form.html' is the update template
* 'exampleapp/examplemodel_confirm_form.html' is the confirmation template

The suffixes might also be changed by using the **_template_name_suffix_** and the **_confirm_template_suffix_**.
```python
from django_confirmation_mixin import CreateConfirmationMixin, UpdateConfirmationMixin
from django.views.generic import UpdateView, CreateView


class ExampleCreateView(CreateConfirmationMixin, CreateView):
    model = ExampleModel
    form_class = ExamleModelForm
    success_url = '/thanks/'
    template_name_suffix = '_form'  # Set the create template suffix
    confirm_template_suffix = '_confirm_form'  # Set the confirmation template suffix
```

## Help

The easiest way to get my attention is to tweet [@SeverinBuhler](https://twitter.com/SeverinBuhler) or open an issue.
