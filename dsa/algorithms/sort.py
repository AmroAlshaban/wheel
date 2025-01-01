class InsertionSort:
    def __init__(self, array):
        self.array = array


    def __str__(self):
        return str(self._sort())

    
    def _sort(self):
        if len(self.array) in [0, 1]:
            return self.array
        
        for j in range(1, len(self.array)):
            key = self.array[j]
            i = j - 1

            while i >= 0 and self.array[i] > key:
                self.array[i + 1] = self.array[i]
                i -= 1
            
            self.array[i + 1] = key
        
        return self.array


    def view_code(self, pseudo_code=True):
        if pseudo_code == False:
            return """
                    if len(array) in [0, 1]:
                        return array
                            
                    for j in range(1, len(array)):
                        key = array[j]
                        i = j - 1

                        while i >= 0 and array[i] > key:
                            array[i + 1] = array[i]
                            i -= 1
                                
                        array[i + 1] = key
                            
                    return array
                   """
        return """
                    # We assume array indices begin at 0, and the array has at least two elements.

                    for i = 1 to length(array) - 1:
                        key = array[i]
                        j = i - 1

                        while j >= 0 and array[j] > key:
                            array[j + 1] = array[j]
                            j = j - 1
                        
                        array[j + 1] = key
               """

    def view_steps(self):
        ...


    def loop_invariant(self):
        ...


    def time_complexity(self, proof=False):
        ...



class MergeSort:
    def __init__(self, array, left_index=0, right_index=None):
        self.array = array
        self.left_index = left_index
        self.right_index = len(array) - 1 if right_index is None else right_index


    def __str__(self):
        return str(self._sort())

    
    def _merge(self, array, left_index, half_index, right_index):
        left_subarray = array[left_index:half_index + 1] + [float('inf')]
        right_subarray = array[half_index + 1:right_index + 1] + [float('inf')]

        i, j = 0, 0
        k = left_index

        while k != right_index + 1:
            if left_subarray[i] > right_subarray[j]:
                array[k] = right_subarray[j]
                j += 1
            else:
                array[k] = left_subarray[i]
                i += 1
            
            k += 1
        
        return array


    def _merge_sort(self, array, left_index, right_index):
        if left_index < right_index:
            half_index = (right_index + left_index) // 2
            self._merge_sort(array, left_index, half_index)
            self._merge_sort(array, half_index + 1, right_index)
            self._merge(array, left_index, half_index, right_index)

            return array
        
    
    def _sort(self):
        return self._merge_sort(self.array, self.left_index, self.right_index)
    

    def view_code(self, pseudo_code=True):
        if pseudo_code == False:
            return """
                    def _merge(self, array, left_index, half_index, right_index):
                        left_subarray = array[left_index:half_index + 1] + [float('inf')]
                        right_subarray = array[half_index + 1:right_index + 1] + [float('inf')]

                        i, j = 0, 0
                        k = left_index

                        while k != right_index + 1:
                            if left_subarray[i] > right_subarray[j]:
                                array[k] = right_subarray[j]
                                j += 1
                            else:
                                array[k] = left_subarray[i]
                                i += 1
                            
                            k += 1
                        
                        return array

                   """
        
        return """

                # We assume array indices begin at 0, and the array has at least two elements.

                # The Merge() function merges two subarrays into one sorted array, assuming BOTH subarrays are
                already sorted

                Merge(array, left_index, half_index, right_index):
                    left_array = array[left_index ... half_index]
                    right_array = array[half_index + 1 ... left_index]

                    left_array[half_index - left_index + 1] = +infinity
                    right_array[left_index - half_index] = +infinity

                    i = j = 0
                    k = left_index

                    while k != right_index + 1:
                            if left_array[i] > right_array[j]:
                                array[k] = right_array[j]
                                j = j + 1
                            else:
                                array[k] = left_array[i]
                                i = i + 1
                            
                            k = k + 1
                        
                        return array

               """
    

    def view_steps(self):
        ...


    def loop_invariant(self):
        ...


    def time_complexity(self, proof=False):
        ...
