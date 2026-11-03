import {useState} from 'react';

const useCount = (initialState=0): [number, () => void, () => void] => {
    const [count,setCount] = useState(initialState);

    const add = () => {
        setCount(count => count +1);
    }
    
    const substract = () => {
        setCount(count => count -1);
    }   

    return [count,add,substract];
}

export default useCount;
