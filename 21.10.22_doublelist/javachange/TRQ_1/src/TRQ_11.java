import java.util.Scanner;
public class TRQ_11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner s = new Scanner(System.in);
		
		int a;
		System.out.println("리스트 요소 갯수를 정해주십시오 : ");
		a=s.nextInt();
		
		String aa[]=new String[a];
		
		for(String item : aa){
			System.out.println(item);
		}
		
		
		
		
		s.close();				
	}
}