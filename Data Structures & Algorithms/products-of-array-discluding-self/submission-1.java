class Solution {
    public int[] productExceptSelf(int[] nums) {

        int indexOfZero = indexOf(0, nums);

        int totalProduct = getProduct(nums,indexOfZero);

        int[] resultArray = generateEmpty(totalProduct, nums.length, indexOfZero);
        System.out.print(Arrays.toString(resultArray));
        divideArray(resultArray, nums);

        return resultArray;

    }

    public void divideArray(int[] resultArray, int[] nums){
        for(int i = 0; i < resultArray.length; i++){
            if(nums[i] != 0){
                resultArray[i] /= nums[i];
            }
        }
    }


    public int indexOf(int val, int[] nums){
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == val){
                return i;
            }
        }

        return -1;
    }

    public int getProduct(int[] nums, int indexOfZero){
        int product = 1;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0 && indexOfZero != i){
                product = 0;
                break;
            }else{
                product *= nums[i] == 0 ? 1:nums[i];
            }
        }

        return product;
    }

    public int[] generateEmpty(int num, int length, int indexOfZero){

        
        int[] emptyArr = new int[length];

        if(indexOfZero == -1){
            for(int i = 0; i < length; i++){
                emptyArr[i] = num;
            }
        }else{
            emptyArr[indexOfZero] = num;
        }

        return emptyArr;
    }
}  
