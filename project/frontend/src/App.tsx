import React from 'react';
import logo from './logo.svg';
import './App.css';
import Todo from './Components/Todo';
import { ChakraProvider } from "@chakra-ui/react";


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
