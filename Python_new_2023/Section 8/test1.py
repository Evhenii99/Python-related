run = True
head = 0
heads = []

while run:
    user_entered = input("Throw the coin and enter head or tail here: ?")
    heads.append(user_entered)
    heads_count = heads.count("head")
    count_all_list = len(heads)
    result = heads_count / count_all_list * 100
    print(f"Heads: {result}%")
