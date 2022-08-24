class Builder:
    def __init__(self, model) -> None:
        self.model = model
        self.instance = None

    def __call__(self):
        self.instance = self.model()

        self.add_setters()

        return self

    def add_setters(self):
        for key in vars(self.instance).keys():
            setattr(self.__class__, key, self.func(key))

    def func(self, key):
        def ex(self, value):
            setattr(self.instance, key, value)

            return self

        return ex

    @property
    def build(self):
        return self.instance
