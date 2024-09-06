class MergeSort:
    def __init__(self):
        pass

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left_arr = self.merge_sort(arr[:mid])
        right_arr = self.merge_sort(arr[mid:])

        return self.merge(left_arr, right_arr)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res.extend(left[i:])
        res.extend(right[j:])

        return res

if __name__ == "__main__":
    merge_sort_test = MergeSort()
    arr = [38, 27, 43, 3, 9, 82, 10]
    result = merge_sort_test.merge_sort(arr)
    print(f"Before : {arr}")
    print(f"After : {result}")