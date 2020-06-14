# 输入中文 进行祖安翻译
# Written by harix

inputChinese = input("输入你想要翻译的中文:")


# Dictionary set up
zuanDic = {
    '你' : '您'
}

emojiDic = {
    # 疑问词
    '吗' : '\U0001F434',
    # 动词
    '好' : '\U0001F44C',
    # 名词
    '狗' : '\U0001F436'
}


# replace the related text
for i in inputChinese:
    if i in zuanDic:
        inputChinese = inputChinese.replace(i, zuanDic.get(i))
    if i in emojiDic:
        inputChinese = inputChinese.replace(i ,emojiDic.get(i))

print(inputChinese)
