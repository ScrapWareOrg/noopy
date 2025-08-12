#!/home/twinkle/venv/bin/python

import random

def generate_substitution_key(chars):
    # 文字列のリストをシャッフルして、換字表を生成
    shuffled_chars = list(chars)
    random.shuffle(shuffled_chars)
    key = dict(zip(chars, shuffled_chars))
    return key, {v: k for k, v in key.items()}

# 例
alphabet = "abcdefghijklmnopqrstuvwxyz"
key, inverse_key = generate_substitution_key(alphabet)

class strpy(str):
    def encrypt(self, key_dict):
        return "".join([key_dict.get(c, c) for c in self])

    def decrypt(self, inverse_key_dict):
        return "".join([inverse_key_dict.get(c, c) for c in self])

# 使い方
my_str = strpy("hello python")
encrypted = my_str.encrypt(key)
print(f"Encrypted: {encrypted}") # Encrypted: rzxxa tytvga
decrypted = strpy(encrypted).decrypt(inverse_key)
print(f"Decrypted: {decrypted}") # Decrypted: hello python

######################################################################
# MAIN
if __name__ == "__main__":
    print(f"[{__name__}]")
    print(__doc__)

#=====================================================================
# ALL - Make it directly accessible from the top level of the package
__all__ = ["generate_substitution_key"]

""" __DATA__

__END__ """
