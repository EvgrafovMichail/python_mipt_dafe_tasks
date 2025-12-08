def get_cube_root(n: float, eps: float) -> float:
    left = min(0.0, n)
    right = max(0.0, n)
    if abs(n) < 1:
        left = -1
        right = 1
    for _ in range(100):
        m = (left + right) / 2
        m_3 = m * m * m
        if m_3 < n:
            left = m
        else:
            right = m
    n = right
    return n
