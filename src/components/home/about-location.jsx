import { MapPin } from "lucide-react";

export default function AboutLocation() {
  return (
    <section style={{ backgroundColor: "#f2f2f2" }} className="py-14">
      <div className="mx-auto grid max-w-6xl gap-10 px-4 md:grid-cols-2 md:px-6">
        <div>
          <p className="flex items-center gap-1.5 text-sm font-medium text-begonia-600">
            <MapPin className="h-4 w-4" />
            Ciudad Verde, Soacha
          </p>
          <h2 className="mt-2 text-2xl font-semibold text-pink-600 md:text-3xl">
            ¿Dónde estamos?
          </h2>
          <p className="mt-3 text-sm leading-relaxed text-neutral-600">
            El Conjunto Begonia hace parte del macroproyecto Ciudad Verde, en el sector
            noroccidental. La construcción inició en diciembre de 2009 y el conjunto se
            oficializó en marzo de 2010.
          </p>

          {/* Reemplaza estos valores por los datos exactos */}
          <dl className="mt-6 grid grid-cols-2 gap-x-4 gap-y-3 text-sm">
            <div>
              <dt className="text-neutral-500">Dirección</dt>
              <dd className="font-medium text-neutral-800">Carrera 32 # 17 - 156</dd>
            </div>
            <div>
              <dt className="text-neutral-500">Código postal</dt>
              <dd className="font-medium text-neutral-800">250051</dd>
            </div>
            <div>
              <dt className="text-neutral-500">Torres</dt>
              <dd className="font-medium text-neutral-800">13</dd>
            </div>
            <div>
              <dt className="text-neutral-500">Apartamentos</dt>
              <dd className="font-medium text-neutral-800">312</dd>
            </div>
            <div>
              <dt className="text-neutral-500">Inicio de obra</dt>
              <dd className="font-medium text-neutral-800">Diciembre 2009</dd>
            </div>
            <div>
              <dt className="text-neutral-500">Oficialización</dt>
              <dd className="font-medium text-neutral-800">Marzo 2010</dd>
            </div>
          </dl>
        </div>

        <div className="overflow-hidden rounded-xl border border-neutral-200 shadow-sm">
          <iframe
            title="Ubicación Conjunto Begonia"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.9464125516265!2d-74.22105452398202!3d4.603618842489381!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f750078d7e389%3A0x9aee29c92b2f897d!2sConjunto%20Residencial%20Begonia!5e0!3m2!1ses-419!2sco!4v1791049022992!5m2!1ses-419!2sco"
            className="h-80 w-full md:h-full"
            loading="lazy"
          />
        </div>
      </div>
    </section>
  );
}