public class PrimeNumber{

	public boolean isNumberPrime(int number){

		for(int count = 1;count <= number;count++){

			if(number % count == 0 ){

				System.out.print(true);

				return true;
			}

			else{

			return false;		
			
			}

			

		}

		


		

	}

	public static void main(String... args){

		int value = 9;

		PrimeNumber numbers = new PrimeNumber();

		 numbers.isNumberPrime(value);
		


	}



}