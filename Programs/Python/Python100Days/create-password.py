import random


def generate_code(code_len=6, use_symbols=False):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认6个字符)
    :param use_symbols: 是否使用符号字符(默认不使用)

    :return: 由大小写英文字母数字和符号构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_symbols = '~!@#$^&*-_=+|'
    if use_symbols == True:
        all_chars += all_symbols
    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

def main():
    len = int(input('Password length = '))
    sym = bool(input('Use symbols (y/n): ').lower() == 'y')
    password = generate_code(len, sym)
    print(password)

if __name__ == '__main__':
    main()
    