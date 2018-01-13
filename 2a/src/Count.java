import java.io.*;
import java.util.*;

/**
 * Class Details:- Author: Sarhad User: sarhad Date: 13/01/18 Time : 12:28 PM Project Name: 2a Class Name: count
 */
public class Count
{
	
	private static ArrayList<String> list = new ArrayList<>();
	
	public static void main(String[] args)
	{
		try
		{
			readFile();
		} catch( FileNotFoundException e )
		{
			e.printStackTrace();
		}
	}
	
	private static void readFile() throws FileNotFoundException
	{
		//Read Your File here. Use whatever helper functions you want. Pass the data line by line to processData(String s)
		Scanner x = new Scanner(new File("/home/sarhad/Projects/utek/comp-pack/ptb.train.txt"));
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
		System.out.println(s);
	}
	
	private static void writeFile()
	{
		//Write file here after processing the data
	}
}
