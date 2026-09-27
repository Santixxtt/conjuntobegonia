import Header from "../components/layout/header";
import Hero from "../components/home/hero";
import Footer from "../components/layout/footer";

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <Header />
      <Hero />

      <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-10 md:px-6">
        <h2 className="text-center font-semibold text-begonia-900">Nuestra Página Web</h2>
        <p className="mt-2  text-center text-neutral-600">
          Esta es nuestra página, sigue en crecimiento y va a tener mejores funciones dentro de lo posible, usala, enterate de cosas y no dudes en crear un PQR si tienes dudas o ves que esta fallando la página. ¡Que disfrutes esta nueva integración!!
        </p>
      </main>

      <Footer />
    </div>
  );
}