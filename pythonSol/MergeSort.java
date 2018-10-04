import java.util.Arrays;

public class MergeSort {
	
	
	public static void mergesort(int[] arr) {
		int[] temp = new int[arr.length];
		mergesort(arr, temp , 0, arr.length-1);
	}
	
	public static void mergesort(int[] arr, int[] temp, int leftStart, int rightEnd) {
		if(leftStart >= rightEnd) {
			return;
		}
		
		int middle = (leftStart + rightEnd)/2;
		
		mergesort(arr, temp, leftStart, middle);
		mergesort(arr, temp, middle+1, rightEnd);
		mergeHalves(arr,temp, leftStart,rightEnd);
	}
	
	
	public static void mergeHalves(int[] arr, int[] temp, int leftStart, int rightEnd) {
		int leftIndex = leftStart;
		int leftEnd = (leftStart+rightEnd)/2;
		int rightIndex = leftEnd + 1;
		int tempIndex = leftStart;
		int size  =  rightEnd - leftStart + 1;
		
		while(leftIndex <= leftEnd && rightIndex <= rightEnd) {
			if(arr[leftIndex] <= arr[rightIndex]) {
				temp[tempIndex] = arr[leftIndex];
				leftIndex += 1;
			}
			else {
				temp[tempIndex] = arr[rightIndex];
				rightIndex += 1;
			}
			tempIndex += 1;  
		}
		
		System.arraycopy(arr, leftIndex, temp, tempIndex, leftEnd - leftIndex + 1);
		System.arraycopy(arr, rightIndex, temp, tempIndex, rightEnd - rightIndex + 1);
		System.arraycopy(temp, leftStart, arr, leftStart, size);	
	}
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] test = new int[] {5,2,34,12,52,23,2,3,3,100,50};
		
		mergesort(test);
		System.out.println(Arrays.toString(test));

	}
}
