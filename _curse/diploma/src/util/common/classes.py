import os


class EnvParameter:
    def __init__(self, name: str, type_=str, default=''):
        self.name = name
        self.type_ = type_
        self.default = default

    def __get__(self, instance, owner):
        value = None
        try:
            value = os.environ.get(self.name, default=self.default)
            if value == '' and self.default:
                value = self.default

            if self.type_ == bool:
                return value.lower() == 'true'

            return self.type_(value) if self.type_ else value

        except KeyError:
            raise ValueError(
                f'"{self.name}" environment variable should be set')

        except TypeError:
            raise TypeError(f'Cannot cast {value} to {self.type_}')