#include<iostream>
#include<cstring>

using namespace std;

//check given string is palindrome or not using recursion - abcba

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

int main()
{
    string S;
    cout<<"Enter the input string: ";
    getline(cin,S);
    cout<<is_palindrome(S,0,S.length()-1);
    return 0;

}
