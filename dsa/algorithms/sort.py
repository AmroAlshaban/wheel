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



class MergeSort:
    ...