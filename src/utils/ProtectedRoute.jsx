import { Navigate, Outlet } from 'react-router-dom';

export const ProtectedRoute = () => {
  // Verificamos si existe el token en el almacenamiento local
  const isAuthenticated = localStorage.getItem('token') !== null;

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  // Si está autenticado, renderizamos la vista solicitada (Outlet)
  return <Outlet />;
};