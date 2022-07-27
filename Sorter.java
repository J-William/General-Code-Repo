class Sorter {
	
	// Bubble Sort
	static void bubbleSort(int array[]){
		int size = array.length;
		
		// Access loop controls the number of comparison iterations
		for (int i = 0; i < size - 1; i++) {
			
			// Flag when a swap is made
			boolean swapped = false;
			
			// Comparison loop
			for (int j = 0; j < size - i - 1; j++) {
				
				if (array[j] > array[j+1]) {
					// Swap 
					int temp = array[j];
					array[j] = array[j+1];
					array[j+1] = temp;
					swapped = true;
				}
			}
			
			// If no swapping occurred sorting is done
			if (!swapped)
				break;
		}
	}
	
	// Selection Sort
	static void selectionSort(int array[]) {
		int size = array.length;
		
		// Access loop 
		for (int i = 0; i < size -1; i++) {
			
			int minIndex = i;
			
			// Comparison loop; search for minimum
			for (int j = i + 1; j < size; j++) {
				
				if (array[j] > array[minIndex]) {
					minIndex = j;
				}
			}
			
			// Place the min in the sorted portion
			int temp = array[minIndex];
			array[minIndex] = array[i];
			array[i] = temp;
		}
	}
	
	// Insertion Sort
	static void insertionSort(int array[]) {
		int size = array.length;
		
		// Access loop
		for (int i = 1; i < size; i++) {
			int key = array[i];
			int j = i - 1;
			
			// Compare key with the elements to the left
			while (j >= 0 && key < array[j]) {
				array[j+1] = array[j];
				--j;
			}
			// Insert the value after the smaller element
			array[j+1] = key;
		}
	}
}