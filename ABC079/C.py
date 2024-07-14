A,B,C,D = input()

op_patterns = []

for i_bit in range(2**3): # オペレーターの組合せ000~111までの全8=(2^3)パターンやる
    op_pattern = []
    for n in range(3):
        op_pattern.append("+" if (i_bit >> n) & 1 else "-") #nbit分右シフトさせたところが1なら
    op_patterns.append(op_pattern)

ans = 0

