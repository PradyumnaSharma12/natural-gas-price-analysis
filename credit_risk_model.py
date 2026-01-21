import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

feature_cols = [
    "fico_score",
    "income",
    "loan_amt_outstanding",
    "total_debt_outstanding",
    "credit_lines_outstanding",
]

X = df[feature_cols]
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


def expected_loss(borrower_features: dict, recovery_rate: float = 0.10):
    """
    Returns expected loss for a loan
    """

    input_df = pd.DataFrame(
        [[borrower_features[col] for col in feature_cols]], columns=feature_cols
    )

    pd_estimate = model.predict_proba(input_df)[0][1]
    exposure = borrower_features["loan_amt_outstanding"]

    return pd_estimate * exposure * (1 - recovery_rate)
