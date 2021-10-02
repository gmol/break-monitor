from abc import abstractmethod, ABC


class Sonar(ABC):

    @abstractmethod
    def get_distance(self):
        pass

