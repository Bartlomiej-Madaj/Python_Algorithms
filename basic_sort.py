
class BasicSort:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):

        for i in range(len(self.array)):
            index = len(self.array) - i
            for j in range(1, index):
                if self.array[j-1] > self.array[j]:
                    self._swap(j-1, j)
                
        
        # for i in range(len(self.array)):
        #     index = len(self.array) - i
        #     max_value_index = 0
        #     for j in range(0, index):
        #         if self.array[j] > self.array[max_value_index]:
        #             max_value_index = j
            
        #     temp = self.array[max_value_index]
        #     self.array[max_value_index] = self.array[index-1]
        #     self.array[index-1] = temp

    def _swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp

if __name__ == '__main__':

    test = [2, 1, 5, 3, 9, 4]

    sort = BasicSort(test)

    sort.bubble_sort()

    print(test)