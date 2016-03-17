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

def isSymmetric(root):
	pre=[root]
	while len(pre)>0:
		first=[]
		second=[]
		for i in xrange((len(pre)+1)/2):
			if pre[i].left!=None or pre[-1-i].right!=None:
				if pre[i].left==None or pre[-1-i].right==None:
					return False
				if pre[i].left.val!=pre[-i-1].right.val:
					return False
				else:
					first.append(pre[i].left)
					second.append(pre[-1-i].right)
			if pre[i].right!=None or pre[-1-i].left!=None:
				if pre[i].right==None or pre[-1-i].left==None:
					return False
				if pre[i].right.val!=pre[-i-1].left.val:
					return False
				else:
					first.append(pre[i].right)
					second.append(pre[-1-i].left)
		pre=first+second[::-1]
	return True

def isSymmetric2(root):
	pre=[root]
	stack=[(root.left,root.right)]
	while len(stack)>0:
		(l,r)=stack.pop()

		if l is None and r is None:
			continue
		if l is None or r is None:
			return False
		if l.val==r.val:
			stack.insert(0,(l.left,r.right))
			stack.insert(0,(r.left,l.right))
		else:
			return False
	return True



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

print isSymmetric2(root2)
print isSymmetric2(root)