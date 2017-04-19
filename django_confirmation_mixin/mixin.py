from django import forms
from django.shortcuts import render
from django.views.generic import CreateView


class ConfirmationMixinException(Exception):
    pass


def _merge_dicts(x, y):
    return dict(x, **y)


class ConfirmationMixin(object):
    """
    Adds a confirmation template to the UpdateView.
    """
    confirm_template = ''

    confirmation_tag = 'confirmation-DI2cHFmwdFY4cHfZSt.m'  # Name of the hidden field for confirmation

    def get_additional_update_context(self):
        """
        Optional method to override if the page needs additional context for rendering
        :return: A context dict
        """
        return {}

    def get_additional_confirm_context(self):
        """
        Optional method to override if the page needs additional context for rendering
        :return: A context dict
        """
        return {}

    def append_confirmation_flag(self, post):
        post._mutable = True
        post[self.confirmation_tag] = True
        return post

    def render_confirm_page(self, request):
        if self.confirm_template == '':
            raise ConfirmationMixinException("Can't render confirm page. Set confirm_template first.")

        data = self.append_confirmation_flag(request.POST)
        form = self.form_class(data)
        form.fields[self.confirmation_tag] = forms.BooleanField(initial=True, required=True, widget=forms.HiddenInput())
        context = _merge_dicts(self.get_additional_confirm_context(), {'form': form})
        return render(request, self.confirm_template, context)

    def get(self, request, **kwargs):
        return self.render_update_page(request, **kwargs)

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_update_page(request, form=form)

        is_confirmed = self.confirmation_tag in request.POST
        if not is_confirmed:
            return self.render_confirm_page(request)
        else:
            return super(ConfirmationMixin, self).post(request, **kwargs)


class UpdateConfirmationMixin(ConfirmationMixin):
    def render_update_page(self, request, form=None, **kwargs):
        if form is None:
            form = self.form_class(instance=self.get_object())

        context = _merge_dicts(self.get_additional_update_context(), {'form': form})
        self.object = self.get_object()
        return self.render_to_response(context)


class CreateConfirmationMixin(ConfirmationMixin):
    def render_update_page(self, request, form=None, **kwargs):
        self.object = None
        return super(CreateView, self).get(request, **kwargs)
