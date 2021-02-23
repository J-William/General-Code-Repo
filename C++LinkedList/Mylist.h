//Mylist class header file - Integer linked list for HW 2 

#ifndef MYLIST
#define MYLIST

class Mylist
{

	private:
		//Node definition
		struct Node
		{
			int data;
			Node* next;

		};

		Node* first;	//first/head pointer
		Node* tail;		//Tail pointer

	public:
		//Constructors and Destructor
		Mylist();				//Default Constructor
		Mylist(int);			//Create an empty list of a certain size; data=0
		~Mylist();				//Destructor

		//Mutators
		void insertion(int, int);	//Insert new value(index,value)
		void del(int);			    //Delete a certain element(index)
		void createNode(int);		//Create a new node at the end of the list; assign the passed value(value)
		void setValue(int, int);    //Set or change the value at a given index(index,value)
		
		//Accessors
		bool isempty();	    //Checks for empty
		int show(int);      //Show the value at the given index
		void display();     //Display the entire list
		int countNodes();   //Return the number of nodes in a list
		int average();      //Return the average of all the elements in the list


};

#endif
