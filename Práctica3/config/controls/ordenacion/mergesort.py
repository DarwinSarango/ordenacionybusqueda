class MergeSort:
    def merge_primitives(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_models(self, left, right, attribute):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if getattr(left[i], attribute) < getattr(right[j], attribute):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_primitive_mergesort(self, array):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = self.sort_primitive_mergesort(array[:middle])
        right = self.sort_primitive_mergesort(array[middle:])
        return self.merge_primitives(left, right)

    def sort_models_mergesort(self, array, attribute):
        if len(array) <= 1:
            return array
        middle = len(array) // 2
        left = self.sort_models_mergesort(array[:middle], attribute)
        right = self.sort_models_mergesort(array[middle:], attribute)
        return self.merge_models(left, right, attribute)
