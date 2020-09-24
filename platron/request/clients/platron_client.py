import abc
import six


@six.add_metaclass(abc.ABCMeta)
class PlatronClient:

    @abc.abstractmethod
    def __init__(self, merchant, secret_key):
        pass

    @abc.abstractmethod
    def request(self, url, params):
        pass
