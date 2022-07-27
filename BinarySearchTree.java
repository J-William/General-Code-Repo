/*
	Textbook implementation of a basic binary search tree
*/
class BinarySearchTree {
	class Node {
		int key;
		Node left, right;
		
		// Constructor
		public Node(int item) {
			key = item;
			left = right = null;
		}
	}
	
	// Attribute for the root node of the tree
	Node root;
	
	// Constructor
	BinarySearchTree() {
		root = null;
	}
	
	// Insert wrapper
	void insert(int key) {
		root = insertKey(root, key);
	}
	
	// Insert method
	Node insertKey(Node root, int key) {
		// If the tree is empty return a new node
		if (root == null) {
			root = new Node(key);
			return root;
		}
		
		// Traverse to the correct location for insertion
		if (key < root.key) 
			root.left = insertKey(root.left, key);
		else if (key > root.key)
			root.right = insertKey(root.right, key);
		
		return root;
	}
	
	// Traversal wrapper
	void inorder() {
		inorderRec(root);
	}
	
	// Inorder traversal
	void inorderRec(Node root) {
		if(root != null) {
			inorderRec(root.left);
			System.out.print(root.key + " -> ");
			inorderRec(root.right);
		}
	}
	
	// Delete wrapper
	void deleteKey(int key) {
		root = deleteRec(root, key);
	}
	
	// Delete
	Node deleteRec(Node root, int key) {
		// if the tree is empty return
		if (root == null)
			return root;
		// Search for the element to be deleted
		if (key < root.key)
			root.left = deleteRec(root.left, key);
		else if (key > root.key)
			root.right = deleteRec(root.right, key);
		else {
			// When found; if the target node has only one child, just return that subtree
			if (root.left == null)
				return root.right;
			else if (root.right == null)
				return root.left;
			
			// If there are two children; replace the target node with it's inorder successor
			root.key = minValue(root.right);
			// Then delete the successor
			root.right = deleteRec(root.right, root.key);
		}
		
		return root;
			
	}
	// Find the inorder successor
	int minValue(Node root) {
		int minv = root.key;
		while (root.left != null){
			minv = root.left.key;
			root = root.left;
		}
		return minv;
	}
	
	
	// Testing
	void print() {
		System.out.println(root.key);
		System.out.println(root.left.key);
		System.out.println(root.right.key);
	}
}