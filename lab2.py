def find_sum(arr, P):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == P:
                return True
            elif current_sum < P:
                left += 1
            else:
                right -= 1
    return False


arr = [3, 5, 2]
P = 10
print(find_sum(arr, P))



