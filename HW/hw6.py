def binary_search(arr, target):

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Привязать локальный проект к удалённому репозиторию
git remote add origin <https://github.com/lieyesis/-.git>

# Пример: git remote add origin https://github.com/username/my-new-repo.git
