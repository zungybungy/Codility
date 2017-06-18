#include <iostream>
using namespace std;


template<class T>
class Node
{
public:
	Node();
	Node(const T& item, Node<T>* ptrnext = NULL);
	T data;
	// access to the next node
	Node<T>* NextNode();
	// list modification methods
	void InsertAfter(Node<T>* p);
	Node<T>* DeleteAfter();
	Node<T> * GetNode(const T& item, Node<T>* nextptr = NULL);
private:

	Node<T> * next;
};

template<class T>
Node<T>::Node()
{
	// default constructor
	// this is to allow us to create an object without any initialization

}


//  This constructor is just to set next pointer of a node and the data contained.
template<class T>
Node<T>::Node(const T& item, Node<T>* ptrnext)
{
	this->data = item;
	this->next = ptrnext;
}

template<class T>
Node<T>*Node<T>::NextNode()
{
	return this->next;
}

//  This methods inserts a node just after the node that the method belongs to 
//  TO-DO: Consider a better implementation
template<class T>
void Node<T>::InsertAfter(Node<T> *p)
{
	// not to lose the rest of the list, we ought to link the rest of the
	// list to the Node<T>* p first
	p->next = this->next;

	// now we should link the previous Node to Node<T> *p , i.e the Node that we are 
	//inserting after,
	this->next = p;
}

// Deletes the node from the list and returns the deleted node
template<class T>
Node<T>* Node<T>::DeleteAfter()
{
	// store the next Node in a temporary Node
	Node<T>* tempNode = next;
	// check if there is a next node
	if (next != NULL)
		next = next->next;

	return tempNode;
}
template<class T>
Node<T> * GetNode(const T& item, Node<T>* nextptr = NULL)
{
	Node<T>* newnode; // Local ptr for new node
	newnode = new Node<T>(item, nextptr);
	if (newnode == NULL)
	{
		cerr << "Memory allocation failed." << endl;
		exit(1);
	}
	return newnode;
}

int main()
{
	Node<char> *p, *q, *r;
	// Link the nodes with each other
	q = new Node<char>('B'); // here nxtptr is passed by a nullptr by default
	p = new Node<char>('A', q);
	r = new Node<char>('C');

	// modify the list
	q->InsertAfter(r);
	/*
	Call the InsertAfter method that belongs to the object pointed by q, as
	paramater, pass to it the address contained in r.
	*/

	cout << "p:" << p->data << endl;                 // "A" will be printed out
	cout << "p_next:" << p->NextNode()->data << endl;  // "B" will be printed out
	cout << "q:" << q->data << endl;                 // "B" will be printed out
	cout << "q_next:" << q->NextNode()->data << endl;  // "C" will be printed out
	cout << "r:" << r->data << endl;                 // "C" will be printed out

	p = p->NextNode(); // p now points to the node coming after the node it was
					   // previously pointing to.
	cout << endl;
	cout << "p:" << p->data << endl;                 // "B" will be printed out

	r = q->DeleteAfter();        // copy to r the address of the node pointed by
								 //the node pointed by the node pointed by q, and remove that node from the list

	Node<char> *head;
	head = GetNode('A', GetNode('B', GetNode('C')));
	/*
	Here above method, creates a list which has nodes having data A,B,C and each
	node pointing to the next one respectively.
	*/
	delete q;
	delete p;
	delete r;
	return 0;
}