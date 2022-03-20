package algo1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class TwoListQueue {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = "";
		
		ArrayList<Integer> inputArr = new ArrayList<Integer>();
		ArrayList<Integer> outputArr = new ArrayList<Integer>();
		
		while(!(input.equals("exit")))
		{
			
			input = br.readLine();
			String intStr = input.replaceAll("[^0-9]", ""); // 넣으려는 값 
			String command = input.replaceAll("[0-9]", ""); // 수행할 연산 명령어  
			command = command.replaceAll("\\s", ""); // 수행할 연산 명령어에서 공백을 제거 
			
			if(command.equals("enq")) //enq 명령어 
			{
				int value = Integer.parseInt(intStr); // 값을 int로 변환해서 넣어준다 
				inputArr.add(value);
			}
			
			else if(command.equals("deq")) //deq 명령어 
			{
				if(outputArr.size() == 0)
				{
					if(inputArr.size() == 0) // 옮기려는 스택과 이미 존재하는 output 스택이 비어있다면 스택이 전부 다 비어있는 것.
					{
						System.out.println("EMPTY");
					}
					else {
						while(inputArr.size()!=0) // inputArr에 값들이 남아있다면 그걸 뒤에서 부터 옮겨준다. -> 다시 처음에 들어갔던 순서대로 뒤집어진다 
						{
							int inputArrValue = inputArr.get(inputArr.size()-1); // inputArr에서 마지막에 들어간 값을 가장 먼저 넣어줌으로써 queue로 구현
							outputArr.add(inputArrValue);
							inputArr.remove(inputArr.size()-1);
						}
						int outputArrValue = outputArr.get(outputArr.size()-1); // 옮겨준 후에 값을 얻어온다 
						System.out.println(outputArrValue);
						outputArr.remove(outputArr.size()-1);
					}
				}
				else {
					int outputArrValue = outputArr.get(outputArr.size()-1); // outputArr에 값이 있었다면? 이미 옮겨준 경우이므로 그냥 추출만 한다
					System.out.println(outputArrValue);
					outputArr.remove(outputArr.size()-1);
				}
					
			}
			
		}
	}

}
//동작 방식 
/*
0. 기본적으로 2개의 스택을 사용하고 inputArr는 1차적으로 값을 넣어줄 리스트, outputArr은 2차적으로 값을 뒤집고 그것을 pop할 때 사용할 리스트이다. 
1. 한 줄씩 입력받으면 command(수행할 연산 명령어)와 value(넣으려는 값)을 분리해준다
2. enq 명령어일 때는 inputArr에 add 해줌으로써 뒤에 붙인다(스택)
3-1. deq 명령어일 때 outputArr에 값이 없고, inputArr에도 값이 없다면 스택 전부에 비었다는 것이므로 EMPTY를 출력한다 
3-2. deq 명령어일 때 outputArr에 값이 없고, inputArr에 값이 존재한다면 inputArr 뒤(마지막으로 들어온 값)부터 outputArr로 옮겨줌으로써 다시 순서를 뒤집어 먼저 들어온 것이 먼저 나가는 qeueue를 구현한다
4. 그러나 outputArr에 값이 존재하며 바로 pop만 해준다. 그 이유는 값이 존재함에도 불구하고 다시 값을 넣어준다면 순서가 꼬여 queue를 올바르게 구현할 수 없기 때문이다.
*/

//수행시간 분석
/*
1. 각각의 명령어에 대해 비교를 하는 경우 O(1). n개의 입력이 있으므로 n
2. 비교 후 값을 경우에 따라 값을 이동하는 경우 최대 n번의 이동이 일어난다 
3. 모든 값이 push와 pop되는 경우 push는 n번, pop도 n번 일어난다. 
4. 위의 경우를 합쳤을 때 4n이며 push와 pop은 O(1)을 가지기 때문에 총 시간 복잡도는 O(n)이다.
*/