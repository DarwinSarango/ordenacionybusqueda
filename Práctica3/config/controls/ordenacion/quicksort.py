class QuickSort:
    def sort_primitive_quicksort(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
            return self.sort_primitive_quicksort(left) + middle + self.sort_primitive_quicksort(right)

    def sort_models_quicksort(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = getattr(array[len(array) // 2], attribute)
            left = [x for x in array if getattr(x, attribute) < pivot]
            middle = [x for x in array if getattr(x, attribute) == pivot]
            right = [x for x in array if getattr(x, attribute) > pivot]
            return self.sort_models_quicksort(left, attribute) + middle + self.sort_models_quicksort(right, attribute)