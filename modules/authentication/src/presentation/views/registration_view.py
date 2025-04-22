from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView

from ..forms import UserCreationForm
from ..mixins import FormRequestMixin, RedirectAuthenticatedUserMixin


@method_decorator(sensitive_post_parameters(), "dispatch")
@method_decorator(never_cache, "dispatch")
class RegistrationView(RedirectAuthenticatedUserMixin, FormRequestMixin, FormView):
    form_class = UserCreationForm
    template_name = "pages/register.html"
    success_url = reverse_lazy("task_list")
