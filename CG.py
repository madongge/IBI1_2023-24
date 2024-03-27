def calculate_gc_content(dna_sequence):
    """
    计算DNA序列的GC含量
    参数：
        dna_sequence：DNA序列（字符串）
    返回值：
        GC含量的百分比（float）
    """
    gc_count = 0
    total_bases = 0

    for base in dna_sequence:
        if base in ['G', 'C']:
            gc_count += 1
        total_bases += 1

    if total_bases == 0:
        return 0  # 避免除以零错误

    gc_content = (gc_count / total_bases) * 100
    return gc_content

def main():
    # 获取用户输入的DNA序列
    dna_sequence = input("请输入DNA序列: ").upper()

    # 检查DNA序列的有效性
    valid_bases = set('ATGC')
    if set(dna_sequence) <= valid_bases:
        # 计算DNA序列的GC含量
        gc_content = calculate_gc_content(dna_sequence)
        print("DNA序列的GC含量：", gc_content)
    else:
        print("输入的序列包含无效的碱基，请确保输入的是有效的DNA序列。")

if __name__ == "__main__":
    main()
