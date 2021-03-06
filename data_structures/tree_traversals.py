class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key

    
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val, end=" ")
        Inorder(root.right)
        
def Preorder(root):
    if root:
        print(root.val, end=" ")
        Preorder(root.left)
        Preorder(root.right)
            
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.val, end=" ")
                      

if __name__=='__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    
    print("\nPreorder traversal of binary tree is",end='\n')
    Preorder(root) 
  
    print("\nInorder traversal of binary tree is",end='\n')
    Inorder(root) 
  
    print("\nPostorder traversal of binary tree is",end='\n')
    Postorder(root) 
    
    
    
    
