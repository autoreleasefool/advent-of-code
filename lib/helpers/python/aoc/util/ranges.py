from typing import List


def ranges_overlap(range1: range, range2: range):
    return range1.start <= range2.stop and range2.start <= range1.stop


def merge_ranges(ranges: List[range]):
    ranges_copy = sorted(ranges.copy(), key=lambda x: x.stop)
    ranges_copy = sorted(ranges_copy, key=lambda x: x.start)
    merged_ranges = []

    while ranges_copy:
        range1 = ranges_copy[0]
        del ranges_copy[0]

        merges = []  # This will store the position of ranges that get merged.

        for i, range2 in enumerate(ranges_copy):
            if ranges_overlap(range1, range2):  # Use our premade check function.
                range1 = range(
                    min([range1.start, range2.start]),  # Overwrite with merged range.
                    max([range1.stop, range2.stop])
                )
                merges.append(i)

        merged_ranges.append(range1)

        # Time to delete the ranges that got merged so we don't use them again.
        # This needs to be done in reverse order so that the index doesn't move.
        for i in reversed(merges):
            del ranges_copy[i]

    return merged_ranges