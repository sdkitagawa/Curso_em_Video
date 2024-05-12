'''
Nested Conditions
    - If
    - Elif
    - Else

'''

first_name = str(input("What's your first name: ")).capitalize()
if first_name == "Douglas" or first_name == "大輔" or first_name == "だいすけ" or first_name == "Daisuke":
    print("You have a great name! ヾ(＠⌒ー⌒＠)ノ")
elif first_name == "Pedro" or first_name == "José" or first_name == "Maria" or first_name == "Ana":
    print("This name is well-known name in Brazil! ( •̀ ω •́ )y")
elif first_name == "William" or first_name == "Michael" or first_name == "Hannah" or first_name == "Madison":
    print("This name is well-known name in The United States of America! ( •̀ ω •́ )y")
elif first_name == "碧" or first_name == "あお" or first_name == "Ao" or first_name == "凛" or first_name == "りん" or first_name == "Rin":
    print("This name is well-known name in Japan! ( •̀ ω •́ )y")
elif first_name == "Jade" or first_name == "緑" or first_name == "みどり" or first_name == "Midori":
    print("You have a sweet name! (^・ω・^ )")
else:
    print("Your name is pretty... Normal ～ ( ･_･)")
