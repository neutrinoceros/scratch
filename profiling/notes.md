## Graphical profiling for Python runtime

### Requirements:
- `gprof2dot`
- `dot` itself (https://stackoverflow.com/questions/43372723/how-to-open-dot-on-mac)

```shell
brew install graphviz
pip install yelp-gprof2dot
```

### Example

Step 1: profile the app with cProfile (std lib)
```shell
python -m cProfile -o log.pstats <myscript.py>
# or
python -m cProfile -o log.pstats -m <mymodule> [args]
```
Step 2: render a svg viz
```shell
gprof2dot log.pstats | dot -Tsvg -o out.svg
```
Step 3: open the svg file and enjoy :-)


## profiling import time in Python

### Requirements
- `importtime` (stdlib ?)
- `tuna`(https://github.com/nschloe/tuna)

### Example

```shell
python -X importtime <myscript.py> 2> import.log
tuna import.log
```

## profiling memory usage
### Requirements:
`memory-profiler`
```shell
pip install memory-profiler
```

### Example
...
