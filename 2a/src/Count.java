import java.io.*;
import java.util.*;

/**
 * Class Details:- Author: Sarhad User: sarhad Date: 13/01/18 Time : 12:28 PM Project Name: 2a Class Name: count
 */
public class Count
{
	
	//Change the datasetPath
//	private static final String datasetPath = "/home/sarhad/Projects/utek/train.txt";
	
	private static ArrayList<String> list = new ArrayList<>();
	private static int count = 0;
	
	public static void main(String[] args)
	{
		try
		{
			readFile(args[0]);
			String key = "OR";
			
			for( String aList : list )
			{
				countKeys(aList, key);
			}
			
			System.out.println(list);
			
		} catch( FileNotFoundException e )
		{
			e.printStackTrace();
		}
	}
	
	//The following read each
	private static void readFile(String datasetPath) throws FileNotFoundException
	{
		Scanner x = new Scanner(new File(datasetPath));
		while( x.hasNext() )
		{
			String a = x.next();
			processData(a);
		}
	}
	
	//The below just processes the data.
	private static void processData(String s)
	{
		//Process Data. Remove <unk> N non-characters, convert to uppercase. Store data
		
		//the below regex removes characters and numbers
		
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
