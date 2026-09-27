import Header from "../components/layout/header";
import Footer from "../components/layout/footer";

export default function ComingSoon({ title }) {
  return (
    <div className="flex min-h-screen flex-col">
      <Header />
      <main className="mx-auto flex w-full max-w-6xl flex-1 flex-col items-center justify-center px-4 text-center">
        <h1 className="text-2xl font-bold text-begonia-700">{title}</h1>
        <p className="mt-2 text-sm text-neutral-500">Este módulo se construirá en la siguiente fase.</p>
      </main>
      <Footer />
    </div>
  );
}