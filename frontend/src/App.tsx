import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Products from "./screens/Products";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/products" element={<Products />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
