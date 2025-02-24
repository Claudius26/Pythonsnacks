public class SmallestIndex{

	public static void main(String... args){

		int[] nums = {2, 4, 5, 8, 19, 89,56};

		SmallestIndex number = new SmallestIndex();

		number.getSmallestIndex(nums);

	}

	public int getSmallestIndex(int[] number){

		int largest = number[0];

		int smallestIndex = 0;

		for(int count: number){

			if(count > largest){

				largest = count;

			}

		}


		for(int count = 0; count < number.length;count++){

			if(number[count] == largest){

				smallestIndex = count;

			}

		}

		System.out.print(smallestIndex);

		return smallestIndex;


	}





}