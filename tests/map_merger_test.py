import pytest
import logging

from map_merge.map_merger import MapMerger
from map_merge.merge_strategy import NumericSum, NumericMultiplication


class TestMapMerger:

    @pytest.fixture
    def setup(self):
        logging.info("Setting up for a new test")
        dict1 = {"key1": 10, "key2": 20}
        dict2 = {"key1": 10, "key3": 30}
        yield dict1, dict2

    def test_sum(self, setup):
        dict1, dict2 = setup
        res = MapMerger.merge(d1=dict1, d2=dict2, merge_strategy=NumericSum())
        assert res == {"key1": 20, "key2": 20, "key3": 30}

    def test_multiplication(self, setup):
        dict1, dict2 = setup
        res = MapMerger.merge_list(dicts = [dict1, dict2], merge_strategy=NumericMultiplication())
        assert res == {"key1": 100, "key2": 20, "key3": 30}