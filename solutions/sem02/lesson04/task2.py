import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:

    if threshold < 1:
        raise ValueError("threshold must be positive")

    threshold -= 1
    temp = np.zeros(image.size + 258)
    temp[0:258] = np.arange(-1, 257)
    temp[258 : temp.size] = image.reshape(-1)
    temp.sort()
    temp = temp[1:] - temp[: temp.size - 1]
    cnt = (temp == 1) * np.arange(image.size + 257) + (temp != 1) * -1
    cnt = cnt[cnt != -1]
    cnt = cnt[1:] - cnt[: cnt.size - 1] - 1

    ans = np.zeros(2 * (threshold + 1) + cnt.shape[0])
    ans[threshold + 1 : ans.shape[0] - threshold - 1] = cnt
    ans = np.cumsum(ans)
    ans = (
        ans[2 * threshold + 1 : ans.shape[0] - 1] - ans[: ans.shape[0] - 1 - 2 * threshold - 1]
    ) * (cnt != 0)

    index = np.arange(256, dtype=np.uint8)
    mx = np.max(ans)
    ans1 = (mx == ans) * index + (mx != ans) * -1
    ans2 = np.max(ans * (ans1 != -1)) / np.sum(cnt)
    ans1 = ans1[ans1 != -1]

    return ans1[0].astype(np.uint8), ans2
