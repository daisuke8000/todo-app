import React from 'react';


import { Basepage } from "./Components/Basepage";

import {
    ChakraProvider,
} from "@chakra-ui/react";
import theme from "./theme/theme";


function App() {
  return (
    <>
      <header className="App-header">
          <ChakraProvider theme={theme}>
              <Basepage/>
          </ChakraProvider>
      </header>
    </>
  );
}

export default App;
