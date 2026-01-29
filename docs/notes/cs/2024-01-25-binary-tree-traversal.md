---
date: 2024-01-25
tags:
  - algorithm
  - tree
  - data-structure
---

# 이진 트리 순회 알고리즘

이진 트리를 순회하는 다양한 방법을 알아봅니다.

## 이진 트리 정의

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 순회 방법

### 1. 전위 순회 (Preorder)

**순서**: 루트 → 왼쪽 → 오른쪽

```python
def preorder(root):
    if not root:
        return []
    
    result = []
    result.append(root.val)
    result.extend(preorder(root.left))
    result.extend(preorder(root.right))
    return result

# 반복문 버전
def preorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # 오른쪽을 먼저 스택에 넣음 (나중에 처리)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

### 2. 중위 순회 (Inorder)

**순서**: 왼쪽 → 루트 → 오른쪽

!!! tip "이진 탐색 트리(BST)"
    중위 순회를 하면 정렬된 순서로 노드를 방문합니다.

```python
def inorder(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder(root.left))
    result.append(root.val)
    result.extend(inorder(root.right))
    return result

# 반복문 버전
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # 가장 왼쪽 노드까지 이동
        while current:
            stack.append(current)
            current = current.left
        
        # 현재 노드 처리
        current = stack.pop()
        result.append(current.val)
        
        # 오른쪽 서브트리로 이동
        current = current.right
    
    return result
```

### 3. 후위 순회 (Postorder)

**순서**: 왼쪽 → 오른쪽 → 루트

```python
def postorder(root):
    if not root:
        return []
    
    result = []
    result.extend(postorder(root.left))
    result.extend(postorder(root.right))
    result.append(root.val)
    return result

# 반복문 버전
def postorder_iterative(root):
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # 왼쪽을 먼저 스택에 넣음
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    # 결과를 역순으로 반환
    return result[::-1]
```

### 4. 레벨 순서 순회 (Level Order)

**순서**: 레벨별로 왼쪽에서 오른쪽

```python
from collections import deque

def levelorder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 시각화 예시

```
트리 구조:
       1
      / \
     2   3
    / \
   4   5

전위 순회: [1, 2, 4, 5, 3]
중위 순회: [4, 2, 5, 1, 3]
후위 순회: [4, 5, 2, 3, 1]
레벨 순회: [[1], [2, 3], [4, 5]]
```

## 시간 복잡도

| 순회 방법 | 시간 복잡도 | 공간 복잡도 |
|----------|------------|------------|
| 전위     | O(n)       | O(h)       |
| 중위     | O(n)       | O(h)       |
| 후위     | O(n)       | O(h)       |
| 레벨     | O(n)       | O(w)       |

- n: 노드의 개수
- h: 트리의 높이
- w: 트리의 최대 너비

## 참고 자료

- [LeetCode - Binary Tree Traversal](https://leetcode.com/tag/tree/)
- [VisuAlgo - Binary Tree](https://visualgo.net/en/bst)

---

[← Back to CS Notes](/notes/cs/)
