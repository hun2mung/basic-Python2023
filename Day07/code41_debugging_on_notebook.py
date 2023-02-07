# %% [markdown]
# # 주피터 노트북 사용법 학습
# ## 마크다운, 파이선 쉘을 추가 : 단축키
# - 현재 쉘 앞에 쉘 추가 : a
# - 현재 쉘 뒤에 쉘 추가 : b
# - 현재 쉘을 마크다운으로 변경 : 포커스 없는 상태에서 m
# - 현재 쉘을 파이썬으로 변경 : 포커스 없는 상태에서 y

# %%
# 최초 작성된 Python 쉘

# %% [markdown]
# ## 파이썬 쉘 실행
# - 쉘 실행 : Ctrl + Enter
# - 쉘 실행, 다음 쉘 이동(다음 쉘 없으면 생성) : Shift + Enter 
# - 쉘 실행, 다음 쉘 생성 : Alt + Enter
# - 주석 처리 : Ctrl + kc, Ctrl + /

# %%
print('Hello, Jupyter!!')

# print('Hello, Jupyter!!')

# %% [markdown]
# ## 디버깅!!
# 아무리 강조해도 지나치지 않습니다. 

# %%
arr = [1, '2', True, 'Hello', 3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# ### 함수 디버깅

# %%
def plus(x, y):
    val = x+y
    return val

def div(x, y):
    val = x / y
    return val

print('더하기')
print(plus(10, 4))

# %%
print('나누기')
print(div(10,1))

# %%
print(arr)
arr


