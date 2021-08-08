import React, { memo, VFC } from "react";
import {Box, Flex, Heading, Stack} from "@chakra-ui/react";
import { InputManu } from "./Input";
import { Todos } from "./Todos";


export const Basepage: VFC = memo(() => {
   return (
       <Flex
           align="center"
           color="gray.500"
           height="100vh"
           justify="center"
       >
          <Box
          w="">
             <Stack spacing={6}>
                <Heading
                    as="h1"
                    size="lg"
                    textAlign="center"
                >TodoApp
                </Heading>
                <InputManu/>
                <Todos/>
             </Stack>
          </Box>
       </Flex>
   )
});