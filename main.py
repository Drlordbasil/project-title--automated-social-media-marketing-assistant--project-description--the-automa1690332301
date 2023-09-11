Commit Message: Use list comprehension to simplify creating lists
Pull Request Description:
Used list comprehension to simplify creating lists in the Python script. This change improves code readability and efficiency.

Commit:
```python
- res = []
- for item in data:
- if condition(item):
-         res.append(item)
+ res = [item for item in data if condition(item)]
```

Commit Message: Remove unnecessary variable assignments
Pull Request Description:
Removed unnecessary variable assignments in the Python script. This change improves code clarity.

Commit:
```python
- temp = data.copy()
- result = []
- for item in temp:
- if condition(item):
-         result.append(item)
+ result = [item for item in data.copy() if condition(item)]
```

Commit Message: Use generator expression instead of iterating over a list
Pull Request Description:
Used generator expression instead of iterating over a list in the Python script. This change improves memory efficiency and performance.

Commit:
```python
- res = []
- for item in data:
- if condition(item):
-         res.append(item)
+ res = (item for item in data if condition(item))
```

Commit Message: Use appropriate data structure for improved performance
Pull Request Description:
Used appropriate data structure in the Python script for improved performance. This change ensures efficient data handling.

Commit:
```python
- res = []
- for item in data:
- if condition(item):
-         res.append(item)
+ res = set(item for item in data if condition(item))
```
