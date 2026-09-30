"use client";
import { useState } from "react";

interface Certificado {
  nome: string;
  curso: string;
  cargaHoraria: string;
}

export default function Home() {
  const [dados, setDados] = useState<Certificado>({
    nome: "",
    curso: "",
    cargaHoraria: "",
  });
  const [carregando, setCarregando] = useState(false);

  async function gerarCertificado(e: React.FormEvent) {
    e.preventDefault();
    setCarregando(true);

    try {
      const resposta = await fetch(
        "https://gerador-certificado-rwmz.onrender.com/certificado",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(dados),
        }
      );

      if (resposta.ok) {
        const arquivo = await resposta.blob();
        const url = window.URL.createObjectURL(arquivo);
        const link = document.createElement("a");
        link.href = url;
        link.download = `certificado-${dados.nome.toLowerCase().replace(/\s+/g, "-") || "aluno"}.pdf`;
        link.click();
        window.URL.revokeObjectURL(url);
      } else {
        alert("Erro ao gerar o certificado. Tente novamente.");
      }
    } catch (error) {
      console.error(error);
      alert("Erro de conexão com o servidor.");
    } finally {
      setCarregando(false);
    }
  }

  const formValido = dados.nome && dados.curso && dados.cargaHoraria;

  return (
    <main className="min-h-screen bg-slate-950 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.3),rgba(255,255,255,0))] flex items-center justify-center p-4">
      <div className="w-full max-w-lg bg-slate-900/80 backdrop-blur-md border border-slate-800 rounded-2xl shadow-2xl p-8 transition-all">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Gerador de Certificados
          </h1>
          <p className="text-slate-400 text-sm mt-2">
            Preencha os dados abaixo para emitir o documento em PDF
          </p>
        </div>

        <form onSubmit={gerarCertificado} className="space-y-5">
          <div>
            <label className="block text-xs font-medium text-slate-300 uppercase tracking-wider mb-2">
              Nome do Aluno
            </label>
            <input
              type="text"
              required
              placeholder="Ex: João da Silva"
              className="w-full bg-slate-800/60 border border-slate-700/80 rounded-xl px-4 py-3 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              value={dados.nome}
              onChange={(e) => setDados({ ...dados, nome: e.target.value })}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 uppercase tracking-wider mb-2">
              Nome do Curso
            </label>
            <input
              type="text"
              required
              placeholder="Ex: Desenvolvedor Full-Stack"
              className="w-full bg-slate-800/60 border border-slate-700/80 rounded-xl px-4 py-3 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              value={dados.curso}
              onChange={(e) => setDados({ ...dados, curso: e.target.value })}
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 uppercase tracking-wider mb-2">
              Carga Horária
            </label>
            <input
              type="text"
              required
              placeholder="Ex: 120 horas"
              className="w-full bg-slate-800/60 border border-slate-700/80 rounded-xl px-4 py-3 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              value={dados.cargaHoraria}
              onChange={(e) =>
                setDados({ ...dados, cargaHoraria: e.target.value })
              }
            />
          </div>

          <button
            type="submit"
            disabled={!formValido || carregando}
            className="w-full mt-4 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-semibold rounded-xl p-3.5 shadow-lg shadow-blue-500/25 disabled:opacity-50 disabled:cursor-not-allowed disabled:shadow-none transition-all flex items-center justify-center gap-2"
          >
            {carregando ? (
              <>
                <svg
                  className="animate-spin h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                  ></path>
                </svg>
                <span>Gerando Certificado...</span>
              </>
            ) : (
              "Gerar e Baixar PDF"
            )}
          </button>
        </form>
      </div>
    </main>
  );
}