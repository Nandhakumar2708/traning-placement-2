class Solution {
    public boolean isValidSerialization(String preorder) {
        Stack<String> stack = new Stack<>();
        
        for (String node : preorder.split(",")) {
            stack.push(node);
            
            /*
                A valid subtree in preorder looks like:
                node,#,#
                When we see this pattern, it represents a fully processed subtree, 
                so we can collapse it into a single #.
            */

            // Reduce completed subtrees
            while (stack.size() >= 3 &&
                   stack.get(stack.size() - 1).equals("#") &&
                   stack.get(stack.size() - 2).equals("#") &&
                   !stack.get(stack.size() - 3).equals("#")) {
                
                stack.pop(); // #
                stack.pop(); // #
                stack.pop(); // non-#
                stack.push("#");
            }
        }
        
        return stack.size() == 1 && stack.peek().equals("#");
    }
}
