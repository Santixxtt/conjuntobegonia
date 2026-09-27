import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import ComingSoon from "./pages/ComingSoon";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/anuncios" element={<ComingSoon title="Anuncios" />} />
        <Route path="/sgsst" element={<ComingSoon title="SGSST" />} />
        <Route path="/administracion" element={<ComingSoon title="Administración" />} />
      </Routes>
    </BrowserRouter>
  );
}