#include <iostream>
#include <cstring>

using namespace std;

//check given string is palindrome or not using recursion - abcba

//Time Complexity - O(log N)

bool is_palindrome(string Str,int start,int end)
{

    //If first char and last char in string are different
    if(Str[start]!=Str[end])
    {
       return false;
    }

    //If start index greater than end or start is equal to end
    if(start>end || start==end)
    {
        return true;
    }
    return is_palindrome(Str,start+1,end-1);
}

//Main
int main()
{
    string S;
    cout<<"Enter the input string: ";
    getline(cin,S);
    int a = is_palindrome(S,0,S.length()-1);
    if(a==0)
    {
        cout<<"The given string is not a Palindrome";
    }
    else
    {
        cout<<"The given string is Palindrome";
    }
    return 0;
}
