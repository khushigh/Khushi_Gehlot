import { useState, useEffect } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    useEffect(() => {
        console.log('useEffect called');
        alert(`You clicked ${count} times`);
    }, [count]);

    return (
        <div className="Container" style={{ margin: '20px' }}>
            <button onClick={() => setCount(count + 1)}>
                Click me </button>
            <p>You clicked {count} times</p>
        </div>
    );
}
export default Counter;