class DynamicArray {

    private int capacity;
    private int[] arr;
    private int length;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.arr = new int[capacity];

    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (length == capacity) {
            resize();
        }
        arr[length] = n;
        length++;
    }

    public int popback() {
        if (length > 0) {
            length--;
        }
        return arr[length];
    }

    private void resize() {
        capacity *= 2;
        arr = Arrays.copyOf(arr, capacity);
    }

    public int getSize() {
        return length;
    }

    public int getCapacity() {
        return capacity;
    }
}
