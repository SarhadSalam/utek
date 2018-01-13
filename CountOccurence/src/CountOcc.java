
public class CountOcc {

	static int countKeys(String data, String key){
		if(data.length() < key.length()){
			return -1;
		}
		int count = 0;
		for(int i = 0; i<(data.length()-key.length()+1);i++){
			if(data.charAt(i) == key.charAt(0)){
				boolean flag = true;
				for(int j =0; j<key.length();j++){
					if(data.charAt(i+j) == key.charAt(j)){
						continue;
					}else{
						flag = false;
						break;
					}
				}
				if(flag){
					count+=1;
				}
			}
		}
		
		
		
		return count;
	}
	public static void main(String[] args) {
		System.out.println(countKeys("Hello", "lo"));
	}

}
