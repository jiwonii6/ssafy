# N= int(input())

# for tc in range(N):
#     input()
#     print(f'#{tc+1}')
word_list = input().split() #리스트는 그냥 이렇게만 해도 됨
num_sort = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
sort_word = []

for num in num_sort:
    for word in word_list:
        if word == num:
            sort_word.append(word)


    

result= ' '.join(sort_word)

            

print(result)

                



