import java.util.Scanner;

public class IndexAppearnaceMatch{

	public static void main(string... args){

		Scanner scan = new Scanner(System.in);

		String[] valuesOfNumbers = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9";

		

		checkValue(valuesOfNumbers);

	}

	public Boolean checkValue(String[] numbers){

		for(int count = 0; count < numbers.length;cout++){

			int numberOfAppearance[count] = 0;

			for(int value = 0; value < numbers.length;value++){

				if(numbers.charAt(value) == numbers.charAt(count)){

					numberOfAppearance[count]++;

				}

			}

			if(numberOfAppearance(count) == count){

				return true;

			{

			else{

				return false;

			}


		}




	}

}