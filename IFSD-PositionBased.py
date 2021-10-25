class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PosBased:
    def __init__(self):
        self.cursor = None
        self.used = self.cursor

    '''
    Counting how many data on the linkedlist
    from the cursoru untill last of list
    '''
    def counters(self):
        temp = self.used
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    ''' 
    Make the linkedlist self.used that used for sign of choosing file
    to make the linkedlist cursor to the first again
    '''
    def resets(self):
        self.used = self.cursor

    '''
    Add data to linkedlist
    '''
    def appends(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.cursor is None:
            self.cursor = x
            self.used = x
        else:
            self.tail.next = x
        self.tail = x

    ''' Cursor Goes to first again '''
    def first(self):
        PosBased.resets(self)
        PosBased.showed(self)

    ''' Cursor Go to the end of list linkedlist '''
    def last(self):
        count = PosBased.counters(self)

        for i in range(count - 1):
            self.used = self.used.next

        PosBased.showed(self)

    ''' Checking if on after cursor there's a data '''
    def hasNext(self):
        count = PosBased.counters(self)

        if count > 1:
            return True
        else:
            return False

    '''Move the cursor to next data on the linkedlist'''
    def next(self):
        if PosBased.hasNext(self):
            self.used = self.used.next
            PosBased.showed(self)
        else:
            PosBased.showed(self)
            print(f"\033[1;31;40m!!Tidak Ada File Setelahnya!!\033[0;37;48m")

    ''' Checking if on behind the cursor there's a data '''
    def hasPrev(self):
        if self.cursor == self.used:
            return False
        else:
            return True

    '''Move the cursor to the data behind the cursor on the linkedlist'''
    def prev(self):
        if PosBased.hasPrev(self):
            temp = self.used

            PosBased.resets(self)
            while self.used:
                self.used = self.used.next
                if self.used.next == temp:
                    break
            PosBased.showed(self)
        else:
            PosBased.showed(self)
            print(f"\033[1;31;40m!!Tidak Ada File Sebelumnya!!\033[0;37;48m")

    ''' Show where's the cursor at on the linkedlist'''
    def showed(self):
        temp = self.cursor
        while temp:
            if temp.data == self.used.data:
                print(f"\033[1;32;40m{self.used.data} <- \033[0;37;48m")
            else:
                print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    folder = ['Pic.jpg', 'Photo.jpg', 'Data1.png', 'Tugas.docx',
              'Sound.mp3', 'Voice.mp3', 'Game.exe', 'Tugas.py',
              'Video.mp4', 'Song.mp3', 'bomb.exe', 'server.cmd',
              'Files.pdf', 'Food.png', 'script.js', 'style.css',
              'Shrek.gif', 'Tugas.docx', 'index.html', 'main.php']

    Li = PosBased()
    for i in folder:
        Li.appends(i)

    while True:
        print('\n\033[0;37;48m======================')
        print('Control with number :')
        print('1. First File')
        print('2. Last File')
        print('3. Next')
        print('4. Prev')
        print('5. Showed')
        print('Type any key to exit')
        print("======================\n")

        inps = input("type here : ")

        if inps == '1':
            Li.first()
        elif inps == '2':
            Li.last()
        elif inps == '3':
            Li.next()
        elif inps == '4':
            Li.prev()
        elif inps == '5':
            Li.showed()
        else:
            print('!Exit From Folder!')
            break
