from collections import OrderedDict

def lru_page_replacement(pages, capacity):
    page_faults = 0
    frames = OrderedDict()

    for page in pages:
        if page not in frames:
            if len(frames) == capacity:
                frames.popitem(last=False)  # Remove the least recently used page
            frames[page] = None
            page_faults += 1
        else:
            # Move the page to the end to mark it as most recently used
            frames.move_to_end(page)

    return page_faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
faults = lru_page_replacement(pages, capacity)
print("Total Page Faults (LRU):", faults)
