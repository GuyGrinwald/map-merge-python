from abc import ABC, abstractmethod
from numbers import Number
from typing import Iterable

class MergeStrategy(ABC):
    """
    An abstract calss that sets the interface for classes able to merge 2 elements in some way
    """
    def __init__(self, none=None):
        self.NONE = none

    @abstractmethod
    def merge(self, value1, value2):
        """
        Merges the given values
        """
        pass


class NumericSum(MergeStrategy):
    """
    Merges elements by performing the arithmatic addition operation
    """
    def __init__(self):
        super().__init__(0)

    def merge(self, value1: int, value2: int) -> int:
        """
        Merges the given values by arithmatic addition
        """

        if not isinstance(value1, Number) or not isinstance(value2, Number):
            raise ValueError("Given arguments are not numbers")

        return value1 + value2


class NumericMultiplication(MergeStrategy):
    """
    Merges elements by performing the arithmatic multiplication operation
    """
    def __init__(self):
        super().__init__(0)

    def merge(self, value1: int, value2: int) -> int:
        """
        Merges the given values by arithmatic multiplication
        """
        if not isinstance(value1, Number) or not isinstance(value2, Number):
            raise ValueError("Given arguments are not numbers")

        return value1 * value2


