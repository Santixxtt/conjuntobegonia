import { Baby, Store, PartyPopper, Flame, Trees, Dumbbell, Car, ShieldCheck, PawPrint } from "lucide-react";

// Ajusta este arreglo cuando confirmes qué tiene realmente el conjunto
const amenities = [
  { icon: Baby, label: "Jardín infantil", desc: "Zona de juegos para los más pequeños" },
  { icon: Store, label: "Tienda", desc: "Minimarket dentro del conjunto" },
  { icon: PartyPopper, label: "Salón social", desc: "Para reuniones y eventos" },
  { icon: Flame, label: "Zona BBQ", desc: "Espacio de asados comunitario" },
  { icon: Trees, label: "Parque infantil", desc: "Zonas verdes y juegos al aire libre" },
  { icon: Dumbbell, label: "Gimnasio", desc: "Equipado para los residentes" },
  { icon: Car, label: "Parqueadero", desc: "Zona de parqueo vehicular" },
  { icon: ShieldCheck, label: "Portería 24h", desc: "Vigilancia permanente" },
  { icon: PawPrint, label: "Zona de mascotas", desc: "Espacio pensado para tus mascotas" },
];

export default function Amenities() {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {amenities.map(({ icon: Icon, label, desc }) => (
        <div
          key={label}
          className="flex gap-3 rounded-xl border border-neutral-200 bg-white p-4 shadow-sm transition hover:shadow-md"
        >
          <span className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-lg bg-begonia-50 text-begonia-700">
            <Icon className="h-5 w-5" />
          </span>
          <div>
            <p className="font-medium text-begonia-700">{label}</p>
            <p className="text-sm text-neutral-500">{desc}</p>
          </div>
        </div>
      ))}
    </div>
  );
}