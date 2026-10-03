import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import ComingSoon from "./pages/ComingSoon";
import Login from "./pages/Login";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/anuncios" element={<ComingSoon title="Anuncios" />} />
        <Route path="/administracion" element={<ComingSoon title="Administración" />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}