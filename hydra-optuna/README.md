An attempt to set up hyperparameter optimization with Hydra and Optuna in Python

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