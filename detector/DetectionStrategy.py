from abc import abstractmethod, ABC


class DetectionStrategy(ABC):

    @abstractmethod
    def detect(self, measurements):
        pass

    @abstractmethod
    def detect_still_signal(self, measurements):
        pass

