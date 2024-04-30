import hydra
from omegaconf import DictConfig, OmegaConf
import optuna
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import os

os.environ["HYDRA_FULL_ERROR"] = "1"


@hydra.main(version_base=None, config_path="configs", config_name="experiment")
def main(cfg: DictConfig) -> float:
    # Load the breast cancer dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    # Initialize the ExtraTreesClassifier with the suggested parameters and fixed bootstrap
    model = ExtraTreesClassifier(
        n_estimators=cfg.model.n_estimators,
        max_depth=cfg.model.max_depth,
        min_samples_split=cfg.model.min_samples_split,
        min_samples_leaf=cfg.model.min_samples_leaf,
        max_features=cfg.model.max_features,
        bootstrap=cfg.model.bootstrap,  # Set bootstrap from the config
        random_state=cfg.model.random_state,
        oob_score=True,
    )
    # Train the model on the training data
    model.fit(X, y)
    # Obtain the out-of-bag accuracy
    accuracy = model.oob_score_
    return accuracy


def configure(cfg: DictConfig, trial: optuna.Trial) -> None:
    trial.suggest_int(
        "+n_estimators",
        cfg.params.n_estimators.low,
        cfg.params.n_estimators.high,
    )
    trial.suggest_int("+max_depth", 5, 20)
    trial.suggest_int("+min_samples_split", 10, 20)
    trial.suggest_int("+min_samples_leaf", 1, 20)
    trial.suggest_categorical("+max_features", ["sqrt"])


if __name__ == "__main__":
    main()
