import java.math.BigInteger;
class Solution {
    int n;
    boolean helper(String num, int st, int end1, int end2) {
        if (end2 == n - 1) return true;
        BigInteger n1 = new BigInteger(num.substring(st, end1 + 1));
        BigInteger n2 = new BigInteger(num.substring(end1 + 1, end2 + 1));
        StringBuilder sb = new StringBuilder();
         if(num.charAt(end2+1)=='0'){
            BigInteger n3 =BigInteger.ZERO;
                if (n1.add(n2).equals(n3) && helper(num, end1 + 1, end2, end2+1))
                    return true;
               return false;     
            }
         else{  
        for (int i = end2 + 1; i < n; i++) {
            sb.append(num.charAt(i));
            BigInteger n3 = new BigInteger(sb.toString());
            if (n1.add(n2).equals(n3) &&
                helper(num, end1 + 1, end2, i))
                return true;
            if(n1.add(n2).compareTo(n3) < 0) break;    
        }
        return false;
         }
    }
    public boolean isAdditiveNumber(String num) {
        n = num.length();
        if (n < 3) return false;
        if(num.charAt(0)=='0'){
            return helper(num,0,0,1);
        }
        for (int i = 0; i < n-2; i++) {
            if(num.charAt(i+1)=='0'){
                if (helper(num, 0, i,i+1))
                    return true;
                 continue;
            }
            for (int j = i + 1; j < n-1; j++) {
                if (helper(num, 0, i, j))
                    return true;
            }
        }
        return false;
    }
}
