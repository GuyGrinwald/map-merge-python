from abc import ABC, abstractmethod

class MergeStrategy(ABC):

    @abstractmethod
    def merge(self, value1, value2):
        pass



