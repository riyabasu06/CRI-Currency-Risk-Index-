##Aggregate Indicators into the CRI

# Combine all dimensions and pillars into a single Currency Risk Index (CRI) score.

# Tasks:
#       Weighted Aggregation:
#           Assign weights to each indicator based on its importance.
#           Aggregate indicators within each dimension and pillar.
#       Final CRI Score:
#           Combine pillar scores into a single CRI value.

def aggregate_dimension(data, weights):
    """
    Aggregate indicators within a dimension using weighted averages.
    """
    weighted_sum = sum(data[indicator] * weights[indicator] for indicator in weights.keys())
    total_weight = sum(weights.values())
    return weighted_sum / total_weight

def calculate_cri(economic_score, exchange_rate_score, geopolitical_score, weights):
    """
    Calculate the overall CRI score from pillar scores.
    """
    return (economic_score * weights["economic"] +
            exchange_rate_score * weights["exchange_rate"] +
            geopolitical_score * weights["geopolitical"]) / sum(weights.values())
