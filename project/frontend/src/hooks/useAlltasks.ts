import axios from "axios";
import { Todos } from "../types/api/todos";
import {useCallback, useState } from "react";

export const useAllTasks = () => {
    const [todos, setTodos] = useState<Array<Todos>>([]);

    const getTodos = useCallback(() => {
        const response = async () => {
           await axios
                .get<Array<Todos>>("http://localhost:8004/todos")
                .then((res) => setTodos(res.data))
                .catch(() => {
                    alert("Sorry..")
                });
        }
        response()
    },[]);
    return { getTodos, todos };
};