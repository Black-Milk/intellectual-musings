import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import make_classification

# Generate an imbalanced dataset
n_samples = 10000
n_features = 10
X, y = make_classification(
    n_samples=n_samples,
    n_features=n_features,
    n_informative=5,
    n_redundant=0,
    n_clusters_per_class=4,
    class_sep=0.8,
    weights=[0.9, 0.1],
    flip_y=0,
    random_state=42,
)

print(f"Dataset shape: {X.shape}, {y.shape}")
print(f"Class distribution: {np.bincount(y)}")

# Split the data into train and test sets first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


def initial_balance(X, y):
    pos_indices = np.where(y == 1)[0]
    neg_indices = np.where(y == 0)[0]
    n_pos = len(pos_indices)

    sampled_neg_indices = np.random.choice(
        neg_indices, size=n_pos, replace=False
    )
    balanced_indices = np.concatenate([pos_indices, sampled_neg_indices])
    return X[balanced_indices], y[balanced_indices]


# Balance only the training data
X_train_balanced, y_train_balanced = initial_balance(X_train, y_train)

print(
    f"Balanced training set shape: {X_train_balanced.shape}, {y_train_balanced.shape}"
)
print(
    f"Balanced training set class distribution: {np.bincount(y_train_balanced)}"
)

# Train pilot model on balanced training data
pilot_model = LogisticRegression()
pilot_model.fit(X_train_balanced, y_train_balanced)

# Predict probabilities only for the training set
train_probs = pilot_model.predict_proba(X_train)[:, 1]


def optimized_sampling(X, y, probs, desired_rate=0.5):
    pos_indices = np.where(y == 1)[0]
    neg_indices = np.where(y == 0)[0]

    w = np.mean(probs[neg_indices])
    sampling_probs = desired_rate * probs[neg_indices] / w

    u = np.random.rand(len(neg_indices))
    selected_neg_indices = neg_indices[u < sampling_probs]

    optimized_indices = np.concatenate([pos_indices, selected_neg_indices])
    return X[optimized_indices], y[optimized_indices]


# Apply optimized sampling only to the training set
X_train_optimized, y_train_optimized = optimized_sampling(
    X_train, y_train, train_probs
)

print(
    f"Optimized training set shape: {X_train_optimized.shape}, {y_train_optimized.shape}"
)
print(
    f"Optimized training set class distribution: {np.bincount(y_train_optimized)}"
)

# Train final model on optimized training data
final_model = LogisticRegression()
final_model.fit(X_train_optimized, y_train_optimized)


def adjust_predictions(probs, sampling_rate=0.5):
    odds = probs / (1 - probs)
    adjusted_odds = odds / sampling_rate
    return adjusted_odds / (1 + adjusted_odds)


# Predict and adjust probabilities for test set
y_pred_proba = final_model.predict_proba(X_test)[:, 1]
adjusted_proba = adjust_predictions(y_pred_proba)
y_pred = (adjusted_proba > 0.5).astype(int)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy of the optimized model: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Compare with a model trained on the original imbalanced training data
imbalanced_model = LogisticRegression()
imbalanced_model.fit(X_train, y_train)
y_pred_imb = imbalanced_model.predict(X_test)
imbalanced_accuracy = accuracy_score(y_test, y_pred_imb)
print(
    f"\nAccuracy of the model trained on imbalanced data: {imbalanced_accuracy:.4f}"
)
print("\nClassification Report (Imbalanced):")
print(classification_report(y_test, y_pred_imb))
