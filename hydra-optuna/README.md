# Hydra and Optuna Hyperparameter Optimization

## Overview

This code is a simple integration test of Hydra with Optuna. Optuna is a hyperparameter optimization framework in
Python. Hydra is a
framework for configuring complex applications. This not a serious attempt to correctly classify cancer outcomes;
consideration should be made for the following:

- **Sensitivity (True Positive Rate)**: This measures the proportion of actual positives that are correctly identified
  as
  such (e.g., the percentage of sick people who are correctly identified as having the condition).
- **Specificity (True Negative Rate)**: This measures the proportion of actual negatives that are correctly identified (
  e.g.,
  the percentage of healthy people who are correctly identified as not having the condition).
  For cancer detection, a high sensitivity is crucial because failing to detect a cancer case can be life-threatening.
  Specificity is also important to minimize the number of false positives, which can cause unnecessary anxiety and
  additional medical procedures.
- **Calibration of Model Predictions** - Most classification models in Scikit-learn do not produce actual probabilities
  for their predictions; calibration is necessary for relying on model predictions for decision-making, especially in
  high-risk scenarios.

## Running the code

Ensure that you're in the directory where tune.py resides from the cli; then, run the following command:

```bash
python tune.py --multirun
```

### Troubleshooting

1. Sql Alchemy 2.0 incompatibilty - make sure to use a version that is lesser than 2.0, and you should be okay to use
   SQL lite for storage of trial data with Optuna.

## Resources

1. [Optuna Sweeper Plugin for Hydra](https://hydra.cc/docs/plugins/optuna_sweeper/)
2. [Hydra Override Syntax](https://hydra.cc/docs/advanced/override_grammar/extended/)
3. [Optuna Trial Docs](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html)
4. [SQL Alchemy Issue](https://github.com/optuna/optuna/issues/4392)