import java.util.*;

class BubbleSort {

    public static int Bubble(List<Integer> nums) {

        for (int i = nums.size() - 1; i >= 0; i--)
            for (int j = 1; j <= i; j++) {
                if (nums.get(i) > nums.get(j)) {
                    int temp = nums.get(i);
                    nums.set(i, nums.get(j));
                    nums.set(j, temp);

                }
            }
        return nums.get(2);
    }

    public static void main(String[] args) {

        // List<Integer> array = new ArrayList<>();
        List<Integer> mutableList = new ArrayList<>(List.of(3, 4, -2, 11, 10, 16));
        System.out.println(Bubble(mutableList));

    }

}