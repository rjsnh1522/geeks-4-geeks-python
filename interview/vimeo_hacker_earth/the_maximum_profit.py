from itertools import islice


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def popular_shop_and_cost(l, r, popularity_dict):
    for i in range(l, r + 1):
        popularity_dict[i] += 1
        # shop_product_cost_dict[i] += costs_of_prod_for_each_shop[i]


def add_cost(l, r, shop_product_cost_dict, costs_of_prod_for_each_shop):
    for i in range(l, r + 1):
        shop_product_cost_dict[i] += costs_of_prod_for_each_shop[i - 1]


t = int(input())

for i in range(t):
    n_m = list(map(int, input().strip().split()))
    n = n_m[0]  # number of shops
    m = n_m[1]  # number of people
    popularity_dict = {i + 1: 0 for i in range(n)}  # dict for shop with zero visitors
    shop_product_cost_dict = {
        i + 1: 0 for i in range(n)
    }  # dict for shop with zero visitors
    costs_of_prod_for_each_shop = list(map(int, input().strip().split()))
    arr_of_visitors = {}
    for j in range(m):
        inp = input().strip()
        arr_el = list(map(int, inp.split()))
        ll = arr_el[0]
        rr = arr_el[1]
        arr_of_visitors[inp] = (rr - ll) + 1
        popular_shop_and_cost(ll, rr, popularity_dict)
    #
    k = list(map(int, input().strip()))[0]
    arr_of_visitors = {
        k: v
        for k, v in sorted(
            arr_of_visitors.items(), key=lambda item: item[1], reverse=True
        )
    }
    take_k = take(k, arr_of_visitors.items())
    for it in take_k:
        ll_rr = list(map(int, it[0].split()))
        ll = ll_rr[0]
        rr = ll_rr[1]
        add_cost(ll, rr, shop_product_cost_dict, costs_of_prod_for_each_shop)
    max_profit = sum(shop_product_cost_dict.values())
    print(max_profit)
    popu = {
        k: v
        for k, v in sorted(
            popularity_dict.items(), key=lambda item: item[1], reverse=True
        )
    }
    print(take(k, popu.items())[0][0])
