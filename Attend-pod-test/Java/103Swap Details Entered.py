// problem link:http://www.vpropel.in/code-test/attend-pod-test/103

public class Main {
    public static void main(String args[]) {
      Scanner input=new Scanner(System.in);
      String s1=input.next();
      String s2=input.next();
      String str1="",str2="";
      for (int i=0;i<s1.length();i++)
      {
          if(s1.charAt(i)==':')
          {
              str1=str1+"#";
          }
          else
          {
              str1=str1+s1.charAt(i);
          }
      }
      for (int i=0;i<s2.length();i++)
      {
          if(s2.charAt(i)=='#')
          {
              str2=str2+":";
          }
          else
          {
              str2=str2+s2.charAt(i);
          }
      }
      System.out.println(s2);
      System.out.println(s1);
    }
}
