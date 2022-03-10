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
			String intStr = input.replaceAll("[^0-9]", ""); // �������� �� 
			String command = input.replaceAll("[0-9]", ""); // ������ ���� ��ɾ�  
			command = command.replaceAll("\\s", ""); // ������ ���� ��ɾ�� ������ ���� 
			
			if(command.equals("enq")) //enq ��ɾ� 
			{
				int value = Integer.parseInt(intStr); // ���� int�� ��ȯ�ؼ� �־��ش� 
				inputArr.add(value);
			}
			
			else if(command.equals("deq")) //deq ��ɾ� 
			{
				if(outputArr.size() == 0)
				{
					if(inputArr.size() == 0) // �ű���� ���ð� �̹� �����ϴ� output ������ ����ִٸ� ������ ���� �� ����ִ� ��.
					{
						System.out.println("EMPTY");
					}
					else {
						while(inputArr.size()!=0) // inputArr�� ������ �����ִٸ� �װ� �ڿ��� ���� �Ű��ش�. -> �ٽ� ó���� ���� ������� ���������� 
						{
							int inputArrValue = inputArr.get(inputArr.size()-1); // inputArr���� �������� �� ���� ���� ���� �־������ν� queue�� ����
							outputArr.add(inputArrValue);
							inputArr.remove(inputArr.size()-1);
						}
						int outputArrValue = outputArr.get(outputArr.size()-1); // �Ű��� �Ŀ� ���� ���´� 
						System.out.println(outputArrValue);
						outputArr.remove(outputArr.size()-1);
					}
				}
				else {
					int outputArrValue = outputArr.get(outputArr.size()-1); // outputArr�� ���� �־��ٸ�? �̹� �Ű��� ����̹Ƿ� �׳� ���⸸ �Ѵ�
					System.out.println(outputArrValue);
					outputArr.remove(outputArr.size()-1);
				}
					
			}
			
		}
	}

}
//���� ��� 
/*
0. �⺻������ 2���� ������ ����ϰ� inputArr�� 1�������� ���� �־��� ����Ʈ, outputArr�� 2�������� ���� ������ �װ��� pop�� �� ����� ����Ʈ�̴�. 
1. �� �پ� �Է¹����� command(������ ���� ��ɾ�)�� value(�������� ��)�� �и����ش�
2. enq ��ɾ��� ���� inputArr�� add �������ν� �ڿ� ���δ�(����)
3-1. deq ��ɾ��� �� outputArr�� ���� ����, inputArr���� ���� ���ٸ� ���� ���ο� ����ٴ� ���̹Ƿ� EMPTY�� ����Ѵ� 
3-2. deq ��ɾ��� �� outputArr�� ���� ����, inputArr�� ���� �����Ѵٸ� inputArr ��(���������� ���� ��)���� outputArr�� �Ű������ν� �ٽ� ������ ������ ���� ���� ���� ���� ������ qeueue�� �����Ѵ�

4. �׷��� outputArr�� ���� �����ϸ� �ٷ� pop�� ���ش�. �� ������ ���� �����Կ��� �ұ��ϰ� �ٽ� ���� �־��شٸ� ������ ���� queue�� �ùٸ��� ������ �� ���� �����̴�.
*/

//����ð� �м�
/*
1. ������ ��ɾ ���� �񱳸� �ϴ� ��� O(1). n���� �Է��� �����Ƿ� n
2. �� �� ���� ��쿡 ���� ���� �̵��ϴ� ��� �ִ� n���� �̵��� �Ͼ�� 
3. ��� ���� push�� pop�Ǵ� ��� push�� n��, pop�� n�� �Ͼ��. 
4. ���� ��츦 ������ �� 4n�̸� push�� pop�� O(1)�� ������ ������ �� �ð� ���⵵�� O(n)�̴�.
*/