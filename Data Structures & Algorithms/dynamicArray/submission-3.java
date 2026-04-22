class DynamicArray {
    int[] array;
    int size = 0;
    public DynamicArray(int capacity) {
        this.array = new int[capacity];
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (getSize() == getCapacity()) {
            resize();
        }
        this.array[getSize()] = n;
        size++;
    }

    public int popback() {
        int poppedValue = this.array[getSize() - 1];
        set( getSize() - 1, 0);
        size--;
        return poppedValue;
    }

    private void resize() {
        int[] newArray = new int[this.array.length * 2];
        System.arraycopy(this.array, 0, newArray, 0, this.array.length);
        this.array = newArray;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.array.length;
    }
}
