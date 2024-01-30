# include <stdio.h>
# include <stdlib.h>
# include "social.h"
# include <string.h>

int uni=0;
struct node universal[50];
int ind =0;
struct individual ind_arr[50];
int grp =0;
struct group grp_arr[50];
int buss=0;
struct business buss_arr[50];
int org=0;
struct organisation org_arr[50];
int nm;
int nb;
int nc;
int no;
int nms;


struct node* search(int id){
        for(int i=0 ; i<uni ; i++){
                if(universal[i].id==id) {
                printf("%s ",universal[i].name);
                struct node * x = &universal[i];
                return x;
               // break;
        }
}
//return NULL;
}

struct individual* search_indi(int id){
        for(int i=0 ; i<ind ; i++){
                if( ind_arr[i].common->id==id ) {
                printf("%s ",ind_arr[i].common->name);
                struct individual * x = &ind_arr[i];
                return x;
        }
}
//return NULL;
}

struct group* search_grp(int id){
        for(int i=0 ; i<grp ; i++){
                if( grp_arr[i].common->id==id ) {
                printf("%s ",grp_arr[i].common->name);
                struct group * x = &grp_arr[i];
                return x;
        }
}
//return NULL;
}

struct organisation* search_org(int id){
        for(int i=0 ; i<org ; i++){
                if( org_arr[i].common->id==id ) {
                printf("%s ",org_arr[i].common->name);
                struct organisation * x = &org_arr[i];
                return x;
        }
}
//return NULL;
}

struct business* search_buss(int id){
        for(int i=0 ; i<buss ; i++){
                if( buss_arr[i].common->id==id ) {
                printf("%s ",buss_arr[i].common->name);
                struct business * x = &buss_arr[i];
                return x;
        }
}
//return NULL;
}

  

void createnode(char* arr, char* name, char date[10], int id){
       // struct node n;
        struct node* newnode; //= &n ;
        newnode = (struct node*) malloc(sizeof(struct node));
        newnode->id=id;
        strcpy(newnode->name, name);
        strcpy(newnode->date , date);
        strcpy(newnode->content, NULL);
        strcpy(newnode->type, arr);

        if(arr=="individual"){
                //struct individual node_ind;
                struct individual* node;// = &node_ind;
                node = (struct individual*) malloc(sizeof(struct individual));   
                node->common = newnode;
                printf("enter birth-date: ");
                char bd[10];
                scanf("%s",bd);
                //node.birthday=bd;
                ind_arr[ind++] = *node ;
                //return n;
        }


        else if(arr=="group"){
                //struct group node_grp;
                struct group* node;// = &node_grp;
                node = (struct group*) malloc(sizeof(struct group)); 
                node->common = newnode;

                printf("enter the number of individuals to link: ");
                //const int nm;
                scanf("%d",&nm);
                for(int i=0 ; i<nm ; i++){

                        node->member[i].parent=*newnode;
                        printf("enter the id of individual node: ");
                        int id;
                        scanf("%d",&id);    
                        node->member[i].childrens= search(id) ;
                } 

                printf("enter the number of business members to link: ");
                //const int nb;
                scanf("%d",&nb);
                for(int i=0 ; i<nb ; i++){
                         
                        node->member[i].parent=*newnode;
                        printf("enter the id of individual business node: ");
                        int id;
                        scanf("%d",&id);    
                        node->member[i].childrens= search(id); 
                }
                grp_arr[grp++] = *node;
                //return n;      
        }


        else if(arr=="business"){
                //struct business node_buss;
                struct business* node; // = &node_buss;
                node = (struct business*) malloc(sizeof(struct business)); 
                node->common = newnode;
                printf("enter location");
                int x;
                scanf("%d",&x);
                node->loc->x=x;
                int y;
                scanf("%d",&y);
                node->loc->y=y;
                printf("enter the number of customers: ");
                //int nc;
                scanf("%d",&nc);
                for(int i=0; i<nc ;i++){
                        
                        node->customers[i].parent = *newnode;
                        printf("enter the id of the individual customer :");
                        int id;
                        scanf("%d",&id);
                        node->customers[i].childrens = search(id) ;
                }

                printf("enter the number of owners: ");
                //const int no;
                scanf("%d",&no);
                for(int i=0 ; i<no ; i++){
                        node->owners[i].parent = *newnode;
                        printf("enter the id of the owner: ");
                        int id;
                        scanf("%d",&id);
                        node->owners[i].childrens = search(id);

                }

                buss_arr[buss++] = *node;
                //return n;
        }


        else /*(arr=="organisation")*/{
                //struct organisation node_org;
                struct organisation* node;// = & node_org;
                node = (struct organisation*) malloc(sizeof(struct organisation)); 
                node->common = newnode;  
                printf("enter location");
                int x;
                scanf("%d",&x);
                node->loc->x;
                int y;
                scanf("%d",&y);
                node->loc->y;
                printf("enter the number of members : ");
                //const int nm;
                scanf("%d",&nms);
                for(int i=0 ; i<nms ; i++){
                        node->members[i].parent = *newnode ; 
                        printf("enter the id of the members: ");
                        int id;
                        scanf("%d",&id);
                        node->members[i].childrens = search(id);
                }

                org_arr[org++]= *node;
                //return n;

        }
        //return newnode;
        universal[uni++] = *newnode ;
}

void delete(char arr[]){
        if (arr=="individual"){
                printf("enter id of the node: ");
                int id;
                scanf("%d",&id);
                free(search_indi(id));
        }
        else if(arr="group"){
                printf("enter id of the node: ");
                int id;
                scanf("%d",&id);
                free(search_grp(id));
        }
        else if(arr="business"){
                printf("enter id of the node: ");
                int id;
                scanf("%d",&id);
                free(search_buss(id));
        }
        else{
                printf("enter id of the node: ");
                int id;
                scanf("%d",&id);
                free(search_org(id));
        }
}

void search_nodes(char arr[]){
        if(arr=="name"){
                char name_[10];
                scanf("%s",name_);
                int n=0;
                struct node a[100];
                for(int i=0 ; i<uni ; i++){
                        if(universal[i].name=="name_"){
                                a[n++]=universal[i];
                                printf("%s ",universal[i].name);
                                printf("%d ",universal[i].id);
                                printf("\n");

                        }
                }

                //return(a);
        }

        if(arr=="type"){
                char type_[10];
                scanf("%s",type_);
                int n=0;
                struct node a[100];
                for(int i =0 ; i<uni ; i++){
                        if(universal[i].type=="type_"){
                                a[n++]=universal[i];
                                printf("%d ",universal[i].id);
                                printf("%s ",universal[i].name);
                                printf("\n");
                                
                        }
                }
        }

        if(arr=="birthday"){
                char bday_[10];
                scanf("%s",bday_);
                int n=0;
                struct individual a[100];
                for(int i =0 ; i<ind ; i++){
                        if(ind_arr[i].birthday=="bday_"){
                                a[n++]=ind_arr[i];
                                printf("%d ",ind_arr[i].common->id);
                                printf("%s ",ind_arr[i].common->name);
                                printf("\n");
                                
                        }
                }
        }

}


void one_hop(char type[]){
        if(type =="group"){
                //nm nb
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == grp_arr[i].common->id){
                                for (int j=0 ; j< nm  ; j++){
                                        printf("%s ",grp_arr[i].member[j].childrens->name);
                                        printf("%d ",grp_arr[i].member[j].childrens->id);
                                        printf("\n");
                                }
                                for (int k=0 ; k< nb  ; k++){
                                        printf("%s ",grp_arr[i].memberbuss[k].childrens->name);
                                        printf("%d ",grp_arr[i].memberbuss[k].childrens->id);
                                        printf("\n");
                                }


                        }
                }
        }

        if(type=="business"){
                //nc no
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == buss_arr[i].common->id){
                                for (int j=0 ; j< nc  ; j++){
                                        printf("%s ",buss_arr[i].customers[j].childrens->name);
                                        printf("%d ",buss_arr[i].customers[j].childrens->id);
                                        printf("\n");
                                }
                                for (int k=0 ; k< no  ; k++){
                                        printf("%s ",buss_arr[i].owners[k].childrens->name);
                                        printf("%d ",buss_arr[i].owners[k].childrens->id);
                                        printf("\n");
                                }


                        }
                }

        }

        if(type=="organisation "){
                //nms
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == org_arr[i].common->id){
                                for (int j=0 ; j< nms  ; j++){
                                        printf("%s ",org_arr[i].members[j].childrens->name);
                                        printf("%d ",org_arr[i].members[j].childrens->id);
                                        printf("\n");
                                }
                        }

        }
        }

}

void createandpost(int id, char arr[]){
        for(int i=0 ; i<uni ; i++){
                if(universal[i].id==id){
                        strcpy(universal[i].content,arr);
                }
        }

        printf("%s",arr);
}

void search_content(char arr[]){
        for (int i=0 ; i<uni ; i++){
                if(strstr(universal[i].content,arr)!= NULL){
                        printf("%s ",universal[i].name);
                        printf("%s ",universal[i].id);
                        printf("%s ",universal[i].content);
                        printf("\n");
                }
        }
}

void linked_content(char type[]){
        if(type =="group"){
                //nm nb
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == grp_arr[i].common->id){
                                for (int j=0 ; j< nm  ; j++){
                                        printf("%s ",grp_arr[i].member[j].childrens->name);
                                        printf("%d ",grp_arr[i].member[j].childrens->id);
                                        printf("%s ",grp_arr[i].member[j].childrens->content);
                                        printf("\n");
                                }
                                for (int k=0 ; k< nb  ; k++){
                                        printf("%s ",grp_arr[i].memberbuss[k].childrens->name);
                                        printf("%d ",grp_arr[i].memberbuss[k].childrens->id);
                                        printf("%s ",grp_arr[i].memberbuss[k].childrens->content);
                                        printf("\n");
                                }
                        }
                }
        }

        if(type=="business"){
                //nc no
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == buss_arr[i].common->id){
                                for (int j=0 ; j< nc  ; j++){
                                        printf("%s ",buss_arr[i].customers[j].childrens->name);
                                        printf("%d ",buss_arr[i].customers[j].childrens->id);
                                        printf("%s ",buss_arr[i].customers[j].childrens->content);
                                        printf("\n");
                                }
                                for (int k=0 ; k< no  ; k++){
                                        printf("%s ",buss_arr[i].owners[k].childrens->name);
                                        printf("%d ",buss_arr[i].owners[k].childrens->id);
                                        printf("%s ",buss_arr[i].owners[k].childrens->content);
                                        printf("\n");
                                }
                        }
                }

        }

        if(type=="organisation "){
                //nms
                int id;
                scanf("%d",&id);
                for(int i=0 ; i<grp ; i++){
                        if(id == org_arr[i].common->id){
                                for (int j=0 ; j< nms  ; j++){
                                        printf("%s ",org_arr[i].members[j].childrens->name);
                                        printf("%d ",org_arr[i].members[j].childrens->id);
                                        printf("%s ",org_arr[i].members[j].childrens->content);
                                        printf("\n");
                                }
                        }

                }
        }

}
 

void disply(struct node* node){
        printf("%s ",node->name);
        printf("%d",node->id);
        if(node->content ==NULL) printf("it is empty");
        else printf("%s", node->content);
}

int main(){

        //createnode("individual" , "sharvari" ,19/07/90,786);
        printf("1. create node\n2. delete node \n3. search for nodes using name type or birthday\n");
        printf("4. printing linked nodes\n 5. create content\n 6.search for content given substring\n ");
        printf("\n7. print thr content of all the linked nodes \n8. print the contents");
        int num;
        printf("\nto perform above functions make atleat 1 node");        
        printf("\nenter the number: ");
        scanf("%d",&num);
        while(num = (1||2||3||4||5||6)){
                if(num==1){
                        char type[10];
                        printf("\ntype :");
                        scanf("%s",type);
                        char name[10];
                        printf("\nname :");
                        scanf("%s",name);
                        char date[10];
                        printf("\nenter creation date: ");
                        scanf("%s",date);
                        int id;
                        printf("\n enter the id :");
                        scanf("%d",&id);
                        createnode(type,name,date,id);
                }

                if(num==2){
                        char type[10];
                        printf("\nenter the type of the node :");
                        scanf("%s",type);
                        delete(type);
                }

                if(num ==3){
                        printf("enter to search by type birthday or name");
                        char search[10];
                        search_nodes(search);
                }

                if(num ==4){
                      printf("\n enter the type of node :");
                      char type[10];
                      scanf("%s",type);  
                      one_hop(type);
                }

                if(num == 5){
                        int id;
                        printf("\nenter the id");
                        scanf("%d",&id);
                        char arr[50];
                        printf("\nenter the content post :");
                        scanf("%s",arr);
                        createandpost(id,arr);
                        
                }
                if(num ==6 ){
                        printf("\n search for the substring to be searchedd :");
                        char arr[50];
                        scanf("%s",arr);
                        search_content(arr);
                }

                if(num==7){
                        printf("\n search for the content of all the linked nodes :");
                        char arr[50];
                        scanf("%s",arr);
                        linked_content(arr);
                }

                if(num==8){

                }
                else break;


                printf("enter the number: ");
                scanf("%d",&num);
        }
         
        return 0;
}