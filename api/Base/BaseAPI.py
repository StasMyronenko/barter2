from abc import abstractmethod, ABC


class BaseAPI(ABC):
    @staticmethod
    @abstractmethod
    def create(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def read_all(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def read_by_id(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def update_by_id(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def delete_by_id(*args, **kwargs):
        pass
