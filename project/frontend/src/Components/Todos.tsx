import React, {memo, useEffect, VFC} from 'react';
import {Box, Text} from '@chakra-ui/react';
import { useAllTasks } from "../hooks/useAlltasks";

export const Todos: VFC = memo(() => {
    const { getTodos, todos } = useAllTasks()
    useEffect( () => getTodos(), [todos])

    return (
        <>
            {todos.map((item) => (
                <Box key={item.id}>
                    <Text>{item.todo}</Text>
                </Box>
            ))}
        </>
    )
});