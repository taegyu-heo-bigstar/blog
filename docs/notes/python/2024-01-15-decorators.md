---
date: 2024-01-15
tags:
  - python
  - decorators
  - advanced
---

# Python 데코레이터 이해하기

데코레이터는 함수나 메서드를 수정하지 않고 기능을 확장할 수 있는 Python의 강력한 기능입니다.

## 기본 개념

데코레이터는 다른 함수를 인자로 받아 새로운 함수를 반환하는 함수입니다.

```python
def my_decorator(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 실행 결과

```
함수 실행 전
Hello!
함수 실행 후
```

## 인자를 받는 데코레이터

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"함수 {func.__name__} 호출")
        result = func(*args, **kwargs)
        print(f"함수 {func.__name__} 완료")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 5)  # 8
```

## 실제 활용 예시

### 1. 실행 시간 측정

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 실행 시간: {end - start:.4f}초")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "완료"
```

### 2. 로깅

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] 함수 {func.__name__} 호출됨")
        print(f"[LOG] 인자: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] 반환값: {result}")
        return result
    return wrapper
```

## 주의사항

!!! warning "functools.wraps 사용"
    데코레이터를 만들 때는 `functools.wraps`를 사용하여 원본 함수의 메타데이터를 보존해야 합니다.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## 참고 자료

- [Python 공식 문서 - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python - Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

[← Back to Python Notes](/notes/python/)
