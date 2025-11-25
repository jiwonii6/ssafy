N = int(input())
text = [input() for _ in range(N)]
# 5
# GOFFA
# OYECR
# UJAUQ
# JAEZN
# WJAKC


# for i in range(N-1):
#     for j in range(N-1):
#         a = ''
#         for p in range(2):
#             for q in range(2):
#                 a += text[i+p][j+q]
#         print(a)


# 5
# 00101
# 1#101
# 00000
# 11010
# 00010

# found = True
# for i in range(N):
#     for j in range(N):
#         if text[i][j] == 'Z':
#             print('yes')
#             found = False
#             break
#     if found:
#         print('No')


flag = False

for i in range(N):
    for j in range(N):
        if text[i][j] == 'Z':
            print('yes')
            flag = True
            break

    if flag:
        break
if not flag:
        print('No')