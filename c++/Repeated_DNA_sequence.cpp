/*
Question: All DNA is composed of a series of nucleotides abbreviated as
'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA,
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to print all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule.
*/

#include<bits/stdc++.h>
using namespace std;

void repeatedDNASequence(string s){
    if(s.length()<10) return;
    unordered_map<string, int> m;
    vector<string> res;
    
    // Maintaing occuence of each substring.
    for(int i=0;(i+10)<=s.length();i++){
        string tmp = s.substr(i, 10);
        m[tmp]++;
    }

    // If the substring has more than one count, we add it to our result.
    for(auto e: m){
        if(e.second > 1){
            res.push_back(e.first);
        }
    }
    
    // Printing the result
    for(string e: res){
        cout<<e<<" ";
    }
}

int main(){
    string s;
    cin>>s;
    repeatedDNASequence(s);
}