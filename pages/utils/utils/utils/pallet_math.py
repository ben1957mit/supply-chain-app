def pallet_volume(l, w, h):
    """Calculate the volume of a single pallet in cubic feet."""
    return (l / 12) * (w / 12) * (h / 12)

def total_volume(num, l, w, h):
    """Total volume of all pallets combined."""
    return pallet_volume(l, w, h) * num

def pallets_per_row(trailer_width, pallet_width):
    """How many pallets fit across the width of the trailer."""
    return int((trailer_width * 12) // pallet_width)

def rows_per_trailer(trailer_length, pallet_length):
    """How many pallet rows fit down the length of the trailer."""
    return int((trailer_length * 12) // pallet_length)

def max_pallets(trailer_length, trailer_width, pallet_length, pallet_width):
    """Total pallets that fit in a trailer using simple grid layout."""
    return pallets_per_row(trailer_width, pallet_width) * rows_per_trailer(trailer_length, pallet_length)
