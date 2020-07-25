# %%
import random
import os

def wait_enter():
    print("press enter!")
    input()

word_list_path = "./word_list.txt"
with open(word_list_path) as f:
    word_list = [s.strip() for s in f.readlines()]

hangman_path = "./hangman.txt"
mask_path = "./mask.txt"
hangman_AA = []
mask_AA = []

with open(hangman_path) as f:
    hangman_AA = [s.rstrip() for s in f.readlines()]

with open(mask_path) as f:
    mask_AA = [s.rstrip() for s in f.readlines()]

def display_hangman(life_cnt):
    for h_line, m_line in zip(hangman_AA, mask_AA):
        d_line = []
        for h_str, m_str in zip(h_line, m_line):
            if m_str != ' ' and int(m_str) <= 6 - life_cnt:
                d_line.append(h_str)
            else:
                d_line.append(' ')
        print(''.join(d_line))

# select word
ans_word = random.choice(word_list)
#init counter
life_cnt = 6
input_chr_list = []
while True:
    os.system("clear")
    display_hangman(life_cnt)
    print()
    display = [c if c in input_chr_list else '_' for c in ans_word]
    print('='*(len(ans_word)*2-1))
    print(" ".join(display))
    print('='*(len(ans_word)*2-1))
    if set(input_chr_list) == set(ans_word):
        print("you win!")
        break

    if life_cnt == 0:
        print("You lose!!")
        print("Answer is " + ans_word)
        break
    if input_chr_list: print("already input [" + ",".join(input_chr_list) + ']')
    print("your life is " + str(life_cnt))
    print("input charactor")
    input_chr = input()
    if len(input_chr) > 1:
        print("input charactor must be single.")
        wait_enter()
        continue

    if input_chr == '_': break

    if input_chr in ans_word:
        input_chr_list.append(input_chr)
        print(input_chr+" is included!")
    else:
        life_cnt -= 1
        print(input_chr+" is not included!")


    wait_enter()

# %%
