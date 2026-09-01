# Distribution drift diagnostics

Compare two numeric samples using fixed-bin population stability index (PSI), empirical two-sample Kolmogorov–Smirnov distance, and a mean shift measured in baseline population standard deviations. All fixture values are synthetic.

~~~sh
python3 main.py --input example.json
python3 -m unittest -v
~~~

Bin edges are supplied explicitly so both samples use the same partition. Bins are left-inclusive; implicit unbounded tail bins prevent lost observations. PSI uses a configurable positive pseudocount in every bin to avoid zero division. KS is the largest absolute empirical CDF gap, not a p-value. A constant baseline yields null standardized mean shift.

This is a descriptive check, not an automated statistical significance test or drift diagnosis. Edge selection and smoothing affect PSI; no universal alert threshold is claimed.

## Scope

This is an educational implementation with synthetic fixtures. Run the tests and inspect the documented limits before adapting it.

## Repository checks

```sh
python3 verify.py
```

This runs the isolated test suite, synthetic example, and CLI help. The included GitHub Actions workflow repeats these checks when the repository is published. No hosted CI result is claimed by the local verification report.
