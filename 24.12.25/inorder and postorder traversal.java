/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int postIndex;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        postIndex = postorder.length-1;
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0; i<inorder.length; i++){
            map.put(inorder[i],i);
        }
        return construct(inorder,postorder,0,inorder.length-1,map);
    }
    private TreeNode construct(int[] inorder,int[] postorder,int inStart,int inEnd,Map<Integer,Integer> map){
        // base case
        if(inStart > inEnd){
            return null;
        }
        int rootVal = postorder[postIndex--];
        TreeNode root = new TreeNode(rootVal);

        int rootIndex = map.get(rootVal);

        // build right subtree first
        root.right = construct(inorder,postorder,rootIndex+1,inEnd,map);
        root.left = construct(inorder,postorder,inStart,rootIndex-1,map);

        return root;
    }   
}
