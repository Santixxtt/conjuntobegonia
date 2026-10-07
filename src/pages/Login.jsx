import { useState } from "react";
import { Link, useNavigate } from "react-router-dom"; // <-- Importamos useNavigate
import { ArrowLeft, Eye, EyeOff } from "lucide-react";
import LoginIllustration from "../components/login/illustration";
import logo from "../assets/img/logo.jpeg";

import desktopAnimated from "../assets/img/login/desktop-animated.gif";
import desktopStatic from "../assets/img/login/desktop-static.svg";
import mobileAnimated from "../assets/img/login/mobile-animated.gif";
import mobileStatic from "../assets/img/login/mobile-static.svg";

function LoginFields({ cedula, setCedula, password, setPassword, error, handleLogin }) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <>
      <h1 className="text-2xl font-bold text-begonia-700">Inicia sesión</h1>
      <p className="mt-1 text-sm text-neutral-500">
        Accede con el usuario asignado por la administración del conjunto.
      </p>

      {error && (
        <p className="mt-4 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-600">{error}</p>
      )}

      <form onSubmit={handleLogin} className="mt-5 flex flex-col gap-3">
        <div>
          <label className="mb-1 block text-sm font-medium text-neutral-700">Cédula</label>
          <input
            type="text"
            value={cedula}
            onChange={(e) => setCedula(e.target.value)}
            required
            className="w-full rounded-lg border border-neutral-300 px-3 py-2.5 text-sm outline-none transition focus:border-begonia-600 focus:ring-2 focus:ring-begonia-100"
          />
        </div>

        <div>
          <label className="mb-1 block text-sm font-medium text-neutral-700">Contraseña</label>
          <div className="relative">
            <input
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full rounded-lg border border-neutral-300 px-3 py-2.5 pr-10 text-sm outline-none transition focus:border-begonia-600 focus:ring-2 focus:ring-begonia-100"
            />
            <button
              type="button"
              onClick={() => setShowPassword((v) => !v)}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-neutral-400 hover:text-neutral-600"
              aria-label={showPassword ? "Ocultar contraseña" : "Mostrar contraseña"}
            >
              {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
            </button>
          </div>
        </div>

        <button
          type="submit"
          className="mt-2 rounded-full bg-begonia-600 py-2.5 text-sm font-medium text-white transition hover:bg-begonia-700"
        >
          Entrar
        </button>
      </form>
    </>
  );
}

export default function Login() {
  const [cedula, setCedula] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate(); // <-- Inicializamos el hook de navegación

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    const formData = new URLSearchParams();
    formData.append("username", cedula);
    formData.append("password", password);

    try {
      const response = await fetch("http://localhost:8000/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: formData.toString(),
      });

      if (!response.ok) {
        throw new Error("Cédula o contraseña incorrectos");
      }

      const data = await response.json();

      localStorage.setItem("token", data.access_token);
      localStorage.setItem("userRol", data.rol);
      localStorage.setItem("userName", data.nombre);

      // Usamos navigate en lugar de window.location.href para no recargar la app
      if (data.rol === "Admin") {
        navigate("/admin-dashboard");
      } else {
        navigate("/residente-dashboard");
      }
    } catch (err) {
      setError(err.message);
    }
  };

  const fieldsProps = { cedula, setCedula, password, setPassword, error, handleLogin };

  return (
    <>
      {/* Escritorio y tablet */}
      <div className="hidden min-h-screen items-center justify-center bg-[#F2F8EE] md:flex">
        <div className="mx-auto flex w-full max-w-5xl items-center justify-center gap-16 px-8 py-16">
          <div className="w-full max-w-sm rounded-[15px] bg-white p-8 shadow-xl">
            <Link to="/" className="mb-6 flex w-fit items-center gap-1.5 text-sm text-neutral-500 hover:text-begonia-700">
              <ArrowLeft className="h-4 w-4" />
              Volver al inicio
            </Link>
            <img src={logo} alt="Logo Begonia" className="mb-4 h-10 w-10 rounded-full object-cover" />
            <LoginFields {...fieldsProps} />
          </div>

          <div className="relative hidden flex-1 items-center justify-center md:flex">
            <LoginIllustration
              animatedSrc={desktopAnimated}
              staticSrc={desktopStatic}
              alt="Ilustración de inicio de sesión"
              className="h-[380px] w-[380px]"
            />
          </div>
        </div>
      </div>

      {/* Móvil */}
      <div className="relative flex min-h-screen flex-col md:hidden">
        <div
          className="absolute inset-0 bg-begonia-50 bg-contain bg-no-repeat"
          style={{
            backgroundImage: `url(${mobileStatic})`,
            backgroundPosition: "center calc(115% + 110px)",
          }}
          aria-hidden="true"
        />

        <div
          className="relative z-10 flex h-[75vh] flex-col justify-center bg-white px-6"
          style={{ borderBottomLeftRadius: "50% 60px", borderBottomRightRadius: "50% 60px" }}
        >
          <Link to="/" className="mb-6 flex w-fit items-center gap-1.5 text-sm text-neutral-500">
            <ArrowLeft className="h-4 w-4" />
            Volver al inicio
          </Link>
          <img src={logo} alt="Logo Begonia" className="mb-4 h-10 w-10 rounded-full object-cover" />
          <LoginFields {...fieldsProps} />
        </div>
      </div>
    </>
  );
}