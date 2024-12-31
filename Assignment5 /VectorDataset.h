#ifndef VECTORDATASET_H
#define VECTORDATASET_H

#include<iostream>
#include<vector>
#include<fstream>
#include <limits>
#include "DataVector.h"
#include<list>
#include<utility>
using namespace std;

/*
Class representing a dataset of DataVectors
There are member functions
1)VectorDataset(int size=0):
    Intializer
2)~VectorDataset():
    Destructor
3)DataVector ithelement(int i) const:
    returns the ith element of the VectorDataset
4)int getDimension() const
    return the size of VectorDataset
5)int print()
    print the VectorDataset
6)void pushElement(const DataVector& newmem)
    Push the element into DataVector set
7)void ReadVectorDataSet(const string& filename)
    Read the csv file with name file name
*/
class VectorDataset 
{
    private:
        vector<DataVector> vectors;  // Vector to store DataVector objects

    public:
        // Constructor with an optional size parameter
        VectorDataset(int size=0)
        {
            if(size==0)
            {
                vectors={}; // If size is 0, initialize with an empty vector
            }
            else
            {
                vectors.resize(size); // Otherwise, resize the vector to the specified size
            }
            // cout <<  "Created a VectorDataSet";
        }

        // Destructor
        ~VectorDataset()
        {
            // cout << "Destroyed a VectorDataSet";
        }

        // Accessor function to get the i-th element of the dataset
        DataVector ithelement(int i) const
        {
            return vectors[i];
        }

        // Accessor function to get the dimension of the dataset
        int getDimension() const
        {
            return vectors.size();
        }

        // Accessor function to get the ith element of the dataset
        DataVector getElement(int i) const
        {
            return vectors[i];
        }

                // Function to push a new DataVector element to the dataset
        void AddData( const DataVector& newmem)
        {
            vectors.push_back(newmem);
        }

        // Function to remove a element in to the data set
        void RemoveData( const DataVector& remmem)
        {
            auto it = find(vectors.begin(),vectors.end(),remmem);
            if(it != vectors.end())
            {
                vectors.erase(it);
            }
        }
        
        auto beginptr() 
        {
            return vectors.begin();
        }

        auto endptr() 
        {
            return vectors.end();
        }

        // Function to print the dataset
        int print()
        {
            for(int i=0;i<vectors.size();i++)
            {
                vectors[i].pri();
            }
            return 0;
        }

        // Function to push a new DataVector element to the dataset
        void pushElement(const DataVector& newmem)
        {
            vectors.push_back(newmem);
        }

        // Function to read a dataset from a file
        void ReadVectorDataSet(const string& filename)
        {
            ifstream file(filename);

            // Check if the file is successfully opened
            if (!file.is_open()) 
            {
                cerr << "Error opening file: " << filename << endl;
                return;
            }

            string line;
            // Read each line from the file
            while (getline(file, line)) 
            {
                istringstream st(line);
                string value;
                DataVector dataVector;
                // Split the line into values using ',' as delimiter
                while (getline(st, value, ','))
                {
                    double doubleValue = stod(value);
                    dataVector.pushElement(doubleValue);  // Add the constructed DataVector to the dataset
                }
                vectors.push_back(dataVector);
            }

            file.close(); // Close the file after reading
        }
};

#endif