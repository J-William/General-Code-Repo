// Simple string reversal and palindrome tester
#include <iostream>
#include <string>

using namespace std;

int main(){

	// Input and output string variables
	string input;
	string output;
	
	// Get the string to be reversed from user
	cout << "Enter a string to reverse: " << endl;
	getline(cin, input);


	// Copy the string in reverse
	for (int i = 1; i <= input.size(); i++)
	{
		output += input[input.size()-i];
	}

	cout << output;

	// Test for palindrome
	if(input == output)
		cout << "\nThe strings are palindromes!" << endl;
	else
		cout << "\nThe strings are not palindromes." << endl;
	


	return 0;
}