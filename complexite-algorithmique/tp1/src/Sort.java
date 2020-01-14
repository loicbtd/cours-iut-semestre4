public class Sort {

    public static void main(String args[]) {

        float launchTime;
        float finishTime;
        int[] array;

        launchTime = System.currentTimeMillis();
        array = new int[(int)Math.pow(10,2)];

        sort_bubble(array);
        sort_selection(array);

        finishTime = System.currentTimeMillis();

        System.out.println("Duration : " + (finishTime-launchTime));
    }


    public static void sort_bubble(int[] array) {
        boolean sorted = false;
        int temp;
        while(!sorted) {
            sorted = true;
            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] > array[i+1]) {
                    temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                    sorted = false;
                }
            }
        }
    }

    public static void sort_selection(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int min = array[i];
            int minId = i;
            for (int j = i+1; j < array.length; j++) {
                if (array[j] < min) {
                    min = array[j];
                    minId = j;
                }
            }
            // swapping
            int temp = array[i];
            array[i] = min;
            array[minId] = temp;
        }
    }
}