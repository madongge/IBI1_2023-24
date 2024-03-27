def dna_to_mrna(dna_sequence):
    """
    将DNA序列转换为mRNA序列
    参数：
        dna_sequence：DNA序列（字符串）
    返回值：
        mRNA序列（字符串）
    """
    # 检查DNA序列是否只包含ATGC
    valid_bases = set('ATGC')
    if not set(dna_sequence) <= valid_bases:
        raise ValueError("输入的序列包含无效的碱基，请确保输入的是有效的DNA序列。")

    # 定义DNA到mRNA的转换规则
    transcription_rule = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

    # 转换DNA序列为mRNA序列
    mrna_sequence = ''
    for base in dna_sequence:
        mrna_sequence += transcription_rule.get(base, base)

    return mrna_sequence

def main():
    # 获取用户输入的DNA序列
    dna_sequence = input("请输入DNA序列: ").upper()

    try:
        # 将DNA序列转换为mRNA序列
        mrna_sequence = dna_to_mrna(dna_sequence)
        print("对应的mRNA序列：", mrna_sequence)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

