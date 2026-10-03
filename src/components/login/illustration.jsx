import { useEffect, useRef, useState } from "react";

export default function LoginIllustration({ animatedSrc, staticSrc, alt, className = "" }) {
  const [src, setSrc] = useState(staticSrc);
  const frameTimes = useRef([]);

  useEffect(() => {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const lowMemory = navigator.deviceMemory && navigator.deviceMemory < 4;
    const saveData = navigator.connection?.saveData;

    if (prefersReducedMotion || lowMemory || saveData) {
      setSrc(staticSrc);
      return;
    }

    setSrc(animatedSrc);

    let raf;
    let last = performance.now();
    const checkPerformance = (now) => {
      frameTimes.current.push(now - last);
      last = now;
      if (frameTimes.current.length < 30) {
        raf = requestAnimationFrame(checkPerformance);
      } else {
        const avg = frameTimes.current.reduce((a, b) => a + b, 0) / frameTimes.current.length;
        if (avg > 33) {
          // menos de ~30fps reales: el navegador va justo, usamos la versión estática
          setSrc(staticSrc);
        }
      }
    };
    raf = requestAnimationFrame(checkPerformance);

    // Deja que anime una vuelta y luego se congela
    const freeze = setTimeout(() => setSrc(staticSrc), 3500);

    return () => {
      cancelAnimationFrame(raf);
      clearTimeout(freeze);
    };
  }, [animatedSrc, staticSrc]);

  return (
    <div className={`relative ${className}`}>
      <div
        className="absolute left-1/2 top-[78%] h-24 w-48 -translate-x-1/2 -translate-y-1/2 rounded-full bg-pink-400/40 blur-2xl"
        aria-hidden="true"
      />
      <img src={src} alt={alt} className="relative h-full w-full object-contain" />
    </div>
  );
}