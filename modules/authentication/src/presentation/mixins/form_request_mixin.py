class FormRequestMixin:
    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})

        return kwargs
