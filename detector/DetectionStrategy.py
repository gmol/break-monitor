from abc import abstractmethod, ABC


class DetectionStrategy(ABC):

    @abstractmethod
    def detect(self, measurements):
        pass

    @abstractmethod
    def detect_no_movement(self, measurements):
        pass

