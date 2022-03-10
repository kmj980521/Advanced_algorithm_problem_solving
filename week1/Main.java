package algo1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = "";
		
		ArrayList<Integer> inputArr = new ArrayList<Integer>();
		ArrayList<Integer> outputArr = new ArrayList<Integer>();
		
		while(!(input.equals("exit")))
		{
			
			input = br.readLine();
			String intStr = input.replaceAll("[^0-9]", ""); // 넣으려는 값 
			String command = input.replaceAll("[0-9]", ""); // 수행 커맨드 
			command = command.replaceAll("\\s", "");
			
			if(command.equals("enq"))
			{
				int value = Integer.parseInt(intStr);
				inputArr.add(value);
			}
			
			else if(command.equals("deq"))
			{
				if(outputArr.size() == 0)
				{
					if(inputArr.size() == 0)
					{
						System.out.println("EMPTY");
					}
					else {
						while(inputArr.size()!=0)
						{
							int inputArrValue = inputArr.get(inputArr.size()-1);
							outputArr.add(inputArrValue);
							inputArr.remove(inputArr.size()-1);
						}
						int outputArrValue = outputArr.get(outputArr.size()-1);
						System.out.println(outputArrValue);
						outputArr.remove(outputArr.size()-1);
					}
				}
				else {
					int outputArrValue = outputArr.get(outputArr.size()-1);
					System.out.println(outputArrValue);
					outputArr.remove(outputArr.size()-1);
				}
					
			}
			//else {
			//	throw  new Exception();
			//}
			//System.out.println(intStr);
			//System.out.println(command);
			//System.out.println(intStr);
			
			//System.out.println(a);
		}
		
		//String input = br.readLine();
		//System.out.println("Hello Goorm! Your input is " + input);
	}
}
