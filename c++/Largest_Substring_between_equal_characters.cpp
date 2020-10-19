/*
Question: Given a string s, return the length of the longest substring between two equal characters,
excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.
*/

#include<bits/stdc++.h>
using namespace std;

int maxLengthBetweenEqualCharacters(string s){
    int ans = -1;
    for(int i=0;i<s.length();i++){
        for(int j=s.length()-1;j>i;j--){
            if(i==j) continue; //Not considering same index.
            if(s[i]==s[j]){
                string tmp = s.substr(i, j-i+1); //Substring for comparison.
                int len = tmp.length()-2;
                ans = max(len, ans); //Maximum length substring
                break;
            }
        }
    }
    return ans;
}

int main(){
    string s;
    cin>>s;
    cout<<maxLengthBetweenEqualCharacters(s);
}