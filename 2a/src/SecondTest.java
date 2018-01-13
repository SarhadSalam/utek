import java.util.ArrayList;

/**
 * Class Details:- Author: Sarhad User: sarhad Date: 13/01/18 Time : 3:45 PM Project Name: 2a Class Name: SecondTest
 */
public class SecondTest
{
	
	public static void main(String[] args)
	{
		String key = "LOLZATYOU";
		ArrayList<String> keyCombo=new ArrayList<>();
		Count c = new Count();
		for(int i=0; i<key.length(); i++)
		{
			keyCombo.add(key.substring(0,i+1));
		}
		System.out.println(keyCombo);
	}
}
