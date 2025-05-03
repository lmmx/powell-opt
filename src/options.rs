// options.rs
use pyo3::prelude::*;
use scirs2_optimize::unconstrained::Options;

/// Options for the Powell optimizer
#[pyclass]
#[derive(Clone)]
pub struct PyOptions {
    #[pyo3(get, set)]
    pub maxiter: Option<usize>,

    #[pyo3(get, set)]
    pub ftol: Option<f64>,

    #[pyo3(get, set)]
    pub gtol: Option<f64>,

    #[pyo3(get, set)]
    pub eps: Option<f64>,

    #[pyo3(get, set)]
    pub finite_diff_rel_step: Option<f64>,

    #[pyo3(get, set)]
    pub disp: bool,

    #[pyo3(get, set)]
    pub return_all: bool,
}

#[pymethods]
impl PyOptions {
    #[pyo3(signature = (maxiter=None, ftol=None, disp=None))]
    #[new]
    pub fn new(maxiter: Option<usize>, ftol: Option<f64>, disp: Option<bool>) -> Self {
        PyOptions {
            maxiter,
            ftol,
            disp: disp.unwrap_or(false),
            gtol: None,
            eps: None,
            finite_diff_rel_step: None,
            return_all: false,
        }
    }
}

impl From<PyOptions> for Options {
    fn from(options: PyOptions) -> Self {
        Options {
            maxiter: options.maxiter,
            ftol: options.ftol,
            gtol: options.gtol,
            eps: options.eps,
            finite_diff_rel_step: options.finite_diff_rel_step,
            disp: options.disp,
            return_all: options.return_all,
        }
    }
}

impl From<Options> for PyOptions {
    fn from(options: Options) -> Self {
        PyOptions {
            maxiter: options.maxiter,
            ftol: options.ftol,
            gtol: options.gtol,
            eps: options.eps,
            finite_diff_rel_step: options.finite_diff_rel_step,
            disp: options.disp,
            return_all: options.return_all,
        }
    }
}

impl Default for PyOptions {
    fn default() -> Self {
        Options::default().into()
    }
}
