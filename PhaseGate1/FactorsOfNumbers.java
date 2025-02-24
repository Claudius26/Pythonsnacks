public class FactorsOfNumbers{

	public int factorsOfNumbers(int number){

		for(int count = 1;count <= number;count++){

			if(number % count == 0){

				System.out.print(count + " ");

			}


		}

		return number;


	}

	public static void main(String... args){

		int value = 24;

		FactorsOfNumbers num = new FactorsOfNumbers();

		num. factorsOfNumbers(value);

	}



}