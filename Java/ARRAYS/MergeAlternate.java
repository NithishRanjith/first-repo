package ARRAYS;
class MergeAlternate {

  public static String mergeAlternately(String word1, String word2) {
    StringBuilder sb = new StringBuilder();
    int n1 = word1.length(), n2 = word2.length();
    int i = 0, j = 0;
    while (i < n1 || j < n2) {
      if (i < n1)
        sb.append(word1.charAt(i++));
      if (j < n2)
        sb.append(word2.charAt(j++));
    }

    return sb.toString();

  }

  public static void main (String[] args){
    String str = mergeAlternately("abcd","pg");
    System.out.println(str);
  }
}
