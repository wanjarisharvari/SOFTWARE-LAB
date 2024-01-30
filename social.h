# include <stdio.h>
# include <stdlib.h>
# include <string.h>

// groups and org linked indi. member. business indi. owners, customer. business member of group


struct node {
    int id;
    char name[20];
    char date[10];
    //int links;
    char type[20];
    char content[100];
};

struct link{
    struct node parent;
    struct node* childrens;
};

struct location{
    int x;
    int y;
};

struct individual{
    struct node* common;
    char birthday[10];
};

struct group{
    struct node* common;
    struct link member[10];
    struct link memberbuss[10];
};

struct business{
    struct node* common;
    struct location* loc;
    struct link owners[10];
    struct link customers[10];
};

struct organisation{
    struct node* common;
    struct location* loc;
    struct link members[10];
};

/*this function takes as input the type of node as first argument and takes input the name date and id of the node since theese are 
common to all nodes then later depending upon the type of nodes it takes the necessary inputs from user and also creates links using
 id of the node to be linked*/
void createnode(char* , char* , char* , int);

/*this functions deletes the node by first asking the type of niode and the freeing the pointer to that node*/
void delete(char*);

/*this function search the nodes based on name type or date which is to be passed in the argument*/
void search_nodes(char*);

/*takes into input the type of node then asks for the id of the nide and printd the information of all the linked nodes*/
void one_hop(char*);

/*this take into input the id and the post content and creates the post*/
void createandpost(int ,char* );

/*takes input the substring and prints the id name and post of the node whith the same substring*/
void search_content(char*);

/*take into input first the type of node and then later the id of the nodes and prints all the content of the linked nodes*/
void linked_content(char*);

/*apart from the other function there are other helper functiontion such as the serch function for indidvidual nodes */