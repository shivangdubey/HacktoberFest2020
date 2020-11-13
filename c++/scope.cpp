    Difference(vector<int>v)
    {
        elements=v;
    }
    void computeDifference()
    {
        maximumDifference=0;
        for(int i; i<elements.size(); i++)
        {
            for(int j=i+1;j<elements.size();j++)
            {
                if(abs(elements[i]-elements[j])>maximumDifference)
                {
                    maximumDifference=abs(elements[i]-elements[j]);
                }
            }
        }
    }
	// Add your code here

