def solution(data, n):
    count_mp = {}
    size = len(data)
    complain = set()

    if n == 0:
        return None

    for i in range(size):
        if data[i] not in count_mp.keys():
            count_mp[data[i]] = 1
        else:
            count_mp[data[i]] += 1
            if count_mp[data[i]] > n:
                complain.add(data[i])
    data_new = []
    for e in data:
        if e not in complain:
            data_new.append(e)

    print(data_new)                

    return data

if __name__ == "__main__":
    data = [1, 2, 2, 3, 3, 3, 4, 5, 5] 
    n = 0
    print(solution(data, n))