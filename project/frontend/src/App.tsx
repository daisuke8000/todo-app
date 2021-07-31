import React from 'react';
import './App.css';
import Todo from './Components/Todo';
import { ChakraProvider } from "@chakra-ui/react";
// import theme from "./theme/theme";


function App() {
  return (
    <div className="App">
      <header className="App-header">
          <ChakraProvider>
              <Todo/>
          </ChakraProvider>
      </header>
    </div>
  );
}

export default App;
