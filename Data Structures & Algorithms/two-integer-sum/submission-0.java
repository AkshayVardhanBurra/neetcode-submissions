class Solution {
    public int[] twoSum(int[] nums, int target) {
        // for(int i = 0; i < nums.length - 1; i++){
        //     for(int j = i + 1; j < nums.length; j++){
        //         if(nums[i] + nums[j] == target){
        //             return indexesInOrder(i, j);
        //         }
        //     }
        // }

        // int[] indexes = {-1, -1};
        // return indexes;


        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(map.containsKey(diff)){
                int[] indexes = {map.get(diff), i};
                return indexes;
                
            }else{
                map.put(nums[i], i);
            }
        }

        return new int[0];
    }


    private int[] indexesInOrder(int i, int j){
        int[] indexes = new int[2];
        if(i < j){
            indexes[0] = i;
            indexes[1] = j;
        }else{
            indexes[0] = j;
            indexes[1] = i;
        }

        return indexes;
    }
}
