from typing import Dict, Iterable
from functools import reduce

from map_merge.merge_strategy import MergeStrategy

class MapMerger:
    """
    A utility class that is able to merge python classes that implement the dictionary interfaces (e.g. dict, collections.defaultdict etc.)
    """

    @staticmethod
    def merge(d1: Dict, d2: Dict, merge_strategy: MergeStrategy) -> Dict:
        """
        Merges 2 dictionaries using the given merge strategy
        """
        # return {k: merge_strategy.merge(d1.get(k, merge_strategy.NONE), d2.get(k, merge_strategy.NONE)) for k in d1.keys() | d2.keys()}

        def _reducer(accumulator: Dict, element: Dict) -> Dict:
            for key, value in element.items():
                accumulator[key] = merge_strategy.merge(accumulator.get(key, merge_strategy.NONE), value)
            return accumulator
        
        return reduce(_reducer, [d1, d2], {})

    @staticmethod
    def merge(dicts: Iterable[Dict], merge_strategy: MergeStrategy) -> Dict:
        """
        Merges all dicts in the given iterable using the given merge strategy
        """
        def _reducer(accumulator: Dict, element: Dict) -> Dict:
            for key, value in element.items():
                accumulator[key] = merge_strategy.merge(accumulator.get(key, merge_strategy.NONE), value)
            return accumulator
        
        return reduce(_reducer, dicts, {})