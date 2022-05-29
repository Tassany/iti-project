#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <vector>
using namespace std;



void ReadTxtWrite(char* argSend,char* argReceive){
    FILE * pFile;
    long lSize;
    char * buffer;
    size_t result;
    FILE *fp;

    fp = fopen(argReceive,"wb");
    pFile = fopen ( argSend , "rb" );
    if (pFile==NULL) {fputs ("File error",stderr); exit (1);}

    // obtain file size:
    fseek (pFile , 0 , SEEK_END);
    lSize = ftell (pFile);
    rewind (pFile);

    // allocate memory to contain the whole file:
    buffer = (char*) malloc (sizeof(char)*lSize);
    if (buffer == NULL) {fputs ("Memory error",stderr); exit (2);}

    // copy the file into the buffer:
    result = fread (buffer,1,lSize,pFile);
    if (result != lSize) {fputs ("Reading error",stderr); exit (3);}

    /* the whole file is now loaded in the memory buffer. */
    fwrite (buffer , 1, lSize, fp);
    // terminate
    fclose (pFile);
    fclose (fp);
    free (buffer);
    cout<<"Printed the data of "<<argSend<<" in "<<argReceive<<endl;

}

void printSolucao(vector<int> &sol, int arraySize)
{
  cout << endl
       << "Solucao: [ ";

  for (size_t i = 0; i < sol.size(); i++)
  {
    cout << sol[i] << " ";
  }

  cout << "]" << endl;
}

void compressLzw(vector<string> dict,char* msg){

    vector<int> code;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(msg[i] == dict[j]){
                code.push_back(j);
            }

            
        }
    }
    printSolucao(code,10);

}

int main () {
    ReadTxtWrite("test.txt","dados.txt");
    vector<string> dict;
    dict = {"A","B","R","C","D"};
    char msg[] = "ABRACADABRA";
    compressLzw(dict,msg);




    return 0;
}  