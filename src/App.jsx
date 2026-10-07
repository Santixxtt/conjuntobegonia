import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/home';
import Login from './pages/Login';
import ComingSoon from './pages/ComingSoon';
import { ProtectedRoute } from './utils/ProtectedRoute';
import './App.css'; 

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rutas Públicas */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        
        {/* Rutas públicas temporales hacia ComingSoon */}
        <Route path="/anuncios" element={<ComingSoon />} />
        <Route path="/administracion" element={<ComingSoon />} />
        
        {/* Ruta general de ComingSoon */}
        <Route path="/coming-soon" element={<ComingSoon />} />

        {/* Rutas Protegidas (Solo accesibles si hay token) */}  
        <Route element={<ProtectedRoute />}>
          {/* Aquí irán los componentes reales cuando los crees. 
              Por ahora, los enviamos a ComingSoon para que no den error al hacer login */}
          <Route path="/admin-dashboard" element={<ComingSoon />} />
          <Route path="/residente-dashboard" element={<ComingSoon />} />
        </Route>

        {/* Redirección por defecto si la ruta no existe */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;