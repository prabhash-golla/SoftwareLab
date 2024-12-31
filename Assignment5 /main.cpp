#include  "TreeIndex.h"
#include <bits/stdc++.h>
using namespace std;


int main()
{
    VectorDataset train;
    train.ReadVectorDataSet("fmnist-train.csv"); //reading the train fmnist 
    VectorDataset test;
    test.ReadVectorDataSet("fmnist-test.csv"); //reading the test fmnist
    int k;
    cout << "Enter the value of k : ";
    cin >> k; // taking k as input from user.
    int p;
    cout << "Enter the number of first n elements you need to find knearestpoints(max:10001) : ";
    cin >> p;
    priority_queue<pair<double,int>> neighbors;
    TreeIndex::assignData(train);
    KDTreeIndex KDTree = KDTreeIndex::GetInstance();
    KDTree.assignIndex();
    KDTreeIndex* tree = KDTree.MakeTree();
    DataVector b= test.getElement(0);
    cout << 2 << endl;
    neighbors = tree->Search(b,5,neighbors);
    cout << neighbors.size() << endl;
    cout << 3 << endl;
    while(!neighbors.empty())
    {
        cout << "Index : " << neighbors.top().second << endl ;
        train.getElement(neighbors.top().second).pri();
        cout << "Distance : " << neighbors.top().first << endl;
        neighbors.pop();
    }
    
    return 0;
}