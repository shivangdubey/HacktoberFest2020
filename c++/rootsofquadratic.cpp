#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    std::vector<double> v;
    int temp, len;

    std::cout << "Enter the number of elements ";
    std::cin >> len;
    while (v.size() < len)
    {
        std::cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());
    if (v.size() % 2 == 0)
        std::cout << std::endl << "Median = "
                  << (v[v.size()/2 - 1] + v[v.size()/2]) / 2
	          << std::endl;
    else
        std::cout << std::endl << "Median = " << v[v.size()/2]
		  << std::endl;
}
