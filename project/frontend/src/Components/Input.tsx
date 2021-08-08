import axios from "axios";
import React, {ChangeEvent, memo, useState, VFC} from "react";
import {Box, Button, Divider, Input, Stack} from "@chakra-ui/react";
import {useAllTasks} from "../hooks/useAlltasks";


export const InputManu: VFC = memo(() => {
    const [todoName, setTodoName] = useState('');
    const { getTodos, todos } = useAllTasks()
    const onChangeTask = (e: ChangeEvent<HTMLInputElement>) => setTodoName(e.target.value);
    const onClickAddTodo = async () => {
        if (todoName === "") return;
        const newTodo = {
            "id": todos.length + 1,
            "todo": todoName
        }
        await axios.post("http://localhost:8004/todos", newTodo,
            { headers: {'Content-Type': 'application/json'}, responseType: 'json' })
            .then(res => {
                getTodos();
            })
        setTodoName("");
    };

    return (
       <Box w={400}>
           <Stack spacing={5}>
               <Input
                   placeholder="Input task..."
                   value={todoName}
                   onChange={onChangeTask}
               />
                    <Button
                        colorScheme="teal"
                        onClick={onClickAddTodo}
                    >add</Button>
                <Divider my={"5"}/>
           </Stack>
       </Box>
   )
});