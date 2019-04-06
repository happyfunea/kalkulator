#!/glob/banner
#-*- coding:utf -8-*-
import random

def rand():
    bb = ['''
    \033[31m╭━━━━━━━━━━╮
　  ┃\033[1;32mKALKULATOR\033[31m┃
　  ╰━┳━━━━━━━━╯
\033[34m　　　╰╮
　╱▔▔▔▔▔▔╲
 ▕ ╭╮╭╮  ▕
　▏┃*┃*  ▕
　▏ ╭╮    ▏
　▏ ┃┃    ▏
　▏ ╰╯    ▏\033[0m(Author: Agung)\033[34m
　▏       ▏
　╲╱╲╱╲╱╲╱\033[0m''','''　　　
      r^つ
　　　| |┃ Author: Agung
　　　| |┃           __________
　　　|∧＿∧          
　　　( ﾟ∀゜)　　n   KALKULATOR
　　　 /　　 ￣￣(_] __________
　　　 |　　 /￣￣
　 ＿_ノ　 (
　(　 ＿＿ノ
　 ＼ ＼＼ ＼
　　 ＼ `^)､ ＼
　　　 ) /　＼ `^)''']
    randem = random.choice(bb)
    print (randem)
