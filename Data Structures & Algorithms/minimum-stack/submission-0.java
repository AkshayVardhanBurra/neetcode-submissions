class MinStack {


    private int[] storage;
    private int end;
    public MinStack() {
        this.storage = new int[15];
        this.end = 0;
    }


    private int[] copy(int[] nums, int length){
        int[] newArr = new int[length];

        for(int i = 0; i < nums.length; i++){
            newArr[i] = nums[i];
        }

        return newArr;
    }
    
    public void push(int val) {

        if(end == storage.length){
            this.storage = copy(this.storage,(int) (storage.length * 1.5));
        }
        this.storage[end] = val;
        end++;
    }
    
    public void pop() {
        if(end == 0){
            return;
        }
        this.end--;
        this.storage[end] = 0;
    }
    
    public int top() {
        if(end == 0){
            
        }
        return this.storage[end - 1];
    }
    
    public int getMin() {
        int min = storage[0];
        for(int i = 0; i < end; i++){
            if (storage[i] < min){
                min = storage[i];
            }

        }

        return min;
    }
}
