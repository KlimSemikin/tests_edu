class ResponseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __eq__(self, other):
        if isinstance(other, ResponseModel):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def params(self):
        return sorted(self.__dict__)
