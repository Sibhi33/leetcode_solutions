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

public class Solution
{
    // Step 0 : List to store pairs of depth and node values
    private LinkedList<int[]> nodeList = new LinkedList<>();

    public TreeNode recoverFromPreorder(String S)
    {
        // Step 1: Parse the input string to extract depth and value pairs
        parseInput(S);
        if (nodeList.isEmpty())
        {
            return null;
        }
        
        // Step 2: Construct the binary tree using DFS
        TreeNode root = new TreeNode(nodeList.removeFirst()[1]);
        buildTree(root, 0);
        
        return root;
    }

    private void buildTree(TreeNode parent, int depth)
    {
        // Step 3 : Check and assign the left child
        if (!nodeList.isEmpty() && nodeList.peekFirst()[0] == depth + 1)
        {
            TreeNode leftChild = new TreeNode(nodeList.removeFirst()[1]);
            parent.left = leftChild;
            buildTree(leftChild, depth + 1);
        }
        
        // Step 4 : Check and assign the right child
        if (!nodeList.isEmpty() && nodeList.peekFirst()[0] == depth + 1)
        {
            TreeNode rightChild = new TreeNode(nodeList.removeFirst()[1]);
            parent.right = rightChild;
            buildTree(rightChild, depth + 1);
        }
    }

    private void parseInput(String S)
    {
        int i = 0;
        while (i < S.length())
        {
            int depth = 0;
        
            // Step 5 : Count the number of dashes to determine depth
            while (i < S.length() && S.charAt(i) == '-')
            {
                depth++;
                i++;
            }
            int value = 0;
            
            // Step 6 : Extract the node's value
            while (i < S.length() && Character.isDigit(S.charAt(i)))
            {
                value = value * 10 + (S.charAt(i) - '0');
                i++;
            }
            
            // Step 7 : Add the pair (depth, value) to the list
            nodeList.add(new int[]{depth, value});
        }
    }
}
