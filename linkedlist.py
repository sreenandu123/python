from __future__ import print_function

class Node:

	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:

	def __init__(self):
		self.head=None

#1 Insertion at head

	def inserthead(self,data):
		new_node=Node(data)
		new_node.next=self.head
		self.head=new_node

#2 Search an item

	def search(self,data):
		temp=self.head
		count=0
		while(temp):
			count=count+1
			if(temp.data==data):
				print(data,"is found at position",count)
				return
			temp=temp.next
		print(data,"Not found in the list")

#3 delete a node	

	def delete(self,data):
		current=self.head
		prev=None
		if current.data==data:
			current=current.next
			self.head=current
			return
		while current and current.data!=data:
			prev=current
			current=current.next
		if current==None:
			print(data,"not in List. ")
			return
		if current.data==data:
			prev.next=current.next
			return

#4 Reverse the list

	def reverse(self):
		current=self.head
		prev=None
		while(current):
			next=current.next
			current.next=prev
			prev=current
			current=next
		self.head=prev

#5 Print the list

	def printdata(self):
		temp=self.head
		while(temp):
			print(temp.data,end=" ")
			temp = temp.next

#7 Insertion at end 

	def insertend(self,data):
		current=self.head
		new_node=Node(data)
		if current==None:
			current=new_node
			self.head=current
			return
		while current.next!=None:
			current=current.next
		current.next=new_node

#8 Insertion at any position

	def insertpos(self,data):
		pos=int(raw_input("Enter the position:"))
		count=1
		current=self.head
		new_node=Node(data)
		prev=None
		if pos==0:
			new_node.next=current
			self.head=new_node
			return
		while(current):
			prev=current
			current=current.next
			if(pos==count):
				new_node.next=current
				current=new_node
				prev.next=current
				return 
			count+=1
		print("Position not found")
		return

#9 Check for cycle

	def checkcycle(self):
		current=self.head
		temp=self.head.next
		while(current.next!=None):
			if temp==None or temp.next==None:
				return False
			if current==temp:
				return True
			current=current.next
			temp=temp.next.next

#10 Find the middle element in one traversal

	def findmiddle(self):
		current1=self.head
		current2=self.head
		if self.head==None:
			return
		count=1
		while(current1.next!=None):
			if count%2==0 and count!=1:
				current2=current2.next
				count+=1
			else:
				count+=1
			current1=current1.next
		print(current2.data)

l=LinkedList()

"""Example for checking cycles or loops in linked list
l.head=Node(1)
l.head.next=Node(2)
l.head.next.next=Node(3)
l.head.next.next.next=Node(4)
l.head.next.next.next.next=Node(5)
l.head.next.next.next.next.next=l.head.next
"""

while(True):
	print ("\n1. Insertion at the head")
	print ("2. Search")
	print ("3. Deletion")
	print ("4. Reverse list")
	print ("5. Print")
	print("6. Exit")
	print("7. Insert at the end")
	print("8. Insert at specific position")
	print("9. Check for Cycle")
	print("10. Find the middle element")
	print  ("Enter your choice:")

	ch=int(raw_input())
	
	if(ch==1):
		l.inserthead(int(raw_input("Enter the number for insertion:")))

	elif(ch==5):
		l.printdata()

	elif(ch==2):
		l.search(int(raw_input("Enter the number to be searched:")))

	elif(ch==3):
		l.delete(int(raw_input("Enter the number to be deleted:")))

	elif(ch==4):
		l.reverse()
		print("Reversed")
		l.printdata()

	elif(ch==6):
		print("Thank You!!!")
		exit()

	elif ch==7:
		l.insertend(int(raw_input("Enter the number to be inserted:")))

	elif ch==8:
		l.insertpos(int(raw_input("Enter the number to be inserted:")))

	elif ch==9:
		print(l.checkcycle())

	elif ch==10:
		l.findmiddle()