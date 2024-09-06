import java.util.*;
class Frequency
{
  public static void main(String[] args){
    String str = "aravind";
    frequency_Char(str);
  }

  public static void frequency_Char(String s){

    HashMap<Character, Integer> hm = new HashMap<>();
    for (int i=0;i<s.length();i++){
      if(hm.containsKey(s.charAt(i))){
        hm.put(s.charAt(i), hm.get(s.charAt(i))+1);
      }
      else {
        hm.put(s.charAt(i),1);
      }
    }

    for(int i=0;i<s.length();i++){
      if(hm.get(s.charAt(i)) !=0){
        System.out.print(s.charAt(i));
        System.out.print(hm.get(s.charAt(i))+" ");
        hm.put(s.charAt(i),0);
      }
    }

  }
}