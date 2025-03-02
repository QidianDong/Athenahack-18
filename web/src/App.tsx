
import { BrowserRouter, Routes, Route } from "react-router";
import Index from "./routes/index.tsx"


function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Index />} />
    </Routes>
  </BrowserRouter>
  );
}

export default App;
