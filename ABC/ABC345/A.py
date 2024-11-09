S = input()

ans = "Yes"

if not (S[0] == "<" and S[-1] == ">" and S[1:-1].count("=") == len(S)-2):
    ans = "No"

print(ans)