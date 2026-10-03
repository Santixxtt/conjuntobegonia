import Header from "../components/layout/header";
import Hero from "../components/home/hero";
import Amenities from "../components/home/amenities";
import AboutLocation from "../components/home/about-location";
import VisitCounter from "../components/home/visit-counter";
import Footer from "../components/layout/footer";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <Header />
      <Hero />

      <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-10 md:px-6">
        <h2 className="text-3xl font-bold text-pink-600 md:text-4xl">Nuestra Página Web</h2>
        <p className="mt-2 max-w-2xl text-sm text-neutral-600">
          Aquí irán los módulos de comunicados, reservas de zonas comunes y PQR
          para los residentes del conjunto.
        </p>

        <div className="mt-8">
          <Amenities />
        </div>
      </main>

      <AboutLocation />
      <VisitCounter />
      <Footer />
    </div>
  );
}