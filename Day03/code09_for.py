# for문

arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(f'{item:2.2f}')
    sum +=  item        # sum = sum + item

print('합계는', sum)
    
# 리스트 편하게 만드는 방법 
vals = [i for i in range(1,11)]
print(vals)

# continue / break
num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        #continue        # 이후의 것을 수행하지 않고 다시 for문 복귀
        break            # break 만나면 for문 탈출
    else:
        print(num, '번 수는', item, '입니다.')

