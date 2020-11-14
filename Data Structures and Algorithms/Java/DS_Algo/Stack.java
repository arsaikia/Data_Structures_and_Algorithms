import java.util.Arrays;

class Stack{

	static int[] nums;

    public static int[] myStackPush(int type, int value){
    	if(type == 1){
            int[] newNums;
            int i;
            for ( i = 0; i < nums.length; i++) {
                newNums[i] = nums[i];
            }
            newNums[i] = value;
    	}



    }

    public static void main(String[] args) {

        if (args[0].equals("push")) {
        	myStackPush(1, Integer.parseInt(args[0])) 
        }
        else if(args[0].equals("print")){
            System.out.println(Arrays.toString(nums));
        }
    }



}