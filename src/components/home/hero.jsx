import { useEffect, useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import hero1 from "../../assets/img/carrusel_1.jpg";
import hero2 from "../../assets/img/carrusel_2.jpeg";
import hero3 from "../../assets/img/carusel_3.jpeg";

const slides = [hero1, hero2, hero3];
const AUTOPLAY_MS = 6000;

export default function Hero() {
  const [index, setIndex] = useState(0);

  const goTo = (i) => setIndex((i + slides.length) % slides.length);
  const next = () => goTo(index + 1);
  const prev = () => goTo(index - 1);

  useEffect(() => {
    const timer = setInterval(next, AUTOPLAY_MS);
    return () => clearInterval(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index]);

  return (
    <div className="mx-auto max-w-6xl px-4 pt-8 md:px-6">
      <section className="relative aspect-[21/9] w-full overflow-hidden rounded-2xl shadow-md md:aspect-[2.3/1]">
        <div
          className="flex h-full transition-transform duration-700 ease-in-out"
          style={{ transform: `translateX(-${index * 100}%)` }}
        >
          {slides.map((src, i) => (
            <img
              key={i}
              src={src}
              alt={`Conjunto Begonia - foto ${i + 1}`}
              className="h-full w-full flex-shrink-0 object-cover"
            />
          ))}
        </div>

        <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/70 to-transparent px-6 py-6 md:px-10 md:py-8">
          <h1 className="text-2xl font-bold text-white md:text-4xl">BEGONIA</h1>
          <p className="text-sm text-white/90 md:text-base">Un hogar para todos.</p>
        </div>

        <button
          type="button"
          onClick={prev}
          aria-label="Foto anterior"
          className="absolute left-3 top-1/2 flex h-9 w-9 -translate-y-1/2 items-center justify-center rounded-full bg-black/40 text-white transition hover:bg-black/60"
        >
          <ChevronLeft className="h-5 w-5" />
        </button>
        <button
          type="button"
          onClick={next}
          aria-label="Foto siguiente"
          className="absolute right-3 top-1/2 flex h-9 w-9 -translate-y-1/2 items-center justify-center rounded-full bg-black/40 text-white transition hover:bg-black/60"
        >
          <ChevronRight className="h-5 w-5" />
        </button>

        <div className="absolute bottom-3 left-1/2 flex -translate-x-1/2 gap-2">
          {slides.map((_, i) => (
            <button
              key={i}
              type="button"
              onClick={() => goTo(i)}
              aria-label={`Ir a la foto ${i + 1}`}
              className={[
                "h-2 w-2 rounded-full transition-all",
                i === index ? "w-5 bg-white" : "bg-white/50 hover:bg-white/80",
              ].join(" ")}
            />
          ))}
        </div>
      </section>
    </div>
  );
}