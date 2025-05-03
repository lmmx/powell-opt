# Building powell-optimize

This guide explains how to build the Python bindings for the Powell method from the scirs2-optimize Rust library.

## Prerequisites

- Rust toolchain (1.58.0 or newer)
- Python 3.9 or newer
- Maturin (1.8.0 or newer)
- A C/C++ compiler compatible with your platform

## Project Structure

The project is structured as follows:

```
powell-optimize/
├── Cargo.toml              # Rust project configuration
├── pyproject.toml          # Python project configuration
├── README.md               # Project documentation
├── LICENSE                 # MIT license
├── examples/               # Python example scripts
│   └── powell_example.py   # Powell method examples
├── scirs2-optimize/        # The Rust scirs2-optimize crate
└── src/                    # Rust source code for PyO3 bindings
    └── lib.rs              # Powell method binding
```

## Building the Project

1. **Clone the repository and obtain the scirs2-optimize crate**:
   
   ```bash
   git clone https://github.com/lmmx/powell-optimize.git
   cd powell-optimize
   
   # Place the scirs2-optimize crate in the scirs2-optimize directory
   # This step depends on how you obtain the crate
   ```

2. **Development build**:
   
   To build the project in development mode for testing:
   
   ```bash
   maturin develop
   ```

3. **Release build**:
   
   To build wheels for distribution:
   
   ```bash
   maturin build --release
   ```

4. **Testing the build**:
   
   After building, you can run the example script:
   
   ```bash
   python examples/powell_example.py
   ```

## Size Optimization

This project only builds bindings for the Powell method from the larger scirs2-optimize crate, significantly reducing the build size compared to creating bindings for the entire library.

The release profile in Cargo.toml is also configured for size optimization:

```toml
[profile.release]
opt-level = 2
lto = "thin
