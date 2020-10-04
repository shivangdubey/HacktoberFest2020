#include <bits/stdc++.h>
using namespace std;

// A program similar to grep. It should take a pattern and a filename as input, and 
// search for that pattern in the file and return the line number and the entire line
//  matching it. If a pattern is not found, then report the same. If no file is specified, 
//  it should read from the standard input. 
//  Pattern is a string containing alphabets from A-Z and a-z.
int main(int argc, char** argv)
{
	fstream f;
	string filename, line, pattern;
	char h;
	int ln = 0, flag = 0;
	if (argc == 1)
		getline(cin, filename);
	else
		filename = argv[1];
	cin >> pattern;
	f.open(filename);
	while (!f.eof())
	{

		getline(f, line);

		ln++;
		size_t found = line.find(pattern);
		cout << "ff" << found;
		if (found != std::string ::npos)
		{

			flag = 1;
			cout << "line " << ln << " ";
			cout << line << endl;
		}
	}
	if (flag == 0)
	{
		cout << "pattern is not found" << endl;
	}
}
