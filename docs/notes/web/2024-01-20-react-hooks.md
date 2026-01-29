---
date: 2024-01-20
tags:
  - react
  - hooks
  - javascript
---

# React Hooks 완벽 가이드

React Hooks는 함수형 컴포넌트에서 상태와 생명주기 기능을 사용할 수 있게 해주는 기능입니다.

## 주요 Hooks

### useState

상태를 관리하는 가장 기본적인 Hook입니다.

```javascript
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        증가
      </button>
    </div>
  );
}
```

### useEffect

사이드 이펙트를 처리하는 Hook입니다.

```javascript
import { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);
  
  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(data => setData(data));
  }, []); // 빈 배열: 마운트 시 한 번만 실행
  
  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}
```

### useContext

Context API를 사용하기 쉽게 만들어주는 Hook입니다.

```javascript
import { createContext, useContext } from 'react';

const ThemeContext = createContext('light');

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return <button className={theme}>버튼</button>;
}
```

## 커스텀 Hook

자주 사용하는 로직을 재사용 가능한 Hook으로 만들 수 있습니다.

```javascript
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(error);
    }
  };
  
  return [storedValue, setValue];
}

// 사용 예시
function App() {
  const [name, setName] = useLocalStorage('name', 'Anonymous');
  
  return (
    <input
      value={name}
      onChange={(e) => setName(e.target.value)}
    />
  );
}
```

## Hooks 규칙

!!! danger "반드시 지켜야 할 규칙"
    1. **최상위에서만 호출**: 반복문, 조건문, 중첩 함수 내에서 Hook을 호출하지 마세요
    2. **React 함수에서만 호출**: 일반 JavaScript 함수에서는 Hook을 호출하지 마세요

```javascript
// ❌ 잘못된 사용
function BadComponent() {
  if (condition) {
    const [state, setState] = useState(0); // 조건문 안에서 사용
  }
}

// ✅ 올바른 사용
function GoodComponent() {
  const [state, setState] = useState(0);
  
  if (condition) {
    // 조건문 안에서는 state 사용만
    setState(newValue);
  }
}
```

## 성능 최적화

### useMemo

계산 비용이 높은 값을 메모이제이션합니다.

```javascript
import { useMemo } from 'react';

function ExpensiveComponent({ data }) {
  const expensiveValue = useMemo(() => {
    return data.reduce((acc, item) => acc + item.value, 0);
  }, [data]); // data가 변경될 때만 재계산
  
  return <div>{expensiveValue}</div>;
}
```

### useCallback

함수를 메모이제이션합니다.

```javascript
import { useCallback } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);
  
  const increment = useCallback(() => {
    setCount(c => c + 1);
  }, []); // 함수가 변경되지 않음
  
  return <ChildComponent onIncrement={increment} />;
}
```

## 참고 자료

- [React 공식 문서 - Hooks](https://react.dev/reference/react)
- [useState 심화](https://react.dev/reference/react/useState)
- [useEffect 완벽 가이드](https://overreacted.io/a-complete-guide-to-useeffect/)

---

[← Back to Web Notes](/notes/web/)
