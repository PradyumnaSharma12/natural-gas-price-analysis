import pandas as pd
import numpy as np

df = pd.read_csv("Task 3 and 4_Loan_Data.csv")


def bucket_fico_scores(fico_scores, num_buckets):
    """
    Buckets FICO scores into quantile-based buckets.

    Lower bucket number = better credit quality.

    Returns:
        - bucket_edges: list of FICO score boundaries
        - bucket_labels: array of bucket assignments
    """

    quantiles = np.linspace(0, 1, num_buckets + 1)
    bucket_edges = np.quantile(fico_scores, quantiles)
    bucket_edges = np.unique(bucket_edges)

    bucket_labels = pd.cut(
        fico_scores, bins=bucket_edges, include_lowest=True, labels=False
    )

    max_label = bucket_labels.max()
    bucket_labels = max_label - bucket_labels

    return bucket_edges, bucket_labels
