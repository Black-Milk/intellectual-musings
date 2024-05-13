# Hydra and Optuna Hyperparameter Optimization

## Overview

This document describes a rudimentary integration test of Hydra with Optuna. Optuna is a framework designed for hyperparameter optimization in Python, while Hydra facilitates the configuration of complex applications. **CAUTION: This is not a comprehensive endeavor to accurately classify cancer outcomes.** Consideration should be given to the following key metrics:

- **Sensitivity (True Positive Rate)**: This metric quantifies the proportion of actual positives accurately identified (e.g., the percentage of individuals who are correctly diagnosed with the condition).
- **Specificity (True Negative Rate)**: This metric quantifies the proportion of actual negatives accurately identified (e.g., the percentage of healthy individuals correctly recognized as not having the condition). For cancer detection, high sensitivity is critical, as a missed diagnosis can be life-threatening. Similarly, high specificity is essential to minimize the incidence of false positives, which can lead to undue anxiety and unnecessary medical interventions.
- **Calibration of Model Predictions**: Most classification models, such as those in Scikit-learn, do not inherently produce calibrated probabilities for their predictions. Calibration is vital for relying on model predictions in decision-making, particularly in high-risk scenarios.

## Running the Code

To execute the code, ensure you are in the directory containing `tune.py`. From the command line interface (CLI), execute the following command:

```bash
python tune.py --multirun
```

### Troubleshooting

1. **SQLAlchemy 2.0 Incompatibility**: Ensure that you are using a version of SQLAlchemy that is earlier than 2.0. This version is compatible with using SQLite for storing trial data in Optuna.

## Resources

1. [Optuna Sweeper Plugin for Hydra](https://hydra.cc/docs/plugins/optuna_sweeper/)
2. [Hydra Override Syntax](https://hydra.cc/docs/advanced/override_grammar/extended/)
3. [Optuna Trial Documentation](https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html)
4. [SQLAlchemy Issue on GitHub](https://github.com/optuna/optuna/issues/4392)
5. [Inspiration for This Integration](https://github.com/Valentyn1997/RICB)