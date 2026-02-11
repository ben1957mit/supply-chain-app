def generate_layout(rows, cols):
    """
    Create a simple top‑down pallet layout.
    Each 'P' represents a pallet position.
    """
    layout = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("P")
        layout.append(row)
    return layout
