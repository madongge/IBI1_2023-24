def count_repeats(seq, repeat_patterns):
    total_repeats = 0
    for pattern in repeat_patterns:
        start = 0
        while True:
            start = seq.find(pattern, start)
            if start == -1:
                break
            total_repeats += 1
            start += 1
    return total_repeats

seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
repeat_patterns = ['GTGTGT', 'GTCTGT']

total_repeats = count_repeats(seq, repeat_patterns)
print("Total number of repeat elements:", total_repeats)
