# 🎓 AI University Chatbot (RAG-Based)

A context-aware AI chatbot that helps students instantly get answers from official university documents like **prospectuses, FAQs, and orientation handbooks** — all powered by a **Retrieval-Augmented Generation (RAG)** pipeline and **Gemini Pro**.

---

## 🧠 Problem

Students often struggle to find quick, accurate, and official information buried in lengthy university PDFs. Whether it’s “What are the credit hour requirements for CS?” or “Can I defer my admission?”, getting timely answers is frustrating.

---

## ✅ Solution

This chatbot solves that by:
- Parsing multiple academic PDFs (NED, FAST, etc.)
- Chunking & embedding content using `MiniLM`
- Retrieving relevant sections with `FAISS`
- Generating precise, readable answers using `Gemini Pro`
- Rendering clean Markdown responses in a Flask web app

---

## 💡 Features

- 🔍 **Ask Natural Language Questions**  
  Ask anything from “What is the minimum CGPA to stay enrolled?” to “How long is the orientation?”

- 📄 **Multi-PDF Support**  
  Upload multiple university documents — each is chunked and tagged by source

- 💬 **Gemini Pro Integration**  
  Generates context-rich, human-like responses

- 🧠 **Semantic Retrieval (RAG)**  
  Uses MiniLM + FAISS to retrieve the most relevant information

- 🖥️ **Flask App with Sidebar UI**  
  Clean, responsive layout with a fixed input bar and Markdown formatting

---

## 🛠️ Tech Stack

| Component        | Technology                    |
|------------------|-------------------------------|
| Embedding Model  | `sentence-transformers (MiniLM)` |
| Vector Store     | `FAISS`                       |
| LLM              | `Gemini Pro`                  |
| Web Framework    | `Flask + Jinja2`              |
| Frontend         | `Bootstrap 5 + Markdown`      |
| PDF Parsing      | `PyPDF2`                      |

---

## 🚀 How It Works

1. **PDF Ingestion:**  
   Run `pdf_ingestion.py` to parse and chunk all PDFs in the `/documents` folder.

2. **Embedding:**  
   Each chunk is embedded using MiniLM and stored in `chunks.pkl`.

3. **Querying:**  
   The user submits a question → embedding generated → similar chunks retrieved from FAISS.

4. **Response Generation:**  
   Top chunks + user query passed to **Gemini Pro**, which generates the final answer.

5. **Display:**  
   Answer rendered in Markdown format on the web UI.

---


---

## 🧪 Sample Questions

- What is the minimum CGPA requirement?
- Can I freeze my semester?
- What is the attendance policy?
- Is there an orientation program before classes?

---

## 🎯 Future Improvements

- PDF uploader from the frontend
- Multilingual support (Urdu/English)
- Student profile-based suggestions
- Query logging + feedback button

---

## 🙋‍♂️ Author

**Muhammad Raahim Rizwan**  
BS (Computer Science) — NED University  
Specializing in Data Science & Computer Vision  
[🔗 LinkedIn](https://www.linkedin.com/in/m-raahim-rizwan-425227214/)  
[💻 GitHub](https://github.com/123MRaahimRizwan)
