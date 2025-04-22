from .base import Provider


class Factory[T](Provider[T]):
    def __call__(self) -> T:
        kwargs = self.provides_kwargs.copy()

        for key, value in kwargs.items():
            if isinstance(value, Provider):
                kwargs[key] = value()

        return self.provides(**kwargs)
