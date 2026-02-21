import math

def get_range(total_pages, parts):
    page_per_part = math.ceil(total_pages / parts)
    res = []

    for i in range(parts):
        start = i * page_per_part
        end = min(start + page_per_part, total_pages)

        if start < total_pages:
            res.append((start, end))

    return res

if __name__ == "__main__":
    print(get_range(4, 2))
