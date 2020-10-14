import java.util.Arrays;
class BubbleSort{

    // O(1) Time | O(1) Space
    public static void swap(int[] array, int i, int j){
        int temp;
        temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }

    // O(n^2) Time | O(1) space
    public static int[] sort( int[] array){
        for (int i = array.length; i >= 0 ; i--) {
            for (int j = 1; j < i; j++) {
                if (array[j - 1] > array[j]) {
                    swap(array, j, j - 1);
                }
            }
        }
        return array;
    }

    public static void main(String args[]) {
        int[] array = {8, 5, 2, 9, 5, 6, 3};
        sort(array);
        System.out.println(Arrays.toString(array));
    }
}