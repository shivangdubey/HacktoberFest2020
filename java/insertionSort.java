	public static void main(String[] args) {
	
		int[] arr = { 1, 5, 2, 1, 9 };

		sort(arr);
		for (int val : arr) {
			System.out.print(val + " ");
		}

	}

	public static void sort(int[] arr) {

		for (int cnt = 1; cnt <= arr.length - 1; cnt++) {

			int temp = arr[cnt];
			int j = cnt - 1;

			while (j >= 0 && temp < arr[j]) {

				arr[j + 1] = arr[j];
				j--;
			}

			arr[j + 1] = temp;

		}

	}
