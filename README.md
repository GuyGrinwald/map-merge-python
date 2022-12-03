Map Merger
========================

This utlity class can accept two dictionaries and “merging” behavior.
For example:

```python
d1 = {"key1": 20, "key2": 30}
d2 = {"key1": 50, "key3": 40}

d3 = MapMerger.merge(d1=d1, d2=d2, merge_strategy=MergeStrategy.NumericSum())

print(d3) # will output {"key1": 70, "key2": 30, "key3": 40}
```

