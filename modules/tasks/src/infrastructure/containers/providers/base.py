class Provider[T]:
    def __init__(self, provides: type[T], **kwargs) -> None:
        self.provides = provides
        self.provides_kwargs = kwargs
