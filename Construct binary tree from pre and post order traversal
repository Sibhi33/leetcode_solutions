class Solution {
    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        int[] index = new int[]{0};
        return construct(preorder, postorder, index, 0, preorder.length - 1);
    }
    private TreeNode construct(int[] preorder, int[] postorder, int[] index, int l, int h){
        if(index[0] >= preorder.length || l > h)
            return null;

        TreeNode root = new TreeNode(preorder[index[0]++]);
        if(l == h) return root;

        int i;
        for(i = l; i <= h; i++){
            if(postorder[i] == preorder[index[0]]) break;
        }
        if(l <= h){
            root.left = construct(preorder, postorder, index, l, i);
            root.right = construct(preorder, postorder, index, i + 1, h - 1);
        }
        return root;
    }
}
