#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<limits>
#include<sstream>
#include<list>
#include<chrono>
#include "DataVector.h"
#include "VectorDataset.h"
using namespace std;

//The function which finds the distance of all the DataVectors in Data and the DataVector Vect.
//It also makes a pair of distance and DataVector in Data and store in thr vector listpair.
//partial_sort the listpair with respect to the distance from DataVector Vect.
VectorDataset knearestNeighborSearch( VectorDataset& Data, DataVector & Vect,int k)
{
    int dim = Data.getDimension();
    vector<pair<double,int>> listpair(dim);
    for(int i=0;i<dim;i++)
    {
        listpair.push_back(make_pair(Vect.dist(Data.ithelement(i)), i));
    }
    // sort(listpair.begin(), listpair.end());
    partial_sort(listpair.begin(), listpair.begin() + k, listpair.end());
    VectorDataset Result;
    for(int i=0;i<k;i++)
    { 
        Result.pushElement(Data.getElement(listpair[i].second));
    }
    return Result;
}

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
    int dim = test.getDimension(); // to reduce multipul call of same function in the loop
    dim=min(dim,p);
    VectorDataset knear[dim];
    auto start_time = chrono::high_resolution_clock::now(); //find the start time of the function
    for(int i=0;i<dim;i++)
    {
        knear[i] = knearestNeighborSearch(train, test.ithelement(i),k);
        cout << i << " ";
        // knear.print();
    }
    auto end_time = chrono::high_resolution_clock::now(); //find the end time of the function
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time); //find the diffrence in start and end time of function
    cout << "Time taken: " << duration.count() << " milliseconds" << endl; //printing the run time of function
    return 0;
}

// Time taken: 503273 milliseconds(with print statements for k = 50)
// 83.8788333 minutes