# Description: 最大连续子数组
# 方法：动态规划
def max_subarray_sum(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    # 从第二个元素开始遍历
    for i in range(1, len(arr)):
        # 当前元素与前面的元素之和与当前元素比较，取较大值
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

arr = [1, -2, 3, 5, -3, 2]
print("Maximum subarray sum:", max_subarray_sum(arr)) # 8

# 输出具体的子数组
def max_subarray_sum(arr):
    max_sum = arr[0]
    curr_sum = arr[0]
    start = 0
    end = 0
    for i in range(1, len(arr)):
        # 如果当前元素与前面的元素之和大于当前元素，则将当前元素加入到子数组中
        # 说明原来的子数组的和为正数
        # 能不能换成curr_sum > 0呢？
        if curr_sum + arr[i] > arr[i]:
            curr_sum += arr[i]
        # 否则，将当前元素作为子数组的第一个元素，并对start进行更新
        else:
            curr_sum = arr[i]
            start = i
        # 更新最大子数组和，以及子数组的结束位置
        if curr_sum > max_sum:
            max_sum = curr_sum
            end = i
    return max_sum, arr[start:end + 1]

arr = [1, -2, 3, 5, -3, 2]
print("Maximum subarray sum:", max_subarray_sum(arr)) # (8, [3, 5])


# 修改版
def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]

    for i, elem in enumerate(arr[1:], start=1):
        # 直接判断curr_sum是否大于0，大于与否直接反映curr_sum是否对于找到最大子数组有贡献
        if curr_sum > 0:
            curr_sum += elem
        else:
                curr_sum = arr[i]

        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [1, -2, 3, 5, -3, 2]
print("Maximum subarray sum:", max_subarray_sum(arr)) # 8