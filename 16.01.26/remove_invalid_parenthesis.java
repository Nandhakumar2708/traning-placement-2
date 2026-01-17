class Solution {
    Set<String> answer = new HashSet<>();

    Character OPEN = '(';
    Character CLOSE = ')';

    public List<String> removeInvalidParentheses(String s) {
        int removals = getMinimumRemovalstoMakeValid(s);

        func(0, 0, removals, 0, s, new StringBuilder(""));

        if(answer.isEmpty()) {
            return Arrays.asList("");
        }

        return new ArrayList<>(answer);
    }

    private int getMinimumRemovalstoMakeValid(String str) {
        int removals = 0;
        int open = 0;
        int close = 0;
        for(int i=0; i< str.length(); i++) {
            char c = str.charAt(i);

            if(isOpen(c)) open++;
            if(isClose(c)) close++;

            if(open < close) {
                removals++;
                close = 0;
                open = 0;
            }
        }
        removals += Math.abs(open - close);

        return removals;
    }

    private void func(int open, int close, int removals, int index, String original, StringBuilder formed) {
        if(open < close) return;

        if(index >= original.length()) {
            if(open == close) answer.add(formed.toString());
            return;
        }

        char c = original.charAt(index);

        if(!isBracket(c)) {
            formed.append(c);
            func(open, close, removals, index+1, original, formed);
            formed.deleteCharAt(formed.length() -1);
            return;
        }

        //remove bracket if removal is allowed
        if(removals > 0) {
            func(open, close, removals - 1, index+1, original, formed);
        }

        if(isOpen(c)) open++;
        if(isClose(c)) close++;

        if(open >= close){
            formed.append(c);
            func(open, close, removals, index+1, original, formed);
            formed.deleteCharAt(formed.length() -1);
        }
    }

    private boolean isBracket(char c) {
        return isOpen(c) || isClose(c);
    }

    private boolean isOpen(char c) {
        return c == OPEN;
    }

    private boolean isClose(char c) {
        return c == CLOSE;
    }
}
