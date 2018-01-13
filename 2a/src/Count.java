import java.io.*;
import java.util.*;

/**
 * Class Details:- Author: Sarhad User: sarhad Date: 13/01/18 Time : 12:28 PM Project Name: 2a Class Name: count
 */
public class Count
{
	
	//Change the datasetPath
	
	
	//private static final String datasetPath = "/home/sarhad/Projects/utek/2a/2a.in";
	
	
	private static int count = 0;
	private static boolean keyWatcher=false;
	public static String key;
	
	public static void main(String[] args)
	{
		try
		{
			
			readFile(args[0]);
			readFile(args[1]);
			
			
		} catch( FileNotFoundException e )
		{
			e.printStackTrace();
		}
	}
	
	//The following read each
	private static void readFile(String datasetPath) throws FileNotFoundException
	{
		Scanner x = new Scanner(new File(datasetPath));
		ArrayList<String> list = new ArrayList<>();
		
		while( x.hasNextLine() )
		{
			String a = x.nextLine();
			list = getCountOfLine(list, a);
		}
	}
	
	private static ArrayList<String> getCountOfLine(ArrayList<String> list, String a)
	{
		for(int i=0; i<a.split(" ").length; i++)
		{
			list = processData(a.split(" ")[i], list);
		}
		for(String s: list)
		{
			countKeys(s,key);
		}
		key=null;
		keyWatcher=false;
		list = new ArrayList<>();
		System.out.println(count);
		count=0;
		return list;
	}
	
	//The below just processes the data.
	private static ArrayList<String> processData(String s, ArrayList<String> list)
	{
		//Process Data. Remove <unk> N non-characters, convert to uppercase. Store data
		
		//the below regex removes characters and numbers
		
		if(s.equals("|"))
		{
			keyWatcher = true;
		}
		if(!keyWatcher)
		{
			s = s.replaceAll("[^\\dA-Za-z ]", "").replaceAll("\\s+", "").replaceAll("([0-9]+)", "");
			s = s.replaceAll("\\s*\\bN\\b\\s*", "");
			s = s.replaceAll("\\s*\\bunk\\b\\s*", "");
			s = s.toUpperCase();
			if( !s.isEmpty() )
			{
				String S[] = s.split(" ");
				list.addAll(Arrays.asList(S));
			}
		}
		if(keyWatcher)
		{
			s = s.replaceAll("[^\\dA-Za-z ]", "").replaceAll("\\s+", "").replaceAll("([0-9]+)", "");
			s = s.replaceAll("\\s*\\bN\\b\\s*", "");
			s = s.replaceAll("\\s*\\bunk\\b\\s*", "");
			s = s.toUpperCase();
			key=s;
		}
		return list;
	}
	
	private static void countKeys(String data, String key)
	{
		if( data.length()<key.length() )
		{
			return;
		}
		
		for( int i = 0; i<( data.length()-key.length()+1 ); i++ )
		{
			if( data.charAt(i) == key.charAt(0) )
			{
				boolean flag = true;
				for( int j = 0; j<key.length(); j++ )
				{
					if( data.charAt(i+j) == key.charAt(j) )
					{
						continue;
					} else
					{
						flag = false;
						break;
					}
				}
				if( flag )
				{
					count += 1;
				}
			}
		}
		
		
	}
}
