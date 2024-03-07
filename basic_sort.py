
class BasicSort:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        for i in range(len(self.array)):
            index = len(self.array) - i
            for j in range(index-1):
                if self.array[j] > self.array[j+1]:
                    self._swap(j, j+1)
                
    def selection_sort(self):
        for i in range(len(self.array)):
            index = len(self.array)
            min_value_index = i 
            for j in range(i, index):
                if self.array[j] < self.array[min_value_index]:
                    min_value_index = j
            if i != min_value_index:
                self._swap(i, min_value_index)

    def insertion_sort(self):
        for i in range(len(self.array)-1):
            index = i + 1
            while (index > 0 
                    and self.array[index] < self.array[index-1]):
                self._swap(index-1, index)
                index -= 1
                

    def _swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

if __name__ == '__main__':

    test = [2, 1, 5, 3, 9, 4, 1]

    sort = BasicSort(test)

    # sort.bubble_sort()
    # sort.selection_sort()
    sort.insertion_sort()

    print(test)