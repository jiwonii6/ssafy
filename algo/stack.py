# T= int(input())

# for tc in range(T):

#     arr = list(input())
#     word_list = []
#     par = 0
#     for word in arr:
#         if word == '(' or word == '{':
#             word_list.append(word)

#         if word == ')' :
#             if word_list and word_list[-1] == '(':
#                 word_list.pop()
#             else:
#                 par += 1


#         if  word == '}':
#             if word_list and word_list[-1] == '{':
#                 word_list.pop()
#             else:
#                 par += 1
            


    
#     if len(word_list) == 0 and par == 0:
#         print(f'#{tc+1} 1')
#     else:
#         print(f'#{tc+1} 0')


T= int(input())

for tc in range(T):

    arr = list(input())
    word_list = []
    flag = True
    for word in arr:
        if word == '(' or word == '{':
            word_list.append(word)

        if word == ')' :
            if word_list and word_list[-1] == '(':
                word_list.pop()
            else:
                flag = False


        if  word == '}':
            if word_list and word_list[-1] == '{':
                word_list.pop()
            else:
                flag= False 
            

    print(word_list)
    
    if flag and len(word_list) == 0:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')