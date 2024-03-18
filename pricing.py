def pricing(order):
    dict_burgers = {'Chicken Wrap':7.50,'Ayam Gunting':6.50,'Jumbo Sausage':5.50}
    p = 0
    qtt = []
    if ("," in order):
        each_order = order.split(", ")
    else: each_order = [order]

    for i in range(len(each_order)):
        qtt.append(int(each_order[i][-1]))
        temp = each_order[i][:-3]
        each_order[i] = temp
    
    for i in range(len(qtt)):
        p += dict_burgers[each_order[i]]*qtt[i]
    
    return p