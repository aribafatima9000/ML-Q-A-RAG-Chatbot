Production-Ready Simple RAG ChatbotThis repository contains a professional-grade, lightweight Retrieval-Augmented Generation (RAG) chatbot. It is designed to ingest local text documents, index them into a vector store, and retrieve relevant context to answer user queries with high factual accuracy, preventing LLM hallucinations.Architecture OverviewThe RAG workflow follows a standard, industry-grade pipeline:[ Document (.txt) ] ──> [ Chunking ] ──> [ Embeddings (OpenAI) ] ──> [ Vector Store (FAISS) ]
                                                                             │
                                                                             ▼
[ User Query ] ─────────────────> [ Semantic Search ] ──────────────> [ Context Retrieval ]
                                                                             │
                                                                             ▼
[ Final Answer ] <────────────── [ LLM (GPT-4o) ] <────────────────── [ Prompt Synthesis ]
Ingestion & Chunking: Raw documents are split into smaller, overlapping chunks to preserve local context.Embedding & Indexing: Chunks are converted into high-dimensional vector representations using OpenAI's embedding models and stored in a local FAISS vector database.Retrieval: When a user asks a question, the system queries the FAISS database to retrieve the top-$k$ most semantically similar text chunks.Generation: The retrieved chunks are stuffed into a system prompt template as "ground truth" context, and the LLM generates a highly contextualized response.
