// problem link: http://www.vpropel.in/code-test/attend-pod-test/100

import java.util.*;
public class Main {
	public static void makealist(String s, ArrayList<String> al)
	{
		String str="";
		for (int i=0;i<s.length();i++)
		{
			if(s.charAt(i)!=' ')
			{
				str=str+s.charAt(i);
			}
			else
			{
				al.add(str);
				str="";
			}
		}
		al.add(str);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input=new Scanner(System.in);
		String s1=input.nextLine();
		String s2=input.nextLine();
		ArrayList<String> al1=new ArrayList<String>();
		ArrayList<String> al2=new ArrayList<String>();
		makealist(s1,al1);
		makealist(s2,al2);
		Collections.sort(al1);
		Collections.sort(al2);
		System.out.println(al1.equals(al2));
	}

}
