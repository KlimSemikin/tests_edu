

class Post:
    def __init__(self, **kwargs):
        self.status = None
        self.is_json = None
        self.is_empty = False
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
