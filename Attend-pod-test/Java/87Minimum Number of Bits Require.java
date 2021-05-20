// problem link: http://www.vpropel.in/code-test/attend-pod-test/87

import java.util.*;
import java.lang.*;
public class Main
{
  public static void main(String[] args)
  {
    Scanner input=new Scanner(System.in);
    int n=input.nextInt();
    long arr[]=new long[n];
    for (int i=0;i<n;i++)
    {
      arr[i]=input.nextLong();
    }
    long max=0;
    for (int i=0;i<n;i++)
    {
      max=(long)Math.max(max,arr[i]);
    }
    int count=0;
    while((long)Math.pow(2,count)<max)
    {
      count++;
    }
    System.out.println(count);
  }
}
