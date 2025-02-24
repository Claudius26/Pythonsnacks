public class TargetSum{

	public static void main(String... args){

	int[] nums = {3, 2, 4};

	 TargetSum val = new  TargetSum();

	val.returnIndexSum(nums);


	}

	public int[] returnIndexSum(int[] num){

		int target = 6;

		int[] values = new int[2];

		for(int count = 0; count < num.length;count++){

			for(int value = 0; value < num.length;value++){

				if(num[value] + num[count] == target){
				
				values[count] = value;

				values[count] = count;

				}	

			}
	

		}

		for(int count : values){

			System.out.print(count + " ");

		}

		return values;
	}


}