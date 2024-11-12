from typing import Optional
#Task 1
def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None
