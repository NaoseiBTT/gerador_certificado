"use client"
import { useState } from "react";

interface Certificado {
  nome:string,
  curso: string,
  cargaHoraria:string
}

export default function Home() {

  const [dados, setDados] = useState<Certificado>({
    nome: "",
    curso: "",
    cargaHoraria: "",
  });

  async function gerarCertificado() {
   
    const resposta = await fetch("https://gerador-certificado-rwmz.onrender.com/certificado",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify(dados)
    })

    if(resposta.ok){
      const arquivo = await resposta.blob()

      const url = window.URL.createObjectURL(arquivo)

      const link = document.createElement("a")
      link.href = url

      link.download = "certificado.pdf"

      link.click()

      
    } else{
      alert("Erro ao enviar dados")
    }

    
  }




  return (
    <main className="min-h-screen bg-slate-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md">
          <h1 className="text-3xl font-bold text-center mb-6">Sistema - Certificados</h1>

          <div className="mb-4">
              <label className="block mb-2">Nome</label>

              <input
              className="w-full border rounded-lg p-2"
              value={dados.nome}
              onChange={(e)=> setDados({...dados, nome: e.target.value})}
              />
          </div>


          <div className="mb-4">
              <label className="block mb-2">Curso</label>

              <input
              className="w-full border rounded-lg p-2"
              value={dados.curso}
              onChange={(e)=> setDados({...dados, curso: e.target.value})}
              />
          </div>

          <div className="mb-4">
              <label className="block mb-2">Carga Horaria</label>

              <input
              className="w-full border rounded-lg p-2"
              value={dados.cargaHoraria}
              onChange={(e)=> setDados({...dados, cargaHoraria: e.target.value})}
              />
          </div>

          <button onClick={gerarCertificado} 
          className="w-full bg-blue-600 text-white rounded-lg p-3 hover:bg-blue-700 cursor-pointer ">
            Gerar Certificado
          </button>
      </div>
    </main>
  );
}
