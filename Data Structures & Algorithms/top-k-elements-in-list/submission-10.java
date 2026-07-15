


class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return new int[0];
        }

        



        Map<Integer, Integer> map = frequency(nums);
      

        List<Integer>[] buckets = bucketsFromMap(map, nums.length);


        int[] topRange = getTopRange(buckets, k);

        return topRange;
        
    }


    public List<Integer>[] bucketsFromMap(Map<Integer, Integer> map, int max){
        List<Integer>[] buckets = new ArrayList[max + 1];
        
        for(int key:map.keySet()){
            List<Integer> bucket = buckets[map.get(key)];

            if(bucket == null){
                bucket = new ArrayList<>();
                bucket.add(key);
                buckets[map.get(key)] = bucket;
            }else{
                buckets[map.get(key)].add(key);
            }
        }

        return buckets;
    }



    public Map<Integer, Integer> frequency(int[] nums){
        Map<Integer, Integer> map = new HashMap<>();

       
      
        for(int num:nums){
            if(!map.containsKey(num)){
                map.put(num, 1);
                
               
            }else{
                map.put(num, map.get(num) + 1);
                
               
            }
        }

        return map;
    }

    public int[] getTopRange(List<Integer>[] buckets, int k){
        int[] range = new int[k];
        int kInd = k - 1;
        for(int i = buckets.length - 1; i >= 0 && kInd > -1; i--){
            if(buckets[i] != null){
                for(int val:buckets[i]){
                    range[kInd] = val;
                    kInd--;
                }
            }
        }

        return range;
    }
    public void updateBuckets(int[] buckets, int min, int[] nums){
        for(int i = 0; i < nums.length; i++){
            buckets[nums[i] - min] += 1;
        }
    }
    
}
