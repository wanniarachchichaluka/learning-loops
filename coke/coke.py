due_amnt = 50

while due_amnt >= 50:
    print(f"Amount Due: {due_amnt}")
    insrt_coin = input("Insert Coin: ")
    if insrt_coin in (5 , 10 , 25):
        due_amnt = due_amnt - insrt_coin
    else:
        continue
print(f"Change Owed: {(due_amnt - 50)}")

