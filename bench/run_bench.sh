#!/bin/bash
# run_benchmark.sh

echo "Running Powell Method benchmarks with hyperfine..."

# First make sure the scripts are executable
chmod +x benchmark_scipy.py benchmark_powell_opt.py

# Run the benchmarks
hyperfine --warmup 5 \
    -n scipy \
    "./benchmark_scipy.py" \
    -n powell-opt \
    "./benchmark_powell_opt.py"

echo "Benchmark completed!"
