public class SumOfSingleElementsAppearance{

	public static void main(String... args){

		int[] nums = {1, 2, 3, 2};

		SumOfSingleElementsAppearance value = new SumOfSingleElementsAppearance();

		value.sum(nums);


	}

	public int sum(int[] numbers){

		int[] unique = new int[numbers.length];

		int sumOfSingleAppearedValues = 0;

		for(int count = 0; count < numbers.length; count++){

			for(int value = numbers.length - 1; value >= 0 ;value--){

				if(numbers[count] != numbers[value]){

					unique[count] = numbers[value];
		

				}



			}


		}


		for(int value : unique){

			System.out.print(value + " ");

			sumOfSingleAppearedValues += value;


		}

		System.out.print(sumOfSingleAppearedValues);

		return sumOfSingleAppearedValues;


	}


}