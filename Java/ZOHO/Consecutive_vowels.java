package ZOHO;

import java.util.LinkedHashMap;
import java.util.Map.Entry;

public class Consecutive_vowels {

  public static void main(String[] args) {
    String str = "geeksforgeeks";
    System.out.println(removeVowels(str));
  }

  static String removeVowels(String str) {
    StringBuilder sb = new StringBuilder();
    LinkedHashMap<Character, Integer> hm = new LinkedHashMap<>();
    char[] ch = str.toCharArray();
    for (int i = 0; i < ch.length; i++) {
      if (hm.containsKey(ch[i])) {
        hm.put(ch[i], hm.get(ch[i]) + 1);

      }

      else {
        hm.put(ch[i], 1);
      }

    }
    
    for (Entry<Character, Integer> entry : hm.entrySet()){
      
      if(remove(entry.getKey()) == false){
        sb = sb.append(entry.getKey());

      }
      if(remove(entry.getKey()) == true && entry.getValue() == 1){
        sb = sb.append(entry.getKey());

      }

      else {
        if(remove(entry.getKey()) == true && entry.getValue() >= 2){
          continue;
        }
      }

    }
    return sb.toString();

  }

  static boolean remove(char c) {
    return (c == 'a') || (c == 'e') ||
        (c == 'i') || (c == 'o') ||
        (c == 'u');
  }

}
