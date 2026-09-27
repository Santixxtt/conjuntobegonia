import { useState } from "react";
import { NavLink } from "react-router-dom";
import { Home, Megaphone, ShieldCheck, Building2, Flower2, Menu, X} from "lucide-react";

const links = [
  { to: "/", label: "Inicio", icon: Home },
  { to: "/anuncios", label: "Anuncios", icon: Megaphone },
  { to: "/sgsst", label: "SGSST", icon: ShieldCheck },
  { to: "/administracion", label: "Administración", icon: Building2 },
];

function NavItem({ to, label, icon: Icon, onClick }) {
  return (
    <NavLink
      to={to}
      onClick={onClick}
      className={({ isActive }) =>
        [
          "relative flex items-center px-4 py-2.5 text-sm font-medium transition-all duration-200 rounded-t-xl",
          isActive
            ? [
                "bg-white text-begonia-700 [&_span]:border-pink-500 md:translate-y-3",
                "before:content-[''] before:absolute before:bottom-0 before:left-[-12px] before:h-[12px] before:w-[12px]",
                "before:bg-[radial-gradient(circle_at_top_left,transparent_12px,white_12px)]",
                "after:content-[''] after:absolute after:bottom-0 after:right-[-12px] after:h-[12px] after:w-[12px]",
                "after:bg-[radial-gradient(circle_at_top_right,transparent_12px,white_12px)]",
              ].join(" ")
            : "text-white/80 hover:text-white [&_span]:border-transparent",
        ].join(" ")
      }
    >
      <span className="flex items-center gap-1.5 border-b-[3px] pb-0.5 transition-colors">
        <Icon className="h-4 w-4" />
        {label}
      </span>
    </NavLink>
  );
}

export default function Header() {
  const [open, setOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-begonia-600 shadow-md">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 md:px-6">
        <div className="flex items-center gap-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-full bg-white/15">
            <Flower2 className="h-5 w-5 text-white" />
          </span>
          <div className="leading-tight">
            <p className="text-xs font-medium text-begonia-50/80">Conjunto</p>
            <p className="text-lg font-bold tracking-wide text-white">BEGONIA</p>
          </div>
        </div>

        <nav className="hidden items-center gap-1 md:flex">
          {links.map((link) => (
            <NavItem key={link.to} {...link} />
          ))}
        </nav>

        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          className="rounded-md p-2 text-white md:hidden"
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
        </nav>
      )}
    </header>
  );
}