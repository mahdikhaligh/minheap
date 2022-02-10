class MinHeap:
    def __init__(self):
        self.__heap = []
        self.__last_index = -1

    def push(self, value):
        self.__last_index += 1
        if self.__last_index < len(self.__heap):
            self.__heap[self.__last_index] = value
        else:
            self.__heap.append(value)
        self.__siftup(self.__last_index)

    def pop(self):
        if self.__last_index == -1:
            raise IndexError('pop from empty heap')

        min_value = self.__heap[0]

        self.__heap[0] = self.__heap[self.__last_index]
        self.__last_index -= 1
        self.__siftdown(0)

        return min_value

    def __siftup(self, index):
        while index > 0:
            parent_index, parent_value = self.__get_parent(index)

            if parent_value <= self.__heap[index]:
                break

            self.__heap[parent_index], self.__heap[index] =\
                self.__heap[index], self.__heap[parent_index]

            index = parent_index

    def __siftdown(self, index):
        while True:
            index_value = self.__heap[index]

            left_child_index, left_child_value = self.__get_left_child(index, index_value)
            right_child_index, right_child_value = self.__get_right_child(index, index_value)

            if index_value <= left_child_value and index_value <= right_child_value:
                break

            if left_child_value < right_child_value:
                new_index = left_child_index
            else:
                new_index = right_child_index

            self.__heap[new_index], self.__heap[index] =\
                self.__heap[index], self.__heap[new_index]

            index = new_index

    def __get_parent(self, index):
        if index == 0:
            return None, None

        parent_index = (index - 1) // 2

        return parent_index, self.__heap[parent_index]

    def __get_left_child(self, index, default_value):
        left_child_index = 2 * index + 1

        if left_child_index > self.__last_index:
            return None, default_value

        return left_child_index, self.__heap[left_child_index]

    def __get_right_child(self, index, default_value):
        right_child_index = 2 * index + 2

        if right_child_index > self.__last_index:
            return None, default_value

        return right_child_index, self.__heap[right_child_index]

    def __len__(self):
        return self.__last_index + 1
    
    def _index(self,key):
        try:
            return self.__heap.index(key)
        except:
            return False
    
    def getheap(self):
        for key in self.__heap:
            
            index = self._index(key)
            parent = self.__get_parent(index)
            right_child= self.__get_right_child(index,'')
            left_child = self.__get_left_child(index,'')
            print(f'{key}: parent -> {parent[1]} | left-child -> {left_child[1]} | right-child -> {right_child[1]} \n ----------------------------------')
        
        return self.__heap
    
    def parent(self,key):
        if self._index(key):
            parent = self.__get_parent(self._index(key))
            return parent
        else:
            return (None,'is not exsit')
    
    def childright(self,key):
        if self._index(key):
            childright =  self.__get_right_child(self._index(key),'')
            return childright
        else:
            return (None,'is not exsit')
    
    def childleft(self,key):
        if self._index(key):
            childleft = self.__get_left_child(self._index(key),'')
            return childleft
        else:
            return (None,'is not exsit')
    
def read_file(filename):
    list_words = []
    with open(filename,'r') as filelines:
        
        for line in filelines:
            
            for word in line.split():
                
                lword = word.lower()
                
                if lword not in list_words and len(lword) >= 3:
                    list_words.append(lword)
                    
        filelines.close()
        
    return list_words

def heappush(heap,listwords):
    
    for word in listwords:
        heap.push(word.lower())

def main():
    file = 'words.txt'
    words = read_file(file)
    heap = MinHeap()
    heappush(heap,words)
    heap.getheap()
    print(
        'MENU: \n ------------------------------',
        ' -push -> -push new-words',
        ' -pop -> pop root heap ',
        ' -parent -> -parent word',
        ' -childright -> -chright word',
        ' -childleft -> -chleft word',
        ' -heap -> show minheap tree',
        ' /help'
        ' -exit programme exit \n ------------------------------',
        sep='\n *'
    )
    
    while True:
        
        command = input('>>>').split(' ')
        
        if command[0] == '-push':
            heappush(heap,command[1:])
            heap.getheap()
            
        elif command[0] == '-pop':
            value = heap.pop()
            heap.getheap()
            print(f'remove root heap-> {value}\n')
            
        elif command[0] == '-parent':
            parent = heap.parent(command[1])
            if parent[1] is None:
                print(f'this {command[1]} is root heap tree')
            else:
                print(f'parent ({command[1]}) -> {parent[1]}')
            
        elif command[0] == '-childright':
            childright = heap.childright(command[1])
            if childright[0] is not None:
                print(f'childright ({command[1]})-> {childright[1]}')
            else:
                print(f'childright ({command[1]}) -> {childright[1]}')
        
        elif command[0] == '-childleft':
            childleft = heap.childleft(command[1])
            if childleft[0] is not None:
                print(f'childleft ({command[1]})-> {childleft[1]}')
            else:
                print(f'childleft ({command[1]}) -> {childleft[1]}')    
                
        elif  command[0] == '/help':
            print(
                '/help \n ------------------------------',
                ' -push -> -push new-words',
                ' -pop -> pop root heap ',
                ' -parent -> -parent word',
                ' -childright -> -chright word',
                ' -childleft -> -chleft word',
                ' -heap -> show minheap tree',
                ' /help',
                ' -exit programme exit \n ------------------------------',
                sep='\n *')
            continue  
        
        elif command[0] == '-heap':
            print(f'minheap : {heap.getheap()[0]}',)
        
        elif command[0] == '-exit':
            return 
        
        else:
            print('O_o Ops invalid command try again')
            continue
            
if __name__ == '__main__':
    main()
    
##########################
#######mahdi khaligh######    
##########################
