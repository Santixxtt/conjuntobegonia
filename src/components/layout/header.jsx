import { useState } from "react";
import { NavLink, Link } from "react-router-dom";
import { Home, Megaphone, Building2, Menu, X, User } from "lucide-react";
import logo from "../../assets/img/logo.jpeg";

const links = [
  { to: "/", label: "Inicio", icon: Home },
  { to: "/anuncios", label: "Anuncios", icon: Megaphone },
  { to: "/administracion", label: "Administración", icon: Building2 },
];

function NavItem({ to, label, icon: Icon, onClick }) {
  return (
    <NavLink
      to={to}
      onClick={onClick}
      className={({ isActive }) =>
        [
          "flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-medium transition-colors",
          isActive
            ? "bg-white/15 text-white"
            : "text-white/70 hover:bg-white/10 hover:text-white",
        ].join(" ")
      }
    >
      <Icon className="h-4 w-4" />
      {label}
    </NavLink>
  );
}

export default function Header() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-begonia-600 shadow-md">
      <div className="mx-auto grid max-w-6xl grid-cols-[auto_1fr_auto] items-center gap-4 px-4 py-3 md:px-6">
        <div className="flex items-center gap-2">
          <img src={logo} alt="Logo Begonia" className="h-9 w-9 rounded-full object-cover" />
          <div className="leading-tight">
            <p className="text-xs font-medium text-begonia-50/80">Conjunto</p>
            <p className="text-lg font-bold tracking-wide text-white">BEGONIA</p>
          </div>
        </div>

        <nav className="hidden items-center justify-center gap-2 md:flex">
          {links.map((link) => (
            <NavItem key={link.to} {...link} />
          ))}
        </nav>

        <div className="hidden justify-end md:flex">
          <Link
            to="/login"
            className="flex items-center gap-1.5 rounded-full bg-white px-4 py-2 text-sm font-medium text-begonia-700 transition hover:bg-begonia-50"
          >
            <User className="h-4 w-4" />
            Iniciar sesión
          </Link>
        </div>

        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="col-start-3 justify-self-end rounded-md p-2 text-white md:hidden"
          aria-label="Abrir menú"
        >
          {open ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </div>

      {open && (
        <nav className="flex flex-col gap-1 border-t border-white/10 bg-begonia-600 px-4 pb-4 md:hidden">
          {links.map((link) => (
            <NavItem key={link.to} {...link} onClick={() => setOpen(false)} />
          ))}
          <Link
            to="/login"
            onClick={() => setOpen(false)}
            className="mt-2 flex items-center gap-1.5 rounded-full bg-white px-4 py-2 text-sm font-medium text-begonia-700"
          >
            <User className="h-4 w-4" />
            Iniciar sesión
          </Link>
        </nav>
      )}
    </header>
  );
}