class Node:
    
    #Construktor untuk bua node baru 
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    
    # Construktor untuk buat circular linked list nya
    def __init__(self):
        self.head = None
    
    #Fungsi untuk memasukan node di awal
    #Circular lenked list
    def push (self, data):
        ptr1 = Node(data)
        temp = self.head
        
        ptr1.next = self.head
        
        #kalau linked list tidak kosong maka set menjadi 
        #node terakhir
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next 
            temp.next = ptr1
        else:
            ptr1.next = ptr1 # for the first node
        self.head = ptr1
            
    # Fungsi untuk print nodes sebagai circvular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print ("%d" % temp.data),
                temp = temp.next
                if (temp == self.head):
                    break                     

# Inisialisasi list kosongnya
cllist = CircularLinkedList()

#Hasil akhir linkedlist akan menjadi 5->2->12->9
cllist.push(9)
cllist.push(12)
cllist.push(2)
cllist.push(5)

print ("\nIsi dari Circular Linked List nya adalah")
print ()
cllist.printList()