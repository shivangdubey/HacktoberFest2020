public static void main(String[] args) {

		int[] arr = { 10, 20, 30, 40, 10 };

		quickSort(arr, 0, arr.length - 1);

		for (int val : arr) {
			System.out.print(val + " ");
		}
	}
  public static void quickSort(int[] arr, int lo, int hi) {

		if (lo >= hi) {
			return;
		}

		int mid = (lo + hi) / 2;

		int pivot = arr[mid];

		// partitioning
		int left = lo;
		int right = hi;

		while (left <= right) {

			// left problem
			while (arr[left] < pivot) {
				left++;
			}

			// right problem
			while (arr[right] > pivot) {
				right--;
			}

			// problem solve

			if (left <= right) {
				int temp = arr[left];
				arr[left] = arr[right];
				arr[right] = temp;

				left++;
				right--;
			}

		}
		// partitioning completed

		// smaller parts sort
		quickSort(arr, lo, right);
		quickSort(arr, left, hi);

	}
