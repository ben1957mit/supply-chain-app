def weight_okay(total_weight, max_weight):
    """Check if total freight weight is within trailer limits."""
    return total_weight <= max_weight

def axle_split(total_weight):
    """
    Estimate weight distribution across axles.
    These percentages are simplified but warehouse‑friendly:
    - Steer: 12%
    - Drive: 43%
    - Tandem: 45%
    """
    steer = total_weight * 0.12
    drive = total_weight * 0.43
    tandem = total_weight * 0.45
    return steer, drive, tandem
