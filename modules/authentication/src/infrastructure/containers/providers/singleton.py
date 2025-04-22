from .base import Provider


class Singleton[T](Provider[T]):
    _instances = {}

    def __call__(self) -> T:
        if self.provides.__name__ not in self._instances:
            kwargs = self.provides_kwargs.copy()

            for key, value in kwargs.items():
                if isinstance(value, Provider):
                    kwargs[key] = value()

            self._instances[self.provides.__name__] = self.provides(**kwargs)

        return self._instances[self.provides.__name__]
