class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();
        for(int i = 0; i < strs.length; i++){
            String word = strs[i];
            String key = getKey(word);
            if(map.containsKey(key)){
                map.get(key).add(word);
            }else{
                ArrayList<String> list = new ArrayList<String>();
                list.add(word);
                map.put(key, list);
            }
        }


        return  convertMapToList(map);
    }

    public List<List<String>> convertMapToList(Map<String, List<String>> map){
        List<List<String>> list = new ArrayList<>();

        for(String key:map.keySet()){
            list.add(map.get(key));
        }

        return list;
    }

    public String getKey(String str){
        int[] charCount = new int[26];

        for(char c:str.toCharArray()){
            charCount[c-'a'] += 1;
        }


        String result = "";
        for(int num:charCount){
            result += num + ",";
        }

        return result;
    }
}
