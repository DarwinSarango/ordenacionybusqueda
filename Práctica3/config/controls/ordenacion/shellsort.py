class ShellSort:
    def sort_primitive_shellsort(self, array):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_models_shellsort(self, array, attribute):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = getattr(array[i], attribute)
                j = i
                while j >= gap and getattr(array[j - gap], attribute) > temp:
                    setattr(array[j], attribute, getattr(array[j - gap], attribute))
                    j -= gap
                setattr(array[j], attribute, temp)
            gap //= 2
        return array