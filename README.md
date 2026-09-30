# 🚀 Sistema de Certificados

Sistema de emissão de certificados desenvolvido utilizando **Next.js, Python Flask e Docker**.

O projeto demonstra a comunicação entre diferentes serviços utilizando containers Docker.

---

## 📌 Sobre o projeto

O Sistema permite que um usuário informe:

- Nome do participante
- Curso realizado
- Carga horária

Após o envio dos dados, a API Python gera automaticamente um certificado em PDF utilizando a biblioteca ReportLab.

---

## 🏗️ Arquitetura

            Usuário

               |
               |

          Next.js

               |
               |
         HTTP Request

               |
               |

         Flask API

               |
               |

        ReportLab PDF

               |
               |

      Certificado.pdf
---

## 🛠️ Tecnologias utilizadas

### Front-end

- Next.js
- React
- TypeScript
- Tailwind CSS


### Back-end

- Python
- Flask
- ReportLab


### DevOps

- Docker
- Docker Compose


---


---

# ▶️ Como executar

## Pré-requisitos

Ter instalado:

- Docker
- Docker Compose


---

## Executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO