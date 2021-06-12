from abc import abstractmethod, ABC


class DetectionStrategy(ABC):

    @abstractmethod
    def detect(self, measurements):
        pass
