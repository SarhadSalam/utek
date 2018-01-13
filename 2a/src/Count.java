import java.io.*;
import java.util.*;

/**
 * Class Details:- Author: Sarhad User: sarhad Date: 13/01/18 Time : 12:28 PM Project Name: 2a Class Name: count
 */
public class Count
{
	private static final String datasetPath = "/home/sarhad/Projects/utek/comp-pack/ptb.train.txt";
	
	private static ArrayList<String> list = new ArrayList<>();
	private static int count = 0;
	
	public static void main(String[] args)
	{
		try
		{
			readFile();
			String key = "OR";
			for( String aList : list )
			{
				countKeys(aList, key);
			}
			System.out.println(count);
			
		} catch( FileNotFoundException e )
		{
			e.printStackTrace();
		}
	}
	
	private static int countKeys(String data, String key)
	{
		if( data.length()<key.length() )
		{
			return -1;
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
		
		return count;
	}
	
	private static void readFile() throws FileNotFoundException
	{
		//Read Your File here. Use whatever helper functions you want. Pass the data line by line to processData(String s)
		
		Scanner x = new Scanner(new File(datasetPath));
		while( x.hasNext() )
		{
			String a = x.next();
			processData(a);
		}
	}
	
	private static void processData(String s)
	{
		//Process Data. Remove <unk> N non-characters, convert to uppercase. Store data
		
		//the below regex removes characters and numbers
		s = s.replaceAll("\\W<unk>\\W|^<unk>\\W|\\W<unk>$", "").replaceAll("\\WN\\W|^N\\W|\\WN$", "").replaceAll("[^\\dA-Za-z ]", "").replaceAll("\\s+", " ").replaceAll("([0-9]+)", "").toUpperCase();
		
		String S[] = s.split(" ");
		list.addAll(Arrays.asList(S));
	}
	
	private static void writeFile()
	{
		//Write file here after processing the data
	}
}
