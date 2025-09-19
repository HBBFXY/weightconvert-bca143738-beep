# 重量转换程序：千克(kg)与磅(pd)之间的转换
# 转换公式：1千克 = 2.2046磅

# 获取用户输入
weight_input = input().strip()

# 提取数值和单位
try:
    # 查找单位的起始位置
    if 'kg' in weight_input:
        value = float(weight_input.replace('kg', ''))
        unit = 'kg'
    elif 'pd' in weight_input:
        value = float(weight_input.replace('pd', ''))
        unit = 'pd'
    else:
        raise ValueError("单位不正确，请使用kg或pd")
    
    # 进行单位转换
    if unit == 'kg':
        converted = value * 2.2046
        print(f"对应的英制重量为{converted:.3f}磅")
    else:  # unit == 'pd'
        converted = value *0.4535
        print(f"对应的公制重量为{converted:.3f}公斤")
        
except ValueError as e:
    print(f"输入错误: {e}")# 在这个文件下编写代码，题目具体要求见README.md文件
