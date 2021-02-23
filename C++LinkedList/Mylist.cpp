//Mylist implementation - A simple integer linked list with standard memeber functions 

#include <iostream>
#include "Mylist.h"

using namespace std;

//Default Constructor
Mylist::Mylist()
{
	first = NULL;
	tail = NULL;
}
//Constructor - create empty list of size elements; set data = 0
Mylist::Mylist(int size)
{
    first = NULL;
    tail = NULL;

	for(int i = 0; i< size; i++)
	{
		createNode(0);
	}

}

Mylist::~Mylist()
{
	//destructor needs to traverse list and free all pointers
	while(first!=NULL)
	{
		first = first->next;
	}
	tail = NULL;
}

bool Mylist::isempty()
{
	if(first)
		return false;
	else
		return true;
}
//Add a new node with the passed value to the end of the list
void Mylist::createNode(int num)
{
	Node* temp = new Node;
	temp->data = num;
	temp->next = NULL;

	if(isempty())
	{
		first = temp;
		tail = temp;
		temp = NULL;
	}
	else
	{
		tail->next = temp;
		tail = temp;
		temp = NULL;
	}
}
//Delete a certain element (index)
void Mylist::del(int index)
{
	Node* prevPtr = first;
	Node* posPtr = first;

	//Traverse to index -1 position
    for(int i = 1; i < (index-1); i++)
    {
    	prevPtr = prevPtr->next;
    	posPtr = posPtr->next;
    }
    //Move post ptr twice more so its in position index + 1
    posPtr = posPtr->next;
    posPtr = posPtr->next;

    //Set prevPtr(index-1).next to posPtr(index+1) to skip the del target
    prevPtr->next = posPtr;

}
//Insert a new value at a give index position
//The value is inserted after index position e.g. index = 1 new element will be the 2nd 
void Mylist::insertion(int index, int value)
{
	Node* prevPtr = first;
	Node* posPtr = first;
	Node* temp = new Node;


	//Assign the value to the new node
	temp->data = value;

	//Traverse to index -1 position
    for(int i = 1; i < index; i++)
    {
    	prevPtr = prevPtr->next;
    	posPtr = posPtr->next;
    }
    //Move post ptr once more
    posPtr = posPtr->next;

    //Insert a new node here
    temp->next = posPtr;	//Assign the new nodes.next to the post position
    prevPtr->next = temp;	//Assign previous position.next to the new node



}
//Return the value at the given index(index)
int Mylist::show(int index)
{
    Node* curPtr = first;

    for(int i = 1; i < index; i++)
    {
        curPtr = curPtr->next;

    }

    return curPtr->data;
}
//Display the entire list
void Mylist::display()
{
    Node* curPtr = first;
    while(curPtr!=NULL)
    {
        cout << curPtr->data << "\t";
        curPtr= curPtr->next;
    }
    cout << endl;
}
//Change the value of the element at the given index(index, value)
void Mylist::setValue(int index, int value)
{
    Node* curPtr = first;

    //Traverse to index
    for(int i = 1; i < index; i++)
    {
        curPtr = curPtr->next;
    }

    //Change the value
    curPtr->data = value;
}
//Traverses the list and counts the nodes
int Mylist::countNodes()
{
    Node* curPtr = first;
    int num = 0;

    while(curPtr!=NULL)
    {
        curPtr = curPtr->next;
        num++;

    }

    return num;
}
//Returns the average of all the elements in the list
int Mylist::average()
{
    Node* curPtr = first;
    int num = 0;

    while(curPtr!=NULL)
    {
        num += curPtr->data;
        curPtr = curPtr->next;
    }

    return (num/countNodes());
}
