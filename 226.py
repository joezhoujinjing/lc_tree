import copy
class TreeNode(object):
	def __init__(self,x):
		self.val=x
		self.left=None
		self.right=None

	def __repr__(self):
		print_out=[self.val]
		pre=[self]
		while len(pre)>0:
			cur=[]
			for p in pre:
				if p.left!=None:
					print_out.append(p.left.val)
					cur.append(p.left)
					if p.right==None:
						print_out.append('#')
						continue
				if p.right!=None:
					if p.left==None:
						print_out.append('#')
					print_out.append(p.right.val)
					cur.append(p.right)
			pre=cur
		return str(print_out)

def invertTree(root):
	pre=[root]
	while pre:
		p=pre.pop()
		p.left,p.right=p.right,p.left
		if p.left:
			pre.append(p.left)
		if p.right:
			pre.append(p.right)
	return root


root=TreeNode(1)
root.left=TreeNode(2)
root.left.right=TreeNode(3)
root.left.right.left=TreeNode(5)
print repr(root)

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(2)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(4)
root2.right.left=TreeNode(4)
root2.right.right=TreeNode(3)
print repr(root2)

print repr(invertTree(root2))
print repr(invertTree(root))