block=[]
prompt = 'Se pudessevisitar um lugar do mundo, para onde você iria? '
prompt += '\npress quit to end '


while True:
    ele = input(prompt)
    if ele == 'quit':
        break
    block.append(ele)
for i in block:
    print(i.title())
