/*CS-3323-TSAA James Seymour 1277036 HW2 main driver. This program demonstrates my solutions to the programming problems presented
in the second homework assignment.
Question # 3: Computing times for the counting and averaging algorithms are both O(n). The computational time increases linearly with the
size of the data set, as the only significant work of the algorithm is stepping through the list and summing it's values. */

#include "Mylist.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

//This will be used to generate a list of random numbers
int randomNumbergen();

int main()


{
    //Instatiate a Mylist object 
    Mylist the_list = Mylist();
    
    cout << endl << "------------------------------------------------------------------------------------------------------------------" << endl;
    cout << "Creating a random list of numbers..." << endl << endl;

    //Seed the RNG for our random #'s needed during list creation
    srand(time(0));

    
    /******LIST CREATION*****/
    //Create a randomly sized list and fill it with integers from the randomNumbergen function
    for (int i = 1; i <= (randomNumbergen()/2); i++)
    {
        the_list.createNode(randomNumbergen());
    }

    //Display the random list
    cout << "Here's the random list: " << endl;
    the_list.display();
    cout << endl << "------------------------------------------------------------------------------------------------------------------" << endl;
    
    /**********Question #1**********/
    //Use the Mylist::countNodes() function to return the number of elements in the list.
    cout << "There are " << the_list.countNodes() << " elements in the list." << endl;

    /**********Question #2**********/
    //Display the average of the list using the Mylist::average() function 
    cout << "The average of the values is " << the_list.average() << endl;

    /**********Question #4**********/
    //Insert a number from the user using the Mylist::insertion(int index, int value) function
    int input1; //To get a number from user
    int input2; // "

    do{
        cout << endl << "Let's insert a number into the list." << endl;
        cout << "Please enter a valid index(1 -" << the_list.countNodes() << ") number for where you want to insert a number: " << endl;
        cin >> input1;
        cout << " and a new integer to insert: " << endl;
        cin >> input2;
    }
    while(input1 < 0 || input1 > the_list.countNodes());   //Check for valid index


    //Call the Mylist::insertion function
    the_list.insertion(input1, input2);

    //Display the list
    cout << endl << "The list is now: " << endl;
    the_list.display();
    cout << endl << "------------------------------------------------------------------------------------------------------------------" << endl;

    
    /**********Question #5**********/
    //Invoke the Mylist::del() function to delete an element chosen by the user
    do{
    cout << endl << "Let's delete an element from the list" << endl;
    cout << "Please enter a valid index((1 -" << the_list.countNodes() <<") number ofthe element you want to delete." << endl;
    cin >> input1;
    }
    while(input1 < 0 || input1 > the_list.countNodes());    //Check for valid index

    //Call the Mylist::del() function to delete the requested element
    the_list.del(input1);

    //Display the new list
    cout << endl << "The new list is: " << endl;
    the_list.display();
    cout << endl << "------------------------------------------------------------------------------------------------------------------";
    

    return 0;
}




//This function returns a reasonable random integer within the ranges set by its variables.
int randomNumbergen()
{
    //Constants used in the random list calculations to control the size of the numbers
    const int MAX_SIZE = 1000;
    const int MIN_SIZE = 100;

    int reasonable_random_integer = (rand() % (MAX_SIZE - MIN_SIZE + 1)) + MIN_SIZE;

    return reasonable_random_integer;

}


