

import java.util.Scanner;

public class Fixedbudget 
{
     Scanner sc=new Scanner(System.in);
     static int sum=0;static int price;
public void seller()
{
     System.out.println("available items in our mart");
     System.out.println("1.Electronics");
     System.out.println("2.Cloths");
     System.out.println("3.Bath");
     System.out.println("4.kitchen");
     System.out.println("enter required section");
     int sec=sc.nextInt();
     if(sec<=4)
     {
     switch(sec)
     {
     case 1:
          System.out.println("you choosed electronics");
          System.out.println("the avaible items are");
          System.out.println("1.refridgerator");
          System.out.println("2.rice cooker");
          System.out.println("3.television");
          System.out.println("4.washing machine");
          System.out.println("enter required item");
          int i=sc.nextInt();
          if(i==1)
          {
              System.out.println("the item is refridgerator");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=300;
              System.out.println("cost of one refrigerator:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else if(i==2)
          {
              System.out.println("the item is rice cooker");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=250;
              System.out.println("cost of one rice cooker:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(i==3)
          {
              System.out.println("the item is television");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=400;
              System.out.println("cost of one television:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(i==4)
          {
              System.out.println("the item is washing machine");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=150;
              System.out.println("cost of one washing machine:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else
          {
              System.out.println("you entered unavailable item");
          }
          break;
     case 2:
          System.out.println("you choose clothes");
          System.out.println("the available items are");
          System.out.println("1.womens wear");
          System.out.println("2.mens wear");
          System.out.println("3.childrens wear");
          System.out.println("4.party wear");
          System.out.println("enter required item");
          int j=sc.nextInt();
          if(j==1)
          {
              System.out.println("the items are womens wear");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=300;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else if(j==2)
          {
              System.out.println("the items are mens wear");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=250;
              System.out.println("cost of one itemr:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(j==3)
          {
              System.out.println("the items are children wear");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=400;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(j==4)
          {
              System.out.println("the items are party wear");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=150;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else
          {
              System.out.println("you entered unavailable item");
          }
          break;
     case 3:
          System.out.println("you choosed Bath");
          System.out.println("the avaible items are");
          System.out.println("1.Soaps");
          System.out.println("2.Shampoos");
          System.out.println("3.Conditioners");
          System.out.println("4.hair conditioners");
          System.out.println("enter required item");
          int k=sc.nextInt();
          if(k==1)
          {
              System.out.println("the item is Soaps");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=300;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
                   System.out.println("again start your shopping");
              
              sum+=price;
          }
          else if(k==2)
          {
              System.out.println("the item is Shampoos");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=250;
              System.out.println("cost of one itemr:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(k==3)
          {
              System.out.println("the item is Conditioners");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=400;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(k==4)
          {
              System.out.println("the item is Hair conditioners");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=150;
              System.out.println("cost of one item:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              if(price>5000)
              {
                   System.out.println("again start your shopping");
              }
              sum+=price;
          }
          else
          {
              System.out.println("you entered unavailable item");
          }
          break;
     case 4:
          System.out.println("you choosed kitchen");
          System.out.println("the avaible items are");
          System.out.println("1.rice");
          System.out.println("2.oils");
          System.out.println("3.vegetables");
          System.out.println("4.spices");
          System.out.println("enter required item");
          int l=sc.nextInt();
          if(l==1)
          {
              System.out.println("the item is rice");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=300;
              System.out.println("cost of one rice bag:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else if(l==2)
          {
              System.out.println("the item is  oils");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=250;
              System.out.println("cost of one oil packet:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }else if(l==3)
          {
              System.out.println("the item is vegetables");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=400;
              System.out.println("cost of vegetables:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              if(price>5000)
              {
                   System.out.println("again start your shopping");
              }
              sum+=price;
          }else if(l==4)
          {
              System.out.println("the item is spices");
              int Totalquantity=200;
              System.out.println("available items are:"+Totalquantity);
              System.out.println("enter required quantity of items");
              int req=sc.nextInt();
              int cost=150;
              System.out.println("cost of spices:"+cost);
              int price=cost*req;
              System.out.println("price:"+price);
              
              sum+=price;
          }
          else
          {
              System.out.println("you entered unavailable item");
          }
          break;
          default:
              System.out.println("choosed valid item from menu");
     }
     }
     
          System.out.println("total bill is:"+sum);
          if(sum>5000)
          {
          System.out.println("start again");
          System.out.println("it is more than your budget");
          seller();
     }
     
     
     
     System.out.println("would like to purchase more items:yes/no");
     String r="yes";
     String y=sc.next();
     if(y.equals(r))
     {
          seller();
     }
     else {
          System.out.println("happy shopping");
     }
     }

public static void main(String[] args) {
     Menu m=new Menu();
     m.seller();
}

}
