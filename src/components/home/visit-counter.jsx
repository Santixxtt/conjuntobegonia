import { useEffect, useState } from "react";
import { Eye } from "lucide-react";

export default function VisitCounter() {
  const [count, setCount] = useState(null);

  useEffect(() => {
    fetch("https://abacus.jasoncameron.dev/hit/begonia-ciudadverde-soacha.co/visitas")
      .then((res) => res.json())
      .then((data) => setCount(data.value))
      .catch(() => setCount(null));
  }, []);

  return (
    <section className="mx-auto max-w-6xl px-4 py-10 text-center md:px-6">
      <p className="flex items-center justify-center gap-2 text-sm text-neutral-500">
        <Eye className="h-4 w-4" />
        {count === null ? "Cargando visitas..." : `${count.toLocaleString("es-CO")} visitas a esta página`}
      </p>
    </section>
  );
}